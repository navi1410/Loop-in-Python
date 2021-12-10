num=int(input("enter any number"))
power=0
string=""
while(num>0):
    string=string+("0"*power)+str(num%10)+"+"
    num=num//10
    power=power+1
string=string[:-1]
print(string[::-1])