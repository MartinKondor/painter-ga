import numpy as np
from PIL import Image
from tqdm import tqdm
from src.population import Population
from matplotlib import pyplot as plt


EPOCH = 64  # Number of trainings
ID_START = 0
POP_SIZE = 100  # Number of starting images
PERSON_SIZE = (10, 10,)  # Size of images


# The biggest the avg the more score 
# In other words, the brighter the image
# the more score
def evaluation_function(person):
    return person.get_avg()


np.random.seed(2)
pop = Population(ID_START, POP_SIZE, PERSON_SIZE, evaluation_function)
for i in tqdm(range(EPOCH)):
    pop.evolve()

# Visualization
x = range(pop.loop_counter)
plt.title('Improvement with Epoch {}'.format(EPOCH))
plt.plot(x, [p.get_avg() for p in pop.history['best_person']], c="g")
plt.plot(x, [p.get_avg() for p in pop.history['worst_person']], c="r")
# plt.plot(x, pop.history['population_size'], c='r')
plt.legend(['best_person', 'worst_person'])
plt.xlabel('time')
plt.ylabel('score')
plt.show()
#plt.savefig('images/readme/ep{}.png'.format(EPOCH))

img = Image.fromarray(np.array(pop.history['best_person'][-1].data))
#img.convert("L").save('paintings/best.jpg', 'JPEG')
#img.convert("L").save('images/readme/ep{}-best.jpg'.format(EPOCH), 'JPEG')
img.show("best")

img = Image.fromarray(np.array(pop.history['worst_person'][0].data))
#img.convert("L").save('paintings/worst.jpg', 'JPEG')
#img.convert("L").save('images/readme/ep{}-worst.jpg'.format(EPOCH), 'JPEG')
img.show("worst")
