# print("Hello", end="!!!\n Jamrock")
# pail = 2
# mail = 4
# print("{0}: {0}, {1}".format(pail, mail))
# print("{name} wants to eat {food}".format(name="Seme", food="Beans"))
# li= []
# li.append("Bambi prescott")
# li.append("Sasha")
# print(li)
# li.pop()
# li=[1,2,3,4,[3,4,53], 5,3]
# print(li[:2])
# print(li[::3])
# del li[2]
# print(li)
# print(li.remove(2))
# li.insert(1,344)
# print(li)
# jame=[4,3,5]
# dake = li + jame
# print(dake)
# li.extend([1,2,3])
# print(li)
# print(len(li))
# print(1 in li)
# print(li.index(2))
# tup =(1,2,4)
# print(tup[0])
# print(type((1)))

# print(tup + (4,3))
# print(tup[:2])
# print(2 in tup)
# a, *b, c =(1,2,4,5)
# print(*b)
# some_set ={1,1,3,3,4,5}
# filled_set =some_set
# print(filled_set.add(5))
# other_set ={3,2,4}
# print(filled_set & other_set)
# print(filled_set | other_set)
# print(filled_set - other_set)
# empty_dict ={}
# filled_dict = {"one":1, "two":2, "three":3}
# print(filled_dict)
# print(filled_dict["one"])
# jammy = list(filled_dict.keys())
# print(jammy)
# crammy = list(filled_dict.values())
# print(crammy)
# print("one" in filled_dict)
# print(filled_dict.get("one"))
# print(filled_dict.get("four"))
# print(filled_dict.get("four", 4))
# print(filled_dict.update({"four": 4}))
# filled_dict["four"]=44
# print(filled_dict)
# frimpong =-3
# if frimpong:
#     print("What")
# som_list =[1,2,3]
# some_string ='a string'
# print(1 in som_list)
# for letter in some_string:
#     print(letter)
# # for i in range(1, 35,3):
# #     print(i)
# print(range(3))
# print(list(range(3)))
# for num in range(1, 100, 15):
#     print(num)
# x = 0 
# while x < 3:
#     print(x)
#     x = x +1
# def add(x, y):
#     print("x is {} and y is {}".format(x, y))
#     print(x + y)

# add(5,55)
# add(x=5,y=5)
# def many_arguments(*args):
#     """args will be a tuple
#     """
#     print(args)
# many_arguments(1,2,4)

# def many_named_arguments(**kwargs):
#     """
#     kwargs will be a dictionary
#     """
#     print(kwargs)
# many_named_arguments(a=1, b=44)
# def both_together(*args, **kwargs):
#     print(args, kwargs)

# def subtract(x, y):
#     return x - y
# for i in range(5):
#     print(subtract(i, 10))


import requests
url ='https://en.wikipedia.org/w/index.php' 
r= requests.get(url)
print(r.text)