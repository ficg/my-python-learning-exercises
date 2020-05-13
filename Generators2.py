def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i


print(list(numbers(11))) # using generator function

# print(list([x for x in range(11) if x % 2 == 0]))  # using list comprehension

# print(list(filter((lambda x: x % 2 == 0), range(11))))  # using lambda filter

'''Replace your range of 11 for 1 million and you will see the difference. 
look at your memory and the absurd time it would take to do all at once before returning some result. '''