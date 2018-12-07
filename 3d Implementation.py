# =============================================================================
from tkinter import *
import sympy as sp
import scipy.optimize as opt
from numpy import *
import timeit
import matplotlib.pyplot as plt

window = Tk()
 
window.title("Robot Arm")
 
window.geometry('200x100')
 
lbl1 = Label(window, text="Enter Co-ordinate X- ")
 
lbl1.grid(column=0, row=1)
 
txt1 = Entry(window,width=10)
 
txt1.grid(column=1, row=1)

lbl2 = Label(window, text="Enter Co-ordinate Y- ")
 
lbl2.grid(column=0, row=3)

txt2 = Entry(window,width=10)
 
txt2.grid(column=1, row=3)

lbl3 = Label(window, text="Enter Co-ordinate Z- ")
 
lbl3.grid(column=0, row=5)

txt3 = Entry(window,width=10)
 
txt3.grid(column=1, row=5)

a=0
b=0
c=0
def f(variables) :
    global a
    global b
    s= variables[0]
    c= variables[1]
    #l2= variables[2]
    #l1= variables[3]
    #(s, c, l2, l1) = variables
    l2=20
    l1=15
    eq1 = l2 * c + l1 - a
    eq2 = l2 * s - b
    eq3 = c**2 + s**2 - 1
    #eq4 = l2 * s - b
    return array([eq1, eq2, eq3])

def clicked():
    global a
    global b
    global c
    a = float(txt1.get()) 
    b = float(txt2.get())
    c= float(txt2.get())
    
    baseAngle= arctan(c/a)
    print(baseAngle)
    a= a/(cos(baseAngle))
    print(a)
    
    st1 = timeit.default_timer()
    
    solution = opt.root(f, (0,0), method='lm' )
    #solution = opt.minimize(f, array([1,0, 0, 0]))
    
    answers= solution.x
    #answers= answers.round().astype(int)
    print(answers[0])
    print(answers[1])
    print("-----------")
    print(answers)
    angle= arcsin(answers[0])
    Theta= [angle]
    #Answer = sp.Matrix([(answers[2]), 0])
    Answer= sp.Matrix([[15], [0]])
    #Length= [(answers[3])]
    Length= [20]
    
    Angle = sp.Symbol('Angle')  #Variable to hold the angles
    Cosine= sp.cos(Angle)      #Variable name to hold cos
    Sine= sp.sin(Angle)        #Variable name to hold sin
    M1= sp.Matrix([[Cosine, -Sine], [Sine, Cosine]])  #Variable name to hold matrix (cos  -sin)
    #                                                                            #(sin   cos)
    x= sp.Symbol('x')  #Holds the x co-ordinate of the initial point
    y= sp.Symbol('y')  #Holds the y co-ordinate of the initial point
    M2 = sp.Matrix([[x], [y]])  #Matrix that holds the x co-ordinate in the 1st row and y co-ordinate in the 2nd row
    L= sp.Symbol('L')  #Holds the legnths
    M3 = sp.Matrix([[L], [0]])     #Matrix to hold the legnth L, 0 as row 1 and row 2 respectively
    eqn= M1 * M2 + M3  #The main equation
    #Answer = Matrix([[1], [0]])     #Starting point  #Also this is L1
    #Theta= [pi/3, pi/3, pi/3, pi/3, pi/3]   #Holds all the angles
    #Length= [1, 1, 1, 1, 1]            #Holds all lengths except the first one
    PlotX= []           #Will hold all the x co-ordinate to plot
    PlotY= []           #Will hold all the y co-ordinate to plot
    PlotX.append(0)  #adds all final x value in an array which will be the origin point based on the last hand
    PlotY.append(0)  #adds all final y value in an array which will be the origin point based on the last hand
    PlotX.append(Answer[0, 0])  #adds all initial x value in an array
    PlotY.append(Answer[1, 0])  #adds all initial y value in an array
    for j in range(0,1):    #First For loop goes from j=1 to i=n which is 4 in this example
        for i in range(j+1):  #second for loop which goes from i=0 to j
            Answer= eqn.subs([(Angle, Theta[i]), (x, Answer[0, 0]), (y, Answer[1, 0]), (L, Length[i])]) #this subsitutes all the values in the equation
            print (Answer)
            PlotX.append(Answer[0, 0])  #adds all the x values in an array
            PlotY.append(Answer[1, 0])  #adds all the y values in another array
    fig = plt.figure()
    ax = fig.add_subplot(111)       
    plt.plot(PlotX, PlotY)  #plots the points on a graph
    # =============================================================================
    # for xy in zip(PlotX, PlotY):
    #     i=0                                       # <--
    #     ax.annotate('(%s)' % Theta[i], xy=xy, textcoords='data')
    #     i=i+1
    # =============================================================================
    plt.grid()      #shows the grid
    plt.show()      #shows the plot
    # 
    # =============================================================================
    st2 = timeit.default_timer()
    print("RUN TIME : {0}".format(st2-st1))    
btn = Button(window, text="Calculate", command=clicked)
 
btn.grid(column=0, row=7)
 
window.mainloop()


# =============================================================================
# solution = opt.fsolve(f, (1,0, 0.8, 1.5))
# print(solution)
# =============================================================================
