#importing important modules
import numpy as np 
import matplotlib.pyplot as plt 









# solution 18-------Kanha Aggarwal(2026UUE0353)


# defining a 6 X 2 matrix named ary. Here, column 1 is X and column 2 is Y.
ary = np.array([
    [1, 2], 
    [3, 4],
    [5, 6], 
    [7, 8], 
    [9, 10], 
    [11, 12]
])
print("The Matrix 6X2:")
print(ary)


# printing X vector
print("The Vector X is:\n", ary[::, :1:])

# printing vector Y
print ("The Vector Y is:\n" , ary[::,1::])















print("\n\n\n\n\n\n\n")
#solution 19



#defining 7 vectors
p1 = np.array([7,14])
p2 = np.array([3,19])
p3 = np.array([11,5])
p4 = np.array([16,2])
p5 = np.array([2,20])
p6 = np.array([9,13])
p7 = np.array([7,4])


#printing the 7 vectors
print("The vector p1:", p1)
print("The vector p2:", p2)
print("The vector p3:", p3)
print("The vector p4:", p4)
print("The vector p5:", p5)
print("The vector p6:", p6)
print("The vector p7:", p7)


print("\n\n")


vect = [p1, p2, p3, p4, p5, p6, p7] #making a list/sequence of all the vectors
disp=[] #an empty list where all the vector change will be stored

#calculating change in p(k) and p(k+1) and printing and storing the magnitude in disp
for i in range(0,6):
    print(f"The change in vector is p{i+1} and p{i+2}:")
    a = (vect[i] - vect[i+1]) #the change in consecutie position as vector
    print(a) # printing that change vector
    disp.append(np.sum((a**2))) #storing the change in disp
displ = np.array(disp) #turning disp as an array
print("\nThe max disp is in interval p", np.argmax(displ)+1, "and p" ,np.argmax(displ)+2 , "and the magnitude of displacemnt is", np.max(displ))
















print("\n\n\n\n\n\n\n")
#solution 20-------Kanha Aggarwal(2026UUE0353)
# we have to plot y=0.5x


x = np.linspace(0, 10, 6) #making an array for x axis
y1 = 0.5*x #making an array for desired Y coordinate
y2 = np.array([0.1, 1.1, 1.9, 3.2, 3.9, 5.1])# an array for observed Y coordinate


plt.plot(x,y1, color= "orange", label= "Desired Trajectory" )
plt.plot(x, y2,  linestyle= "dashed", marker= "o" , color= "red", markerfacecolor= "red", label= "Obsereved Trajectory")
plt.title("Trajectory of Drone", fontweight= "bold", fontsize = 30)
plt.xlabel("X - coordinate(in m)", color = "purple", fontsize = 20)
plt.ylabel("Y - coordinate(in m)", color = "cyan", fontsize = 20)
plt.yticks(x)
plt.legend()
plt.show()
















print("\n\n\n\n\n\n\n")
#solution 21-------Kanha Aggarwal(2026UUE0353)


Ey = abs(y1 - y2)#array of error in y asssuming X absolute
print("The error in Y is assuming X as absolute:")
print(Ey)
print("The tolerance = 0.25m")

#analysis of data
if np.max(Ey)<=0.25:
    print("The trajectory is ACCEPTED")
else: 
    print("The trajectory is REJECTED")



#changing the data and reanalyzing it
print("If we change the tolerance to 0.1m")
if np.max(Ey)>0.1 and np.max(Ey)<0.25 :
    print("The trajectory is now rejected")
    print("The decision is now changed because in engineering the decision is based on need and application of the model not just on data values alone.")
elif np.max(Ey)>0.1:
    print("The trajectory is still rejected")
else:
    print("The trajectory is still accepted")