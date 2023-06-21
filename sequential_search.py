import random

def sequential_search(number_list, target_value):
    for index in range(len(number_list)):
        #determine is the number at the currnent index is equal to the target
        #If so return the index and end the loop
        if number_list[index] == target_value:
            return(index)
    return -1

def main():
    #create a list oif 100 number from 1 to 100
    number_list = random.sample(range(1,101), 100)
    number_list.sort()
    
    found_index = sequential_search(number_list, 77)

    print(found_index)

main()