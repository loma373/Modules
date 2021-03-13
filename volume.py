#Volume Calculator
pi=3.141592
def cylinder():
    r=int(input('Enter the radius '))
    h=int(input('Enter the height '))
    v=pi*r*r*h
    print('The volume of the cylinder is '+str(v))
cylinder()    
    
    
def cube():
    l=int(input('Enter the length '))
    v=l**3
    print(v)
    
def cuboid():
    l=int(input('Enter the length '))
    b=int(input('Enter the breadth '))
    h=int(input('Enter the height '))
    v=l*b*h
    print(v)
    
def cone():
    r=int(input('Enter the radius '))
    h=int(input('Enter the height '))
    v=1/3*pi*(r**2)*h
    print(v)
    
def sphere():
    r=int(input('Enter the radius '))
    v=4/3*(r**3)
    print(v)
    
    