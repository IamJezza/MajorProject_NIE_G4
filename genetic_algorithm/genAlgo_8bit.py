import pandas as pd
import numpy as np
import random
import time
import GA_pop_select


code_start_time = time.time()
# set random seed
random.seed(0)


def gen_weighted_8bit_val(weights):
    """
    :param weights: percent probability of each bit
    :return: a weighted eight bit integer
    """
    s = ''
    for i in range(8):
        s += random.choices(['1', '0'], [weights[i], 255-weights[i]])[0]
    return int(s, 2)


def gen_weights(Bit_len):
    """
    To generate the initial weights
    :return: list of weights for each bit.
    """
    l = []
    for _ in range(Bit_len):
        l.append(random.randint(0, 255))
    return l


def gen_initial_pop(weights, pop_len):
    """
    To generate a fixed size population
    :param weights: weights based on which the population is generated
    :param pop_len: size of the population.
    :return: list of fixed size int values
    """
    pop = []
    start_time = time.time()
    while len(pop) < pop_len:
        val = gen_weighted_8bit_val(weights)
        if val not in pop:
            pop.append(val)
        if time.time()-start_time>10:
            raise TimeoutError
    return pop


def mutation(val, mut_percent):
    """
    :param val: the number that has to be mutated
    :param mut_percent: probability of mutation
    :return: mutated value
    """
    val = bin(val)
    val = val[2:].zfill(8)
    new_val = ''
    for i in range(len(val)):
        ran_val = random.random()*100
        if mut_percent > ran_val:
            if val[i] == '0':
                new_val += '1'
            else:
                new_val += '0'
        else:
            new_val += val[i]
    return int(new_val, 2)


def fitness(population, data):
    """
    :param population: whose fitness has to determined
    :return: fitness of the population
    indicated the fault coverage of the population
    """
    error_list = []
    for ele in population:
        my_list = np.array(data.iloc[ele]).nonzero()[0]
        error_list = list(set().union(error_list, my_list))
    return len(error_list)*100/len(data.columns)


def determine_weights(my_list):
    """
    :param my_list: a list of ints
    :return: the list of weight of each bit in my_list
    """
    weights = [0]*8
    for i in my_list:
        i = bin(int(i))
        for j in range(2, len(i)):
            weights[j-2] += int(i[j], 2)
    for i in range(len(weights)):
        weights[i] /= (len(my_list)/255)
        weights[i] = int(weights[i])
    return weights


population_size = 15  # set size of population
count = 0  # to count the generation
mu_rate = 5
weights = gen_weights(8)  # initial weights
data = pd.read_csv('USEFUL_DIFF_DATA.csv')
population = gen_initial_pop(weights, population_size)  # initial population
fit = fitness(population, data)
res_file = open('GA_8bits.txt', 'w')
res_file.write("%generation,\t populationLength,\t weights,\t mutationRate,\t fitness\n")
res_file.write(str(count)+",\t "+str(len(population))+",\t "+','.join(map(str, weights))+",\t "+str(mu_rate)+",\t "+str(fit)+"\n")

# print statements.
print("generation", count)
print("population", sorted(population))
print("with weights", weights)
print("population fitness", fit)

# while the fault coverage is less than 95%
while fit < 98.8:
    result = []
    for i in population:
        result.append(fitness([i], data))
    # sort based on fitness of each member of population
    best = GA_pop_select.GA_select_roulette_wheel(population, result, 11)
    '''
    result.sort()
    result.reverse()
    # select the top 10 / a number less that population size
    best = np.array(result[:10])
    '''
    # find the wights of the best
    new_weights = determine_weights(best)

    # generated a new population
    new_population = gen_initial_pop(new_weights, population_size)

    # add mutation to the population
    population = []
    for member in new_population:
        population.append(mutation(member, mu_rate))
    fit = fitness(population, data)
    count += 1  # increment generation
    # print statements.
    res_file.write(str(count) + ",\t " + str(len(population)) + ",\t " + ','.join(map(str, new_weights)) + ",\t " + str(mu_rate) + ",\t " + str(fit) + "\n")

    print("generation", count)
    print("population", sorted(population))
    print("with weights", new_weights)
    print("population fitness", fit)

# store the final result in a txt file
res_file.close()
file = open('Final_GA_8bits.txt', 'w')
file.write("%generation,\t populationLength,\t weights,\t mutationRate,\t fitness\n")
file.write(str(count)+",\t "+str(len(population))+",\t "+str(new_weights)+",\t "+str(5)+",\t "+str(fit)+"\n")
file.close()
print()
print('Hurray...')
print('successfully found the required weights')
print(new_weights)
code_stop_time = time.time()
hr = int((code_stop_time-code_start_time)/(60*60))
minutes = int((code_stop_time - code_start_time) / 60 - hr * 60)
sec = int((code_stop_time - code_start_time) - (minutes + hr*60)*60)
millisec = int((code_stop_time - code_start_time - (sec + (minutes + hr*60)*60))*10**3)
microsec = int(((code_stop_time - code_start_time - (sec + (minutes + hr*60)*60))*10**3-millisec)*10**3)
print('In a time of', hr, 'hrs|', minutes, 'mins|', sec, 'secs|', millisec, 'millisecond|', microsec, 'microsecond')

