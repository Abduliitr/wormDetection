print("Holla!! Pratham. Let's get started dude....#Started working on a project at Texas Technical University, Texas, United States of America")


import math

def f1(x):
    return x*x-2.0

def df1(x):
    return 2.0*x

def newton(x):
    # Newton-Raphson root finding method
    nmax=100
    tolerance=1.0e-10
    for i in range(0,nmax):
        fx= f1(x)
        dfx=df1(x)
        x=x-fx/dfx
        print("fx",fx,"dfx",dfx,"x=",x)
        if abs(fx)<tolerance: return x
    return x


a=float(input("enter initial guess : "))
r=newton(a)
print(" ROOT : ",r,"\nFUNCTION VALUE : ",f1(r))