from operator import index
import os
import random
import numpy as np
from PIL import Image
from tqdm import tqdm

from person import Person


EPOCH = 16  # Number of trainings
ID_START = 0
POP_SIZE = 128  # Number of starting images
PERSON_SIZE = (32, 32,)  # Size of images


class Population:

    def __init__(self, id_start, population_size, person_size, evaluation_function):
        self.population = []
        self.current_id = id_start
        self.population_size = population_size
        self.person_size = person_size
        self.evaluation_function = evaluation_function
        self.loop_counter = 0
        self.history = {
            'best_person': [],
            'worst_person': [],
            'population_size': [],
        }

    def get_new_id(self):
        self.current_id += 1
        return self.current_id - 1

    def remove_person(self, id):
        index = 0
        i = 0
        for p in self.population:
            if p.id == id:
                index = i
            i += 1
        self.population.pop(index)

    """
    Create a new population
    """
    def creation(self):
        #print("<{}. creation>".format(self.loop_counter))
        for i in range(self.population_size - len(self.population)):
            p = Person(self.get_new_id(), self.person_size)
            self.population.append(p)

    """
    Evaluate each person
    """
    def selection(self):
        #print("<{}. selection>".format(self.loop_counter))
        for person in self.population:
            person.score = self.evaluation_function(person)

        # Remove 25%-of the population
        goal_pop_size = (1 - 0.2) * len(self.population)
        best_person = max(self.population, key=lambda x: x.score)

        while len(self.population) > goal_pop_size:

            # Choose bad scored person's with higher propability
            choosen_person = random.choice(self.population)
            if random.random() > (choosen_person.score / (best_person.score + 1)):
                self.remove_person(choosen_person.id)

        #print("[{}.] Best avg:".format(self.loop_counter), best_person.get_avg())
        self.history['best_person'].append(best_person)
        self.history['worst_person'].append(min(self.population, key=lambda x: x.score))

    """
    Make random changes in different person's 
    """
    def mutation(self):
        #print("<{}. mutation>".format(self.loop_counter))

        mutation_count = int((0.27) * len(self.population))
        for i in range(mutation_count):
            person = random.choice(self.population)
            
            # Change n pixel
            n = 1 + int(random.random() * (person.x / 2) - 1)
            choosen_pixels = []

            for i in range(n):
                x, y = person.x, person.y
                x = int(random.random() * x - 1)
                y = int(random.random() * y - 1)
                
                if [x, y] in choosen_pixels:
                    x = int(random.random() * x - 1)
                    y = int(random.random() * y - 1)

                person.data[x][y] = 255*random.random() - 1
                choosen_pixels.append([x, y])

    def _crossing(self, person_a, person_b):
        xs, ys = person_a.x, person_a.y
        child = Person(self.get_new_id(), self.person_size)
        choosen_for_a = []
        choosen_for_b = []

        for i in range(int(xs*ys/2)):
            xi, yi = int(random.random()*xs - 1), int(random.random()*ys - 1)
            while [xi, yi] in choosen_for_a:
                xi, yi = int(random.random()*xs - 1), int(random.random()*ys - 1)
            choosen_for_a.append([xi, yi])

        # Choose the ones not choosen for person_a
        for x in range(xs):
            for y in range(ys):
                if [x, y] not in choosen_for_a:
                    choosen_for_b.append([x, y])

        """
        for i in range(int(xs*ys/2 - 2)):
            xi, yi = int(random.random()*xs - 1), int(random.random()*ys - 1)
            while [xi, yi] in choosen_for_a or [xi, yi] in choosen_for_b:
                xi, yi = int(random.random()*xs - 1), int(random.random()*ys - 1)
            choosen_for_b.append([xi, yi])
        """

        for index_a, index_b in zip(choosen_for_a, choosen_for_b):
            child.data[index_a[0]][index_a[1]] = person_a.data[index_a[0]][index_a[1]]
            child.data[index_b[0]][index_b[1]] = person_b.data[index_b[0]][index_b[1]]

        return child

    """
    :exclude: list of Persons
    """
    def _choice_score(self, exclude):
        self.population = sorted(self.population, key=lambda x: x.score, reverse=True)
        pop = self.population.pop(0)

        while pop in exclude:
            self.population.append(pop)
            pop = self.population.pop(0)

        self.population.append(pop)
        return pop

    """
    Cross the best persons with each other
    """
    def reproduction(self):
        #print("<{}. reproduction (pop_size: {})>".format(self.loop_counter, len(self.population)))

        cross_count = int(self.population_size - len(self.population))
        exclude = []

        for i in range(cross_count):
            person_a = self._choice_score(exclude)
            exclude.append(person_a)
            person_b = self._choice_score(exclude)
            exclude.append(person_b)

            while person_a is None:
                person_a = random.choice(self.population)
            
            while person_b is None or person_a.id == person_b.id:
                person_b = random.choice(self.population)

            new_person = self._crossing(person_a, person_b)
            self.population.append(new_person)

        #print("[{}.] Population size:".format(self.loop_counter), len(self.population))
        self.history['population_size'].append(len(self.population))

    def remove_nones(self):
        new_pop = []
        for pop in self.population:
            if pop is None:
                continue
            new_pop.append(pop)
        self.population = new_pop

    """
    Execute one step of evolution
    """
    def evolve(self):
        self.loop_counter += 1
        
        if len(self.population) == 0:
            self.creation()

        self.selection()
        self.mutation()
        self.reproduction()
        self.remove_nones()
        # print("-"*10)


if __name__ == '__main__':
    # TODO: Numbers are not between 0-1, instead 0-255
    from matplotlib import pyplot as plt

    # The brighter the avg the more score
    def evaluation_function(person):
        return 100*person.get_avg()

    pop = Population(ID_START, POP_SIZE, PERSON_SIZE, evaluation_function)

    # Crossing test
    """
    a, b = Person(0, PERSON_SIZE), Person(1, PERSON_SIZE)
    a.data = [[0 for i in range(100)] for i in range(100)]
    b.data = [[255 for i in range(100)] for i in range(100)]
    #Image.fromarray(np.array(b.data)).show()
    Image.fromarray(np.array(pop._crossing(a, b).data)).convert('RGB').show()
    exit(0)
    """

    for i in tqdm(range(EPOCH)):
        pop.evolve()

    # Visualization
    x = range(pop.loop_counter)
    plt.title('Improvement with Epoch {}'.format(EPOCH))
    plt.plot(x, [p.get_avg() for p in pop.history['best_person']], c="g")
    plt.plot(x, [p.get_avg() for p in pop.history['worst_person']], c="r")
    #plt.plot(x, pop.history['population_size'], c='r')
    plt.legend(['best_person', 'worst_person', 'pop_size'])
    plt.xlabel('time')
    plt.ylabel('score')
    plt.show()

    img = Image.fromarray(np.array(pop.history['best_person'][0].data))
    img.convert("L").save('paintings/first_best.jpg', 'JPEG')

    img = Image.fromarray(np.array(pop.history['best_person'][-1].data))
    #img.convert("L").save('paintings/best.jpg', 'JPEG')
    img.convert("L").save('images/readme/ep{}-best.jpg'.format(EPOCH), 'JPEG')
    #img.show("best")

    img = Image.fromarray(np.array(pop.history['worst_person'][0].data))
    #img.convert("L").save('paintings/worst.jpg', 'JPEG')
    img.convert("L").save('images/readme/ep{}-worst.jpg'.format(EPOCH), 'JPEG')
    #img.show("worst")

    """
    pop.creation()
    pop.remove_person(0)
    print(str(pop.population[0]))
    print(len(pop.population))
    """
