nums = [11, 22, 33, 44, 55]
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x, y: x + 5 + y * 100, nums, nums1))
'''this is just using map function with multiple lambdas as the arguments.
Notice that we can apply the map function to the lists that have different length without any error.'''
print(result)
