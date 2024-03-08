def HCF(x,y):
    smaller = min(x,y)

    for i in range(1,smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

x = 24
y = 36

print(HCF(x,y))