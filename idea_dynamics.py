from pylab import *
import networkx as nx
import pandas as pd
import itertools as itr
from scipy import spatial
from collections import Counter
import operator
from collections import OrderedDict


dim = 4  # dim: dimensions of problem space
group_size = 20
number_items = 10
n = 3  # number of ideas in final selection
MC = 100  # number of Monte Carlo experiments
mont_iter = 20  # number of Monte Carlo experiments for each group

coef_unknown = 0.2
coef_com_like = 1.
number_new_ideas = 4  # number of potential new ideas in function of post a novel idea
number_initial_idea = 50
noise = 0.1
number_personal_idea = 1
number_visible_idea = 20  # number of visible ideas in each iteration
number_groups = 1


########################################################################################################################
# functions
########################################################################################################################
items = list(arange(number_items))
initial_n_idea = [[choice(items) for i in range(dim)] for j in range(number_initial_idea)]
TU = {tuple(c): random() for c in initial_n_idea}
i_1, i_0 = choice(arange(number_initial_idea), 2, replace=False)
TU[tuple(initial_n_idea[i_1])] = 1.
TU[tuple(initial_n_idea[i_0])] = 0.

def True_utility(idea): # given n initial ideas
    pure_idea = tuple(idea['idea'])
    initial_idea = list(TU.keys())
    initial_idea_value = list(TU.values())
    if pure_idea in initial_idea:
        return TU[pure_idea]
    else:
        dist = []
        for i in range(len(initial_idea)): # n is the number of initial ideas
            dist.append(sqrt(sum([(float(initial_idea[i][d]) - float(pure_idea[d]))**2 for d in range(dim)])))
        return sum([initial_idea_value[i]*(dist[i]**(-2)) for i in range(len(dist))])/sum([dist[i]**(-2) for i in range(len(dist))])


def Background(expertise):
    Background = []
    for i in range(dim):
        if i in expertise:
            Background.append(list(choice(items, int(uniform(int(number_items/2.)+2, number_items)), replace=False)))
        else:
            Background.append(list(choice(items, int(uniform(1, int(number_items/2.)-2)), replace=False)))
    return Background


def Diff_background(agent1, agent2):
    Background1 = agent1.background
    Background2 = agent2.background
    overlap = 0
    for i in range(dim):
        for j in Background1[i]:
            if j in Background2[i]:
                overlap += 1
    whole_items1 = sum([len(Background1[i]) for i in range(dim)])
    whole_items2 = sum([len(Background2[i]) for i in range(dim)])
    return 1-overlap/(whole_items1 + whole_items2 - overlap)


def Individual_utility(agent, idea):
    background = agent.background
    pure_idea = idea['idea']
    r = 0
    for i in range(dim):
        if pure_idea[i] in background[i]:
            r += 1
    return r*clip(True_utility(idea)+uniform(-noise, noise), 0, 1) + coef_unknown*(1-r)*uniform(0, 1.)


def Best_idea(agent):
    personal_idea_pool = agent.idea_pool
    if len(personal_idea_pool) == 0:
        return None
    else:
        max_idea = max(personal_idea_pool, key=lambda i: Individual_utility(agent, i))
    return max_idea


def Variance_ideas(idea_list):
    dist = []
    for i in idea_list:
        for j in idea_list:
            if i != j:
                dist.append(sqrt(sum([(float(i[d])-float(j[d]))**2 for d in range(dim)])))
    return var(dist)
