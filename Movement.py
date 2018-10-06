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

Answer = Matrix([[1], [0]])     #Starting point
Theta= [pi/2, pi/2, pi, pi/2]   #Holds all the angles
Length= [1, 1, 1, 1]            #Holds all lengths
PlotX= []           #Will hold all the x co-ordinate to plot
PlotY= []           #Will hold all the y co-ordinate to plot

for j in range(1,4):    #First For loop goes from j=1 to i=n which is 4 in this example
    for i in range(j):  #second for loop which goes from i=0 to j
        Answer= eqn.subs([(Angle, Theta[i]), (x, Answer[0, 0]), (y, Answer[1, 0]), (L, Length[i])]) #this subsitutes all the values in the equation
        #print (Answer)
        PlotX.append(Answer[0, 0])  #adds all the x values in an array
        PlotY.append(Answer[1, 0])  #adds all the y values in another array
        
plt.plot(PlotX, PlotY, "ro")  #plots the points on a graph
plt.show()      #shows the plot