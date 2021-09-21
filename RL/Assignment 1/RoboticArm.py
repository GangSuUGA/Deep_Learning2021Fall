# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:06:57 2021

@author: gs70055
"""

from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import random
import time
import gym

class RoboticArm(Env):  
    def __init__(self):
        
        self.d1 = 1
        self.d2 = 1.5
        self.xb = 2.176
        self.yb = .129
        self.xh = 2.266
        self.yh = .643
        self.theta1_bolt = 40
        self.theta2_bolt = -60
        self.theta1_hole = 40
        self.theta2_hole = -40 
        
        self.viewer = None
        # Actions we can take, down, stay, up
        self.action_space = Discrete(8)
        # Temperature array
        self.observation_space = Box(low=np.array([0,-60,0,0]), high=np.array([60,60,1,1]))
        # Set start temp
        self.state = np.array([40,0,0,0], dtype=np.float32)
        self.done = False
    
    def step(self, action):
        s = self.state
        # Apply action
        if action <= 3: 
            grip = 0
        else:
            grip = 1
            action = action - 4
        
        if int(action/2) == 0:
            theta1 = -20
        elif int(action/2) == 1:
            theta1 = +20
            
        if action%2 == 0: 
            theta2 = -20
        elif action%2 == 1: 
            theta2 = +20
        
        self.state[0] = self.state[0] + theta1
        self.state[1] = self.state[1] + theta2 
        
        if s[0] < 0:
            s[0] = 0
            theta1 = 0
        if s[0] > 60:
            s[0] = 60
            theta1 = 0
        if s[1] < -60:
            s[1] = -60
            theta2 = 0
        if s[1] > 60:
            s[1] = 60
            theta2 = 0
        
        xg = np.round((self.d1 * np.cos(s[0]*np.pi/180) + self.d2 * np.cos((s[0]+s[1])*np.pi/180)),3)
        yg = np.round((self.d1 * np.sin(s[0]*np.pi/180) + self.d2 * np.sin((s[0]+s[1])*np.pi/180)),3)
        
        self.done = False
        
        if xg >= self.xh and yg != self.yh:
            reward = -100
        elif s[0] == self.theta1_hole and s[1] == self.theta2_hole and s[2] == 1 and grip == 0:
            reward = +10
            self.done = True
        else: 
            reward = -1

        if grip == 0: 
            s[2] = 0
        
        if s[0] == self.theta1_bolt and s[1] == self.theta2_bolt and grip == 1:
            s[2] = 1 
        
        s[3] = grip
        
        #print("state:",self.state,"reward:",reward)
        
        # Set placeholder for info
        info = {}
        
        # Return step information
        done = self.done
        return self.state, reward, done, info
    
    
    def render(self, mode="human"):
        from gym.envs.classic_control import rendering

        s = self.state

        if self.viewer is None:
            self.viewer = rendering.Viewer(500, 500)
            bound = self.d1 + self.d2 + 0.2  # 2.2 for default
            self.viewer.set_bounds(-1.5, 1.5*bound, -1.5, 1.5*bound)

        if s is None:
            return None
        
        xg = np.round((self.d1 * np.cos(s[0]*np.pi/180) + self.d2 * np.cos((s[0]+s[1])*np.pi/180)),3)
        yg = np.round((self.d1 * np.sin(s[0]*np.pi/180) + self.d2 * np.sin((s[0]+s[1])*np.pi/180)),3)
        
        p1 = [np.round((self.d1 * np.cos(s[0]*np.pi/180)),3), np.round((self.d1 * np.sin(s[0]*np.pi/180)),3)]

        p2 = [xg, yg]
      
        self.viewer.draw_line((2.266, 0), (2.266, 0.62))
        self.viewer.draw_line((2.266, 0.68), (2.266, 2))
        self.viewer.draw_line((0, 0), (1, 0))
        self.viewer.draw_line((0, 0), (0, 1))
        
        ### Draw Link and Circle 
        l, r, t, b = 0, 1, 0.05, -0.05
        jtransform = rendering.Transform(rotation= s[0]*np.pi/180, translation=(0, 0))
        link = self.viewer.draw_polygon([(l, b), (l, t), (r, t), (r, b)])
        link.add_attr(jtransform)
        link.set_color(0, 0.8, 0.8)
                
        circ = self.viewer.draw_circle(0.06)
        circ.set_color(0.8, 0.8, 0)
        circ.add_attr(jtransform)
        
        l, r, t, b = 0, 1.5, 0.05, -0.05
        jtransform = rendering.Transform(rotation= (s[0]+s[1])*np.pi/180, translation=(p1[0], p1[1]))
        link = self.viewer.draw_polygon([(l, b), (l, t), (r, t), (r, b)])
        link.add_attr(jtransform)
        link.set_color(0, 0.8, 0.8)
        
        circ = self.viewer.draw_circle(0.06)
        circ.set_color(0.8, 0.8, 0)
        circ.add_attr(jtransform)
        
        if s[2] == 0.0 and self.done == False:
            ### Bolt in Originial Location
            jtransform = rendering.Transform(rotation= 0, translation=(2.176, 0.13))
            circ = self.viewer.draw_circle(0.10)
            circ.set_color(0.8, 0, 0.8) 
            circ.add_attr(jtransform)

            jtransform = rendering.Transform(rotation= 0, translation=(p2[0], p2[1]))
            circ = self.viewer.draw_circle(0.06)
            circ.set_color(0.8, 0.8, 0)
            circ.add_attr(jtransform)
        if s[2] == 1.0:
            ### Bolt in Gripper
            jt = rendering.Transform(rotation= 0, translation=(p2[0]+0.1*np.cos((s[0]+s[1])*np.pi/180), p2[1]+0.1*np.sin((s[0]+s[1])*np.pi/180)))
            circ = self.viewer.draw_circle(0.10)
            circ.set_color(0.8, 0, 0.8)
            circ.add_attr(jt)
        if self.done == True:
            ### Bolt in Hole Location
            jtr = rendering.Transform(rotation= 0, translation=(2.266, 0.643))
            circ = self.viewer.draw_circle(0.10)
            circ.set_color(0.8, 0, 0.8) 
            circ.add_attr(jtr)
        
       ### Draw Gripper
        gripperwidth = 0.3
        gripperheight = 0.05
        angle = (s[0]+s[1])
        l, r, t, b = -gripperwidth / 2, gripperwidth / 2, gripperheight / 2, -gripperheight / 2
        gripper = self.viewer.draw_polygon([(l, b), (l, t), (r, t), (r, b)])
        jtransform = rendering.Transform(rotation= (angle+90)*np.pi/180, translation=(p2[0], p2[1]))
        gripper.add_attr(jtransform)

        if s[3] == 0:
            ### Draw Open Gripper
            gripper = self.viewer.draw_polygon([(l/1.2, b/3), (l/1.2, t/3), (r/1.2, t/3), (r/1.2, b/3)])
            jtransform = rendering.Transform(rotation= angle*np.pi/180, translation=(p2[0]+0.4*gripperwidth*np.sin(angle*np.pi/180)+0.3*gripperwidth*np.cos(angle*np.pi/180), p2[1]-0.4*gripperwidth*np.cos(angle*np.pi/180)+0.3*gripperwidth*np.sin(angle*np.pi/180)))
            gripper.add_attr(jtransform)
            gripper = self.viewer.draw_polygon([(l/1.2, b/3), (l/1.2, t/3), (r/1.2, t/3), (r/1.2, b/3)])
            jtransform = rendering.Transform(rotation= angle*np.pi/180, translation=(p2[0]-0.4*gripperwidth*np.sin(angle*np.pi/180)+0.3*gripperwidth*np.cos(angle*np.pi/180), p2[1]+0.4*gripperwidth*np.cos(angle*np.pi/180)+0.3*gripperwidth*np.sin(angle*np.pi/180)))
            gripper.add_attr(jtransform)
        else:
            ### Draw Close Gripper
            gripper = self.viewer.draw_polygon([(l/1.2, b/3), (l/1.2, t/3), (r/1.2, t/3), (r/1.2, b/3)])
            jtransform = rendering.Transform(rotation= (angle+30)*np.pi/180, translation=(p2[0]+0.3*gripperwidth*np.sin(angle*np.pi/180)+0.3*gripperwidth*np.cos(angle*np.pi/180), p2[1]-0.3*gripperwidth*np.cos(angle*np.pi/180)+0.3*gripperwidth*np.sin(angle*np.pi/180)))
            gripper.add_attr(jtransform)
            gripper = self.viewer.draw_polygon([(l/1.2, b/3), (l/1.2, t/3), (r/1.2, t/3), (r/1.2, b/3)])
            jtransform = rendering.Transform(rotation= (angle-30)*np.pi/180, translation=(p2[0]-0.3*gripperwidth*np.sin(angle*np.pi/180)+0.3*gripperwidth*np.cos(angle*np.pi/180), p2[1]+0.3*gripperwidth*np.cos(angle*np.pi/180)+0.3*gripperwidth*np.sin(angle*np.pi/180)))
            gripper.add_attr(jtransform)
            
        
        return self.viewer.render(return_rgb_array=mode == "rgb_array")
    
    def reset(self):
        self.state = np.array([40,0,0,0], dtype=np.float32)
        #self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
        #self.steps_beyond_done = None                #############################
        return self.state
       
    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None