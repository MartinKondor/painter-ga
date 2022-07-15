import random
from src.person import Person


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
        self.debug = False

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
        if self.debug:
            print("<{}. creation>".format(self.loop_counter))
        
        for i in range(self.population_size - len(self.population)):
            p = Person(self.get_new_id(), self.person_size)
            self.population.append(p)

    """
    Evaluate each person
    """
    def selection(self):
        if self.debug:
            print("<{}. selection>".format(self.loop_counter))
        
        for person in self.population:
            person.score = self.evaluation_function(person)

        # Remove 20%-of the population
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
        if self.debug:
            print("<{}. mutation>".format(self.loop_counter))

        mutation_count = int((0.27) * len(self.population))
        for _ in range(mutation_count):
            person = random.choice(self.population)
            
            # Change n pixel
            n = 1 + int(random.random() * (person.x / 2) - 1)
            choosen_pixels = []

            for _ in range(n):
                x, y = person.x, person.y
                x = int(random.random() * x - 1)
                y = int(random.random() * y - 1)
                
                if [x, y] in choosen_pixels:
                    x = int(random.random() * x - 1)
                    y = int(random.random() * y - 1)

                person[x][y] = 255*random.random() - 1
                choosen_pixels.append([x, y])

    def _crossing(self, person_a, person_b):
        xs, ys = person_a.x, person_a.y
        child = Person(self.get_new_id(), self.person_size)
        choosen_for_a = []
        choosen_for_b = []

        for i in range(int(xs*ys/2)):
            xi, yi = int(random.random()*xs), int(random.random()*ys)
            while [xi, yi] in choosen_for_a:
                xi, yi = int(random.random()*xs), int(random.random()*ys)
            choosen_for_a.append([xi, yi])

        # Choose the ones not choosen for person_a
        for x in range(xs):
            for y in range(ys):
                if [x, y] not in choosen_for_a:
                    choosen_for_b.append([x, y])

        for index_a, index_b in zip(choosen_for_a, choosen_for_b):
            child[index_a[0]][index_a[1]] = person_a[index_a[0]][index_a[1]]
            child[index_b[0]][index_b[1]] = person_b[index_b[0]][index_b[1]]

        return child

    """
    Choose a person who is not excluded.

    :exclude: list of Person id's
    """
    def _choice_score(self, exclude):
        i = 0
        choosen_person = self.population[i]

        while choosen_person.id in exclude:
            i += 1
            choosen_person = self.population[i]

        return choosen_person

    """
    Cross the best persons with each other
    """
    def reproduction(self):
        if self.debug:
            print("<{}. reproduction (pop_size: {})>".format(self.loop_counter, len(self.population)))
        
        self.population = sorted(self.population, key=lambda x: x.score, reverse=True)
        cross_count = int(self.population_size - len(self.population))
        exclude = []

        for i in range(cross_count):
        
            person_a = self._choice_score(exclude)
            exclude.append(person_a.id)
            person_b = self._choice_score(exclude)
            exclude.append(person_b.id)
            
            new_person = self._crossing(person_a, person_b)
            self.population.append(new_person)

        #print("[{}.] Population size:".format(self.loop_counter), len(self.population))
        self.history['population_size'].append(len(self.population))

    """
    Execute one step of evolution
    """
    def evolve(self, debug=False):
        self.debug = debug
        self.loop_counter += 1
        
        if len(self.population) == 0:
            self.creation()

        self.selection()  # about 0.0015411376953125s
        self.mutation()  # about 5.1975250244140625e-05s    
        self.reproduction()  # about 0.005439043045043945s (0.004846096038818359s)
        # print("-"*10)
