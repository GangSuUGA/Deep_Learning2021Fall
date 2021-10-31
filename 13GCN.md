## Resourse 
- ![image](https://user-images.githubusercontent.com/88390140/139561763-0e42054f-d768-4ca9-8186-822e9ed32b01.png)

———————————————————————————————————————————————— 
## Motivation 
🥋 CNN is limited to learn complex spatio-related feature. 
![image](https://user-images.githubusercontent.com/88390140/139562688-78a22750-938b-4d3f-b391-d0641b4a20c6.png)
- Improvement of CNN:          
🍮 Let filter kernel more flexbile and learnable to the dynamic varability of data. 

- However, the flexible Kernel still can not handle more complex problem in real world.  

________________________________________ 
# The basic idea of GCN (Spectral Approaches)   
### Fourier:     
![image](https://user-images.githubusercontent.com/88390140/139561716-ca7eff89-d25d-42a1-8a8f-3e6e647f7492.png)

### Inverse Fourier:     
![image](https://user-images.githubusercontent.com/88390140/139561725-a5d91c71-fbf1-4acc-b4db-d54a991477b8.png)

### How to convolute? 
![image](https://user-images.githubusercontent.com/88390140/139561747-403fa685-d1a9-4b79-bdb3-3de45c153f1e.png)

### How to define graph fourier transformer? 
![image](https://user-images.githubusercontent.com/88390140/139561875-8bef61f6-247a-42e5-b186-caa9eb7796d7.png)

# Background 
![image](https://user-images.githubusercontent.com/88390140/139561984-032dd72b-b0a6-4b94-b9f3-cc0f4f8ea5bd.png)

- L Matrix positive semidifinite proof:
![image](https://user-images.githubusercontent.com/88390140/139562701-79ef4050-7603-4501-9362-3a3faa72da92.png)

- Eigen Decomposition or Spectral Decomposition: 
![image](https://user-images.githubusercontent.com/88390140/139563236-f3f6c0a8-81f6-4488-8dd6-2b01ef955424.png)
![image](https://user-images.githubusercontent.com/88390140/139563248-c121db02-c02d-428b-b31f-e6c250e13e2e.png)![image](https://user-images.githubusercontent.com/88390140/139563215-938fde2b-1c1a-47e6-b0c7-eab1a0b60637.png)


- Laplace Operator:            
![image](https://user-images.githubusercontent.com/88390140/139562586-b64e6c50-9e04-48e6-b877-e4233c6edc2a.png)

![image](https://user-images.githubusercontent.com/88390140/139562610-20b5bb44-30e6-46a2-b41e-b35ac2a30857.png)
![image](https://user-images.githubusercontent.com/88390140/139562612-db19f3e6-dc8d-455d-a5c7-78fc5d978ed0.png)
![image](https://user-images.githubusercontent.com/88390140/139562654-325e5495-a997-4221-8c93-96a25f5ff9ab.png)

- Weighted: 
![image](https://user-images.githubusercontent.com/88390140/139562735-247cb04a-c17c-44c6-ae65-85a956dc8f7c.png)
![image](https://user-images.githubusercontent.com/88390140/139562751-6f32f899-0220-4a96-b9fb-06bb76f4c8d1.png)


# Graph Fourier Transformer 
![image](https://user-images.githubusercontent.com/88390140/139562793-7181f9b2-9318-4579-9149-7c1e3ace399e.png)

![image](https://user-images.githubusercontent.com/88390140/139563125-f75fbfdd-d865-4231-934a-90eaf3329b7b.png)

![image](https://user-images.githubusercontent.com/88390140/139563138-a10db29d-761c-4e0c-bbce-d3a4e3dc012c.png)

![image](https://user-images.githubusercontent.com/88390140/139562838-0362147a-5e32-4257-8054-a3e4d2ebcfb3.png)![image](https://user-images.githubusercontent.com/88390140/139562884-18116778-eaa8-42b7-a21a-6116ce41b7ae.png)


⭐ ![image](https://user-images.githubusercontent.com/88390140/139563057-646984e9-bdcb-4b5e-bc66-114e21b1eef2.png)

![image](https://user-images.githubusercontent.com/88390140/139563312-f9789e80-83c7-47f7-937c-1c8b26967649.png)




