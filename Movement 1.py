from sympy import *
import matplotlib.pyplot as plt

Angle = Symbol('Angle')  #Variable to hold the angles
Cosine= cos(Angle)      #Variable name to hold cos
Sine= sin(Angle)        #Variable name to hold sin
M1=Matrix([[Cosine, -Sine], [Sine, Cosine]])  #Variable name to hold matrix (cos  -sin)
                                                                           #(sin   cos)
x= Symbol('x')  #Holds the x co-ordinate of the initial point
y= Symbol('y')  #Holds the y co-ordinate of the initial point
M2 = Matrix([[x], [y]])  #Matrix that holds the x co-ordinate in the 1st row and y co-ordinate in the 2nd row
L= Symbol('L')  #Holds the legnths
M3 = Matrix([[L], [0]])     #Matrix to hold the legnth L, 0 as row 1 and row 2 respectively
eqn= M1 * M2 + M3  #The main equation
Answer = Matrix([[1], [0]])     #Starting point  #Also this is L1
Theta= [pi/3, pi/3, pi/3, pi/3, pi/3]   #Holds all the angles
Length= [1, 1, 1, 1, 1]            #Holds all lengths except the first one
PlotX= []           #Will hold all the x co-ordinate to plot
PlotY= []           #Will hold all the y co-ordinate to plot
PlotX.append(0)  #adds all final x value in an array which will be the origin point based on the last hand
PlotY.append(0)  #adds all final y value in an array which will be the origin point based on the last hand
PlotX.append(Answer[0, 0])  #adds all initial x value in an array
PlotY.append(Answer[1, 0])  #adds all initial y value in an array
for j in range(1,5):    #First For loop goes from j=1 to i=n which is 4 in this example
    for i in range(j+1):  #second for loop which goes from i=0 to j
        Answer= eqn.subs([(Angle, Theta[i]), (x, Answer[0, 0]), (y, Answer[1, 0]), (L, Length[i])]) #this subsitutes all the values in the equation
        print (Answer)
        PlotX.append(Answer[0, 0])  #adds all the x values in an array
        PlotY.append(Answer[1, 0])  #adds all the y values in another array
fig = plt.figure()
ax = fig.add_subplot(111)       
plt.plot(PlotX, PlotY, "ro")  #plots the points on a graph
for xy in zip(PlotX, PlotY):
    i=0                                       # <--
    ax.annotate('(%s)' % Theta[i], xy=xy, textcoords='data')
    i=i+1
plt.grid()      #shows the grid
plt.show()      #shows the plot