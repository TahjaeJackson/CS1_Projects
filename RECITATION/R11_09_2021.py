# Name: Tahjae Jackson
# Date: November 9, 2021
# Purpose: Dictionary

# Create a function that takes a dictionary as a parameter:
#      key : NetID strings
#      value: string name
# the function should print out all the names of the dictionary

# def print_names(dict):
#     for key in dict:
#         print(dict[key])
#
#
#
# my_dict = {"F00123":"Apurva","F00124":"Isaac","F00125":"Kelly","F00126":"Vasanta", "F00127":"Bob","F00128":"Mary"}
#
# print_names(my_dict)


# Define a function that takes a list of names (strings). Your function returns a dictionary such that
#     keys : names
#     values: Number of times the name is in the list

def num_of_times(list):
    dict = {}
    for name in list:
        if len(name) not in dict:
            dict[len(name)] = 1
        else:
            dict[len(name)]+=1

    return dict

names = ["Sam", "Bob", "Sam", "Joe", "Joe", "Kevin"]
print(num_of_times(names))


# Define a function that takes a dictionary as a parameter. Inside the dictionary
#       keys = ID
#       values = names
# return a new dictionar with names as keys and a positive integer as value giving the number of students with that name
# in the original dictionary

# def new_dict(dict):
#     new_dict = {}
#     for names in dict:
#         val = dict[names]
#         if val not in new_dict:
#             new_dict[val] = 0
#         if val in new_dict:
#             new_dict[val] = new_dict[val] + 1
#
#     return new_dict
#
# dict = {"F00123":"Apurva","F00124":"Isaac","F00125":"Kelly","F00126":"Vasanta", "F00127":"Isaac","F00128":"Kelly"}
# print(new_dict(dict))








