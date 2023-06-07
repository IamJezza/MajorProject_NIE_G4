import random
import time


def GA_select_elites(fitness_and_population: list, top: int):
    temp = fitness_and_population[:]
    temp.sort()
    return temp[:top]


def GA_select_roulette_wheel(population: list, pop_fitness: list, size: int, isRepetitionAllowed= False):
    """
    :param population: GA population list
    :param pop_fitness: population fitness list
    :param size: the size of the selection
    :param isRepetitionAllowed: Is the repetition in new population allowed?
    :return: the new selected population.
    """
    result = []
    start_time = time.time()

    if isRepetitionAllowed:
        while len(result) < size:
            result.append(random.choices(population, pop_fitness))

        return result

    if len(population) < size:
        raise Exception("current population size is small")

    while len(result) < size:
        new_mem = random.choices(population, pop_fitness)
        if new_mem not in result:
            result.append(random.choices(population, pop_fitness)[0])
        if time.time() - start_time > 10:
            raise TimeoutError("Unable to produce the selected population")
    return result


