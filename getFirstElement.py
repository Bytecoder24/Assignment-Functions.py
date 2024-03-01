def getFirstElement(input_list):
    if input_list:
        return input_list[0]
    else:
        return None

my_list = [5, 6, 7,8,9]
first_element = getFirstElement(my_list)
print(first_element)
