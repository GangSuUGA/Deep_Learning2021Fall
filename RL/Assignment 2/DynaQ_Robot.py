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
        self.Q_values = {}
        self.Model = {}
        for theta1 in range(0,80,20):
            for theta2 in range(-60,80,20):
                for bolt in range(dim_states[2]):
                    for gripper in range(dim_states[3]):
                        self.Q_values[(theta1,theta2,bolt,gripper)] = {}
                        for a in range(num_actions):
                            self.Q_values[(theta1,theta2,bolt,gripper)][a] = random.random() 
        
    def Q_learn(self, old_state, action, reward, state):
        TD = reward + self.dr * max(self.Q_values[tuple(state)].items())[1] - self.Q_values[tuple(old_state)][action]
        self.Q_values[tuple(old_state)][action] += self.lr * TD 
        
    def Model_learn(self, old_state, action, reward, state): 
        if tuple(old_state) not in self.Model.keys():
            self.Model[tuple(old_state)] = {}
        self.Model[tuple(old_state)][action] = (reward, state) 

    def Planning(self, n): 
        for i in range(n-1):
            # randomly choose an state
            rand_idx = np.random.choice(range(len(self.Model.keys())))
            _old_state = list(self.Model)[rand_idx]
            # randomly choose an action
            rand_idx = np.random.choice(range(len(self.Model[tuple(_old_state)].keys())))
            _action = list(self.Model[tuple(_old_state)])[rand_idx]

            _reward, _state = self.Model[tuple(_old_state)][_action] 
            self.Q_learn(_old_state, _action, _reward, _state)

episodes = 100
model = DynaQ(dim_states=([4,7,2,2]), num_actions=env.action_space.n)
#epsilon = 0.1
n = 10

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
        
        # Q-Learning: 
        model.Q_learn(old_state, action, reward, state)
        # Model-Learning: 
        model.Model_learn(old_state, action, reward, state) 
        # Model-Planning: 
        model.Planning(n)
        
        if score < -500000:
            break

    env.close()
    print('Episode:{} Score:{}'.format(episode, score))