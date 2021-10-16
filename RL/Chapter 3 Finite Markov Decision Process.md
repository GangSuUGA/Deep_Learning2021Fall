## Book Link: 
- Sutton, Richard S. and Andrew G. Barto. [**Reinforcement Learning: An Introduction.**](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf) :star: :star: :star: :star: :star:

__________________________________________________________________


# Finite Markov Decision Processes 

- **Definition**: MDPs are a classical formalization of sequential decision making, where actions influence not just **immediate reward**, but also subsequent situations, or states, and through those **future rewards**.  

![image](https://user-images.githubusercontent.com/88390140/137599344-f8c89775-c877-4e4f-b079-cd69dc986e93.png)

**Agent tries to learn a policy/decision for each states from interactions to acieve a goal.** 

- Trajectory:                
![image](https://user-images.githubusercontent.com/88390140/137599496-eb65d7aa-1362-439b-9f80-a35d56231967.png)

- The function p defines the dynamics of the MDP:                    
![image](https://user-images.githubusercontent.com/88390140/137599633-f1db795e-efcd-4e11-b164-2defd5fc8aff.png)                    
![image](https://user-images.githubusercontent.com/88390140/137599647-2da0a204-a584-4dc8-bb3f-5409f43d273e.png)

- **MDP Assumption**: p, the dynamic or the probability of each possible value for St and Rt depends only on the immediately preceding state and action, St1 and At1, not at all on earlier states and actions.  
- **MDP Property**: The state must include information about all aspects of the past interactive information. 

- **State Transition Probability**:                        
![image](https://user-images.githubusercontent.com/88390140/137599916-21a1769e-b58b-4692-96a1-c6ca1c48607b.png)

- **Expected Rewards**:                   
![image](https://user-images.githubusercontent.com/88390140/137599936-2afa37a5-1b11-4220-9253-274582fb79da.png)            
![image](https://user-images.githubusercontent.com/88390140/137599950-2d49632d-8276-4802-95fe-1c730fc61cc9.png)

- Some actions might control what an agent chooses to think about, or where it focuses its attention. 
- In general, actions can be any decisions we want to learn how to make, and the states can be anything we can know that might be useful in making them.         

![image](https://user-images.githubusercontent.com/88390140/137600508-8b8db77f-3fa8-4d23-a567-133ece32ea32.png)             
   
![image](https://user-images.githubusercontent.com/88390140/137600610-79cf207e-d402-442d-87ac-0650e5742338.png)       
  
![image](https://user-images.githubusercontent.com/88390140/137600645-d25a2a9d-992a-4ed4-8c62-1c8e8dc2ca38.png)          
 


























 



