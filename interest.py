def compoundInterest():

    p=int(input('Enter the principal amount')) 
    r=int(input('Enter the rate of interest')) 
    t=int(input('Enter the time'))
    ci=p*(r**t)
    print('the compound interest is '+str(ci))


def simpleInterest():

    p=int(input('Enter the principal amount')) 
    r=int(input('Enter the rate of interest')) 
    t=int(input('Enter the time'))
    ci=p*r*t/100
    print('the simple interest is '+str(ci))

print('Welcome to interest calculator')
