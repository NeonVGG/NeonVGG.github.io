import random
ch='y'
while(ch != 'n' or 'N'):
    #12 digit latitude and longitude
    n=random.randint(111111111111,9999999999999)
    n1=random.randint(1,9)

    #This will generate random and new values every time
    n3=int(n/n1)

    #d1 and d2 will generate random directions where :
    #d1 gives a random vertical direction
    #d2 gives a random horizontal direction
    d1=random.randint(0,1)
    d2=random.randint(0,1)
    NS=['N','S']
    EW=['W','E']
    mf1=1
    mf2=1
    if d1==0:
        mf1=1
    else:
        mf1=-1
    if d2==0:
        mf2=-1
    else:
        mf2=1
    #converting to a string format to make it easier to display
    n2=str(n3)
    lat=float(n2[0:6])/10000*mf1
    lon=float(n2[6:12])/10000*mf2
    print("Degrees Minutes Seconds Form :")
    print(n2[0:2],"°",n2[2:4],"'",n2[4:6],NS[d1]," ",n2[6:8],"°",n2[8:10],"'",n2[10:12],EW[d2])
    print("Degree Decimal Form :")
    print(lat,lon)
    print("\nCopy pasting either values in google maps will give you a location, just remove extra spaces")
    ch=input("Do you want to continue (y/n)")
