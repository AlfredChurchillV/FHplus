# ic={'al':0,'j':4,'sd':98,'sts':9,'jhj':77,'hj':77}
#
# list=list(dict.values(ic))
# maxval=0
# second_maxval=0
# for i in list:
#     if i >maxval:
#         maxval=i
# for i in list:
#     if i >second_maxval and i<maxval:
#         second_maxval=i
#
# print(maxval,second_maxval)



# class CommonKeys:
#
#     dict1={'alice':100,'gwen':77,'hailey':79}
#     dict2 = {'alice': 100, 'gwen': 71, 'hailey': 79}
#     #print the people got same marks
#     def ck(self,dict1,dict2):
#
#             same_marks = {key: dict1[key] for key in dict1 if key in dict2 and dict1[key] == dict2[key]}
#             print(same_marks)

dict1 = {'alice': 100, 'gwen': 77, 'hailey': 79}
dict2 = {'alice': 100, 'gwen': 71, 'hailey': 79}

# Find the people with the same marks in both dictionaries
same_marks = {i: dict1[i] for i in dict1 if i in dict2 and dict1[i] == dict2[i]}

print(same_marks)




