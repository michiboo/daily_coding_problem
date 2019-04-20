'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

def cal(num_list, k):
    for x in range(len(num_list)):
        for y in range(x+1,len(num_list)):
            if num_list[x] + num_list[y] == k:
                return True
    return False


num_list = [int(i) for i in input().split()]
k = int(input())
print(cal(num_list,k))
