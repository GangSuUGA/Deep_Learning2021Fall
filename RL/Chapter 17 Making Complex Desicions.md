## Book Link: 
- S. Russell, P. Norvig, [**Artificial Intelligence: A Modern Approach**](https://www.researchgate.net/publication/220546066_S_Russell_P_Norvig_Artificial_Intelligence_A_Modern_Approach_Third_Edition), Third Edition. 

_____________________________________

![image](https://user-images.githubusercontent.com/88390140/136808964-61e426a8-1737-4143-9b44-b492a910ac75.png)
![image](https://user-images.githubusercontent.com/88390140/136809009-92815e13-4330-4a06-9d57-b6cff22c4963.png)

- An optimal policy for the world of Figure 17.1 is shown in Figure 17.2(a). 


## The balance of risk and reward changes depending on the value of R(s) for the nonterminal states. 
![image](https://user-images.githubusercontent.com/88390140/136809400-0d4c42b3-7f3a-4b0d-a4a4-c3dd53e37d43.png)

- Figure 17.2(b) shows optimal policies for four different ranges of R(s). 
- When R(s) ≤ −1.6284, life is so painful that the agent heads straight for the nearest exit, even if the exit is worth –1. 
- When −0.4278 ≤ R(s) ≤ −0.0850, life is quite unpleasant; the agent takes the shortest route to the +1 state and is willing to risk falling into the –1 state by accident. In particular, the agent takes the shortcut from (3,1). 
- When life is only slightly dreary (−0.0221 < R(s) < 0), the optimal policy takes no risks at all. In (4,1) and (3,2), the agent heads directly away from the –1 state so that it cannot fall in by accident, even though this means banging its head against the wall quite a few times. 
- Finally, if R(s) > 0, then life is positively enjoyable and the agent avoids both exits. 

## Optimal Policy 
![image](https://user-images.githubusercontent.com/88390140/136814271-f2da11da-90dc-49fa-b298-0d03d5f6d469.png)
![image](https://user-images.githubusercontent.com/88390140/136814289-2bf40f43-c05e-4bb4-9869-34c30eaeaabc.png)
![image](https://user-images.githubusercontent.com/88390140/136814205-72bab105-66ac-44b4-afb2-9e2f54c7b7d9.png)

## Value Iteration 
- The basic idea is to calculate the utility of each state and then use the state utilities to select an optimal action in each state.
