n=3*16**2018-2*8**1028-3*4**1100-2**1050-2022
count=0
while n:
    if n%4==3:
        count+=1
    n//=4
print(count)