import random
import numpy as np

def createPopulation(populationSize, individualSize):
    # Arreglo con todos ceros
    population = np.zeros((populationSize, individualSize))
    # Para cada individuo
    for i in range(populationSize):
        # Número random de unos a crear
        ones = random.randint(0, individualSize)
        population[i, 0:ones] = 1
        # Shuffle
        np.random.shuffle(population[i])

    return population


def calcFitness(population):
    # Separar arreglo

    # Hacer función para evaluar

    return fitness


def selection(population, fitness):
    # Tamaño de la población
    populationSize = len(fitness)

    # Elegir individuos
    indiv1 = random.randint(0, populationSize - 1)
    indiv2 = random.randint(0, populationSize - 1)

    # Obtener fitness
    indiv1_fitness = fitness[indiv1]
    indiv2_fitness = fitness[indiv2]

    # Identificar individuo con mayor fitness
    if indiv1_fitness >= indiv2_fitness:
        selected = indiv1
    else:
        selected = indiv2

    # Regresar seleccionado
    return population[selected, :]


def crossover(indiv1, indiv2):
    # Obtener tamaño del inviduo
    individualSize = len(indiv1)

    # Escoger punto de cruza
    crossoverPoint = random.randint(1, individualSize - 1)

    # Crear hijos
    # np.hstack para juntar los arreglos
    offspring1 = np.append((indiv1[0:crossoverPoint], indiv2[crossoverPoint:]))

    offspring2 = np.append((indiv2[0:crossoverPoint], indiv1[crossoverPoint:]))

    # Regresar hijos
    return offspring1, offspring2


def mutate(population, probability):
    # Aplicar mutación random
    mutationArray = np.random.random(size=(population.shape))

    mutationBoolean = \
        mutationArray <= probability

    population[mutationBoolean] = \
        np.logical_not(population[mutationBoolean])

    # Regresar población mutada
    return population


# MAIN
# Variables generales
individualSize = 12
populationSize = 5
maxGeneration = 2

# Crea población inical
population = createPopulation(populationSize, individualSize)

# Calcular fitness
fitness = calcFitness(population)

# Generaciones
for generation in range(maxGeneration):
    # Crear nueva población
    newPopulation = []

    # Crear nueva población generando 2 hijos a la vez
    for i in range(int(populationSize / 2)):
        parent1 = selection(population, fitness)
        parent2 = selection(population, fitness)
        offspring1, offspring2 = crossover(parent1, parent2)
        newPopulation.append(offspring1)
        newPopulation.append(offspring2)

    # Reemplazar vieja población con la nueva
    population = np.array(newPopulation)

    fitness = calcFitness(population)

# Fin :3
print(fitness)