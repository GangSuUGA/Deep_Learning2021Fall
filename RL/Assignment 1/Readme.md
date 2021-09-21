## Running the algorithm: 
1. Clone or download the repo.
2. Using the Anaconda prompt or any other terminal, navigate to the root folder and run the file Validate.py by executing: 

```
python Validate.py
```
 _________________________________
## Robotic manipulator engaged in a pick-and-place task.  

 - We will consider the setting where a manipulator with two revolute joints and a two-fingered gripper is tasked with picking a bolt and inserting it into a hole in a metal sheet. 

 ![image](https://user-images.githubusercontent.com/88390140/134245843-25476f5f-8d81-4c2a-9347-408065b37b60.png)

 - **From above computation, the location of bolt (2.176, 0.643) should correspond to (40, -60); the location of hole (2.266, 0.643) should correspond to (40, -40).** 


## State/Observation Space: 
 - There are 4 factors we will consider in the state definition, **[theta1, theta2, with/without bolt, gripper open/close]**. 

## Action Space: 
 - Range for theta1: [0, 20, 40, 60]; range for theta2: [-60, -40, -20, 0, 20, 40, 60].         
 - Action for theta1, theta2: [-20, 20];   
 - Action for gripper: [Open/0, Close/1];                    
 - There are 8 (2* 2* 2) discrete action the agent can choose.     

Action|theta1|theta2|Grip
----|----|----|----
0 |-20| -20| 0 
1 |-20| +20| 0 
2 |+20| -20| 0 
3 |+20| +20| 0 
4 |-20| -20| 1
5 |-20| +20| 1 
6 |+20| -20| 1 
7 |+20| +20| 1 

__________________________________

## Reference Link:
 - [**Python gym.envs.classic_control**](https://www.programcreek.com/python/index/8261/gym.envs.classic_control)
