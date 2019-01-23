import matplotlib.pyplot as plt
import math

Px0 = []
Px1 = []
Hx0=[]
Hx1=[]
A=0.99
B=0.01

for i in range(99):
    V = math.log(A,2)
    J = math.log(B,2)
    Hx0.append((-A*V)+(-B*J))
    Px0.append(A)
    Px1.append(B)
    
   # Hx1.append(-A*(math.log(A,2)) -B*(math.log(B,2)))
    A -= 0.01
    B += 0.01
   
for i in range(20):
    print()
    print("P(x): ",end="")
    for j in range(5):
        print(str(Px0[j*i+i])+",",end="")
print()        
print("=======================================================================================================")      
for i in range(20):
    print()
    print("H(x): ",end="")
    for j in range(5):
        print(str(Hx0[j*i+i])+",",end="")        
plt.plot(Px0, Hx0, color='orange')
plt.xlabel('P(X)')
plt.ylabel('H(X)')
plt.title('Binary entropy function')
plt.show()

