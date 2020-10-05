import math, time, random
import numpy as np
ntrials= 1000
x1=np.random.random(ntrials)
y1=np.random.random(ntrials)
z1=np.random.random(ntrials)
x2=np.random.random(ntrials)
y2=np.random.random(ntrials)
z2=np.random.random(ntrials)
x1= np.array(0.2)
y1= np.array(0.34)
z1= np.array(0.57)
x2= np.array(0.3)
y2= np.array(0.59)
z2= np.array(0.74)
ntrials=10000000
dist=0
start_time=time.process_time()
for i in range(ntrials):
    x1=random.random()
    y1=random.random()
    z1=random.random()
    x2=random.random()
    y2=random.random()
    z2=random.random()
    dist+=math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
dist/=ntrials
e_time=time.process_time()-start_time
dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
ex_dist=1/105*(4+17*math.sqrt(2)-6*math.sqrt(3)+21*math.log(1+math.sqrt(2))+42*math.log(2+math.sqrt(3))-7*math.pi)
print("Ntrials=%d  Ave dist=%9.7f  Exact dist=%9.7f time=%6.2f"%(ntrials,dist,ex_dist,e_time))