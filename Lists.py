# Lists

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  
# lines of commands where each command will be of the  types listed above. 
# Iterate through each command in order and perform the corresponding operation on your list.

# Example





# : Append  to the list, .
# : Append  to the list, .
# : Insert  at index , .
# : Print the array.
# Output:
# [1, 3, 2]
# Input Format

# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

# Direct Link: https://www.hackerrank.com/challenges/python-lists/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================

N = int(input())
ARRAY = []

while N != 0:
    A = input().split()

    if len(A) == 3:
        B = int(A[1])
        C = int(A[2])
    elif len(A) == 2:
        B = int(A[1])

    if A[0] == "insert":
        ARRAY.insert(B, C)
    elif A[0] == "print":
        print(ARRAY)
    elif A[0] == "remove":
        ARRAY.remove(B)
    elif A[0] == "append":
        ARRAY.append(B)
    elif A[0] == "sort":
        ARRAY.sort()
    elif A[0] == "pop":
        ARRAY.pop()
    elif A[0] == "reverse":
        ARRAY.reverse()
    N -= 1