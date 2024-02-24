# odds only
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (nums[0:10:2])

# negative order
print (nums[::-1])

#join method
print (".".join(str(nums))) #only works on string, not int. [] should not be binded.
print ("\n".join(str(nums)))

#split method
str = "abcd/efgh/ijkl"
str = str.split("/")
print (str)

#sort
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
print(data[::-1])