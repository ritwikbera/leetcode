def mySqrt(x):
    if x==1:
        return 1

    low=0.0
    high=x*1.0
    count=1
    middle=(low+high)*0.5
    while (abs(middle*middle-x)>0.001) and (count<=10000):
        if middle*middle>x:
            high=middle
        else:
            low=middle
        middle=(low+high)*0.5
        count=count+1

    return int(round(middle)) if round(middle)-middle<0.1 else None

print(mySqrt(45))