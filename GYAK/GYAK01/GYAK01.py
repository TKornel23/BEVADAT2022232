#Create a function that decides if a list contains any odd numbers.
#return type: bool
#function name must be: contains_odd
#input parameters: input_list
     
def contains_odd(input_list):

    for number in input_list:
        if(number % 2 == 1):
            return True

    return False

     

#Create a function that accepts a list of integers, and returns a list of bool.
#The return list should be a "mask" and indicate whether the list element is odd or not.
#(return should look like this: [True,False,False,.....])
#return type: list
#function name must be: is_odd
#input parameters: input_list
     
def is_odd(input_list):

    result = []

    for number in input_list:
        if(number % 2 == 1):
            result.append(True)
        else:
            result.append(False)

    return result
        



#Create a function that accpects 2 lists of integers and returns their element wise sum. 
#(return should be a list)
#return type: list
#function name must be: element_wise_sum
#input parameters: input_list_1, input_list_2

def element_wise_sum(input_list_1, input_list_2):

    result = []

    for number_1, number_2 in zip(input_list_1, input_list_2):
        result.append(number_1 + number_2)
    
    return result

     

#Create a function that accepts a dictionary and returns its items as a list of tuples
#(return should look like this: [(key,value),(key,value),....])
#return type: list
#function name must be: dict_to_list
#input parameters: input_dict
     
def dict_to_list(input_dict):

    result = []

    for key, value in input_dict.items():
        result.append((key, value))
    
    return result


#If all the functions are created convert this notebook into a .py file and push to your repo