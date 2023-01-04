###
import math
from cmath import sqrt


def ask_value(variable_name): #variable input and check if it's digit
    while (True):
        variable = input("Enter the value for " + str(variable_name) + ": ")
        try:
            int(variable)
            return(int(variable))
        except:
            try:
                float(variable)
                return(float(variable))
            except:
                print("Please enter digits only!" + "\n")


def discriminant(a, b, c): #calculate Discriminant
    Discr = float(b)**2 - 4*float(a)*float(c)
    #return(Discr)
    return(float(b)**2 - 4*float(a)*float(c))

def roots(a, b, discr, roots_number): #calculate roots
    if roots_number == 1:
        x = (-1*b + math.sqrt(discr))/(2*a)
        print("root1 is: " + str(x))
    else:
        x1 = (-1*b + math.sqrt(discr))/(2*a)
        x2 = (-1*b - math.sqrt(discr))/(2*a)
        print("root1 is: " + str(round(x1, 4)))
        print("root2 is: " + str(round(x2, 4)))
    #

def solv_square(a,b,c):

    #красивый вывод уравнения при значении коэфф 0 и 1
    if a == 1:
      a_prn = "x^2"
    elif a == -1:
        a_prn = "-x^2"
    else:
        a_prn = str(a) + "x^2"

    if b == 0:
        b_prn = ""
    elif b == 1:
        if a != 0:
            b_prn = "+x"
        else:
            b_prn = "x"
    elif b == -1:
        b_prn = "-x"
    elif b > 0:
        if a != 0:
            b_prn = "+" + str(b) + "x"
        else:
            b_prn = str(b) + "x"
    else:
        b_prn = str(b) + "x"

    if c == 0:
        c_prn = ""
    elif c > 0:
        c_prn = "+" + str(c)
    else:
        c_prn = str(c)
    #####
    
    print("The equal is: " + a_prn + b_prn + c_prn + " = 0")

    
    discr = discriminant(a, b, c) #call and print discriminant. check the roots
    print("Discriminant is: " + str(discr))
    if discr == 0:
        print("One root only")
        roots_number = 1
    elif discr < 0:
        print("No roots!")
        exit()
    else:
        print("There are 2 roots")
        roots_number = 2

    roots(a, b, discr, roots_number)

#Main 
while (True):
    a = ask_value("a")
    if a != 0:
        break
    print("The valie \"a\" can not equal to zerro!\n")

b = ask_value("b")
c = ask_value("c")
print("a = " + str(a) + "\n" + "b = " + str(b) + "\n" + "c = " + str(c))

solv_square(a,b,c)
