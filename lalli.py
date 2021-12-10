# my_dict = {
#         'data1':100,
#         'data2': -54,
#         'data3': 247
#        } 
# s=0
# for i in my_dict:
# 	s=s+my_dict[i]
# print(s)

# 2)question

# list1=["one","two","three","four"]
# list2=[1,2,3,4]
# i=0
# a={}
# while i<len(list1):
#     a[list1[i]]=list2[i]
#     i+=1
# print(a)

# dic={
#     'ball':'red',
#     'bat':4,
#     'wickets':8,
#     'ball':'green',
#     'bat':3
#     }
# dic["ball"]="red"
# dic["bat"]=4
# # dic.update()
# print(dic)

# 4)question

list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
a=[]
for key in list1:
    for i in key:
        if key[i] in a:
            pass
        else:
            a.append(key[i])
print(a)