# -*- coding: utf-8 -*-
"""
Created on Tue Oct 9 16:08:52 2021

@author: gs70055
"""
import gym
from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
import time
import torch
from torch import nn 
import torch.optim as optim
import pandas as pd
from RoboticArm import RoboticArm


env = RoboticArm()

def choose_action(state, model, epsilon):
    """
    Decide wheter to perform an explorative or exploitative action, according to an epsilon-greedy policy
    """
    if random.random() < epsilon:
        return env.action_space.sample() # random action
    else:
        return max(model.Q_values[tuple(state)]) # the best action given the current state
    
class DynaQ():
    def __init__(self, dim_states, num_actions, lr=0.1, dr=0.9):
        self.dr = dr 
        self.lr = lr
        self.num_a = num_actions
        self.Q_values = {}
        self.Model = {}
        self.PQ = []
        for theta1 in range(0,80,20):
            for theta2 in range(-60,80,20):
                for bolt in range(dim_states[2]):
                    for gripper in range(dim_states[3]):
                        self.Q_values[(theta1,theta2,bolt,gripper)] = {}
                        for a in range(self.num_a):
                            self.Q_values[(theta1,theta2,bolt,gripper)][a] = random.random() 
        
    def TD(self, old_state, action, reward, state):
        TD = reward + self.dr * max(self.Q_values[tuple(state)].items())[1] - self.Q_values[tuple(old_state)][action]
        #self.Q_values[tuple(old_state)][action] += self.lr * TD 
        return abs(TD) 
    
    def Q_learn(self, old_state, action, reward, state):
        TD = reward + self.dr * max(self.Q_values[tuple(state)].items())[1] - self.Q_values[tuple(old_state)][action]
        self.Q_values[tuple(old_state)][action] += self.lr * TD 
        
    def Model_learn(self, old_state, action, reward, state): 
        if tuple(old_state) not in self.Model.keys():
            self.Model[tuple(old_state)] = {}
        self.Model[tuple(old_state)][action] = (reward, state) 

    def Planning(self, n): 
        if self.PQ: 
            for i in range(n):
                _old_state = self.PQ[0][1][0] 
                _action = self.PQ[0][1][1] 
                del self.PQ[0]
                _reward, _state = self.Model[tuple(_old_state)][_action] 
                self.Q_learn(_old_state, _action, _reward, _state)
                for _action in range(self.num_a):
                    if _action in model.Model[tuple(old_state)].keys(): 
                        _reward, _state = self.Model[tuple(_old_state)][_action] 
                        TD = self.TD(_old_state, _action, _reward, _state)
                        self.Add(TD, _old_state, _action, _reward, _state, theta=0.0001)
                        
    def Add(self, TD, old_state, action, reward, state,theta): 
        if TD > theta: 
            if len(self.PQ) > 0:
                for i in range(len(self.PQ)): 

                    if (old_state, action, reward, state) == self.PQ[i][1]: 
                        self.PQ[i][0] = TD 
                    else: 
                        self.PQ += tuple([[TD, (old_state, action, reward, state)]]) 
                        self.PQ.sort(reverse=True) 
            else: 
                self.PQ += tuple([[TD, (old_state, action, reward, state)]]) 

        

episodes = 50
model = DynaQ(dim_states=([4,7,2,2]), num_actions=env.action_space.n)
#epsilon = 0.1
n = 10
theta = 0.1

for episode in range(1, episodes+1):
    epsilon = max(0,(1.0 - (episode / episodes)))
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        env.render()
        #time.sleep(.05)
        action = choose_action(state,model,epsilon)
        old_state = state 
        state, reward, done, info = env.step(action)
        score+=reward
        
        # Model-Learning: 
        model.Model_learn(old_state, action, reward, state) 
        
        # Priority Insert: 
        TD = model.TD(old_state, action, reward, state) 
        model.Add(TD, old_state, action, reward, state,theta)
        
        # Model-Planning: 
        model.Planning(n)

    env.close()
    print('Episode:{} Score:{}'.format(episode, score))
    #df = pd.DataFrame(model.Q_values)
    #print(df.T)