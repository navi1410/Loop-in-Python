print("WELCOME TO THE BIRTHDAY PARTY")
age=9
can_height=[1,3,4,6,4,6]
can_height.sort()
# pprint(can_height)
max=0
i=0
while i<len(can_height):
    c=0
    if can_height[i]>max:
        max=can_height[i]
    i+=1
    for ele in can_height:
        if ele==max:
            c+=1
print("Tallest Candle is:",max)
print("Number Of Candle is:",c)