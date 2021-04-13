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


def Probability_accept(node, idea):
    agent = node['agent']
    best_utility = max([Individual_utility(node['agent'], i) for i in agent.idea_pool])
    mid_utility = median([Individual_utility(node['agent'], i) for i in agent.idea_pool])
    if Individual_utility(node['agent'], idea) > best_utility:
        return 1.
    elif Individual_utility(node['agent'], idea) < mid_utility:
        return 0.
    else:
        if mid_utility == best_utility:
            return 1.
        else:
            return (Individual_utility(node['agent'], idea)-mid_utility)/(best_utility-mid_utility)


def Visible_ideas(node):  # personal ideas are not included
    local_ideas = []
    # get the index of the node
    index = 0
    for i in range(len(net.nodes)):
        if node == net.nodes[i]:
            index = i
    for nb in list(net.neighbors(index)):  # neighbors' idea_pool
        local_ideas = local_ideas + net.nodes[nb]['agent'].idea_pool

    local_iter = [i['iteration'] + 10**-10 for i in local_ideas]
    local_comment = [len(i['comment']) + 10**-10 for i in local_ideas]
    local_like = [len(i['like']) + 10**-10 for i in local_ideas]

    p_iter = [(i-min(local_iter))/max(local_iter) for i in local_iter]
    p_comment = [(i-min(local_comment))/max(local_comment) for i in local_comment]
    p_like = [(i-min(local_like))/max(local_like) for i in local_like]
    p = [p_iter[i]+coef_com_like*p_comment[i]+coef_com_like*p_like[i] for i in range(len(p_iter))]
    if sum(p) == 0:
        norm_p = [1./len(p)]*len(p)
    else:
        norm_p = [i/sum(p) for i in p]

    if len(local_ideas) <= number_visible_idea:
        return local_ideas
    else:
        return list(choice(local_ideas, number_visible_idea, p=norm_p))



def Like(node, idea):  # need to be testified
    if node in idea['like']:
        return
    elif random() <= Probability_accept(node, idea):
        idea['like'].append(node)
        print("like")
    else:
        return


def Comment(node, idea): # comment here represents the suggestions; complement comments are assumed to be equal to clicking like
    agent = node['agent']
    pure_idea = idea['idea']
    personal_pure_ideas = [i['idea'] for i in agent.idea_pool]

    if node in idea['comment']:
        return
    elif random() <= Probability_accept(node, idea):
        if pure_idea in personal_pure_ideas:  # if the agent has the same idea
            idea['comment'].append(node)
        else:
            new_idea = pure_idea[:]
            background = agent.background
            size_background = sum([len(i) for i in background])
            selected_dim = choice(list(arange(dim)), p=[(len(i)+10**-10)/size_background for i in background])
            random_item = choice(background[selected_dim])
            new_idea[selected_dim] = random_item
            new_idea_dic = {'idea': new_idea}
            if Individual_utility(agent, new_idea_dic) > Individual_utility(agent, idea):  # if the new idea is better than previous one
                idea['comment'].append(node)
            print("comment")
    else:
        return


def Post_novel_idea(node, iteration):
    agent = node['agent']
    background = agent.background
    potential_new_ideas = []
    for i in range(number_new_ideas):
        tem_new_idea = []
        for di in range(dim):  # choose item randomly
            tem_new_idea.append(choice(background[di]))
        potential_new_ideas.append({'idea': tem_new_idea})

    selected_idea = potential_new_ideas[0]
    for i in potential_new_ideas:
        if Individual_utility(agent, i) > Individual_utility(agent, selected_idea):
            selected_idea = i
    new_idea = {'idea': selected_idea['idea'], 'comment': [], 'like': [], 'iteration': iteration}

    personal_idea_pool = node['agent'].idea_pool
    pure_personal_idea = [i['idea'] for i in personal_idea_pool]
    pure_visible_idea = [i['idea'] for i in visible_ideas]

    if (new_idea['idea'] not in pure_personal_idea) and (new_idea['idea'] not in pure_visible_idea)\
            and (random() <= Probability_accept(node, new_idea)):
        node['agent'].idea_pool.append(new_idea)
        print("new")
    else:
        return

