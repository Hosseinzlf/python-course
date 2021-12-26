int1 = 6
int2 = 79
print(int1*int2)
print(int1+int2)
print(int1-int2)
print(int1/int2)
print(int1**int2)

print(int1%2)
print(int1+6)

for i in range(1,8):
    if int1*i>40:
        print(int1*i+int2)
        print("The number {} is bigger than 40 ".format(int1*i))
    elif i==7:
        print("You are lucky")
    elif i>3:
        int2 +=i 

           

    


