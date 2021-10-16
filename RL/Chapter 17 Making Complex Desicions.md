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
**Bellman Equation**: 
![image](https://user-images.githubusercontent.com/88390140/136814713-21a0509c-143f-4593-a600-84042141e8ce.png)
![image](https://user-images.githubusercontent.com/88390140/136814806-48409a8b-d5c9-462b-ae64-91f21dc01940.png)
- If there are n possible states, then there are n Bellman equations, one for each state. 
- There is one problem: the equations are nonlinear, because the “max” operator is not a linear operator. 
- Whereas systems of linear equations can be solved quickly using linear algebra techniques, systems of nonlinear equations are more problematic. One thing to try is an iterative approach. 
- We repeat this until we reach an equilibrium. Let Ui(s) be the utility value for state s at the ith iteration. The iteration step, called a **Bellman update**, looks like this:
![image](https://user-images.githubusercontent.com/88390140/136816884-8fe1926a-8c67-4b39-8973-17aa37de7edb.png)


![image](https://user-images.githubusercontent.com/88390140/136816362-98fa1e3e-8328-4a92-9284-e1ced9ad2da2.png)
![image](https://user-images.githubusercontent.com/88390140/136816559-e6f43359-ac3c-4387-8091-85123f21516f.png)
- We can think of the value iteration algorithm as propagating information through the state space by means of local updates. 

## Why Value Iteration Convergence? 
![image](https://user-images.githubusercontent.com/88390140/137592415-7b16fb9c-4006-429e-ad1d-63bfe7ab4b77.png)
![image](https://user-images.githubusercontent.com/88390140/137592526-842d8cb8-6af5-4246-a6d8-f04fc23bd10d.png)
![image](https://user-images.githubusercontent.com/88390140/137592529-edbdb29c-1534-4aef-ab91-741b6ab0f56b.png)                           
![image](https://user-images.githubusercontent.com/88390140/137592535-a7c3ca7b-4fb3-4160-b493-a43673c2e3fb.png)  (since Contraction Mapping)              
![image](https://user-images.githubusercontent.com/88390140/137592565-667b12cc-1754-4313-b434-f6a9b2193c5e.png)


## We can use Lagrange Mean Value to proof Contraction Mapping: 
![image](https://user-images.githubusercontent.com/88390140/137593362-e57d3abe-c276-4671-93cd-6d81873f1748.png)                   
![image](https://user-images.githubusercontent.com/88390140/137593370-facfacc9-7919-4281-8211-f95d506c29bc.png)





















