# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:08:52 2021

@author: gs70055
"""
from RoboticArm import RoboticArm
import time

env = RoboticArm()

episodes = 3
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    score = 0 
    
    while not done:
        env.render()
        time.sleep(.05)
        action = env.action_space.sample()
        n_state, reward, done, info = env.step(action)
        score+=reward
    env.render()
    env.close()
    print('Episode:{} Score:{}'.format(episode, score))