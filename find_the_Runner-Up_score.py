# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains . The second line contains an array   of  integers each separated by a space.

# Constraints

# Output Format

# Print the runner-up score.

# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5
# Explanation 0

# Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.


# Direct Link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================


N = int(input())
ARRAY = map(int, input().split())
MY_LIST = list(ARRAY)

MY_LIST.sort()
HIGHEST_NUMBER = max(MY_LIST)

for i in range(len(MY_LIST)-1, -1, -1):
    if MY_LIST[i] < HIGHEST_NUMBER:
        break

print(MY_LIST[i])