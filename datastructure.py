name_list = ["Ali", "Jafar", "Mamad", "Hossein"]
print(name_list.remove("Mamad"))
print(name_list)
del name_list[-1]
print(name_list)
name_list.append("akbar")
print(name_list)



for i in range(len(name_list)):
    print("Hello {}".format(name_list[i]))



a=" "
for i_name in name_list:
    print("Hello {}".format(i_name))
    a += i_name + "_"

print(a)


print("=="*20)
print("|".join(name_list))



human_dic = {"name" : "Hassan", "color" : "Blue", "age": 20}
print(human_dic["age"])
human_dic["age"] = 25
human_dic["color"] = "Black"
print(human_dic)

human_dic = {"name" : ["Hassan", "Ali", "mamad"], "color" : ["Blue", "white", "Green"], "age": [20 , 30 , 40]}

for i in range(len(human_dic["name"])):
    for key in human_dic.keys():
        # print(human_dic[key])
        key_list = human_dic[key]
        print("My {} is {}"
        .format(key, key_list[i]))


human_list = [{"name":"ali", "age" : 20} , {"name":"akbar", "age" : 10}, {"name":"ahmad", "age" : 30}]
for i_human in human_list:
    print("My name is {}. My age is {}"
    .format(i_human["name"] , i_human["age"]))


for i_human in human_list:
    name, age = i_human.items()
    print("My name is {}. My age is {}"
    .format(name[-1] , age[-1]))

name_list = ["ali", "akbar", "jafar"]
age_list = [19, 34, 29]

#List comprehension
human_list = [{"name":i_name, "age":i_age}
 for i_name, i_age in zip(name_list, age_list)]
print(human_list)



human_list2 = []
for i_name, i_age in zip(name_list, age_list):
    human_list2 += [{"name":i_name, "age":i_age}]
print(human_list2)



human_list3 = []
for i_name, i_age in zip(name_list, age_list):
    human_list3.append([{"name":i_name, "age":i_age}])
print(human_list3)




