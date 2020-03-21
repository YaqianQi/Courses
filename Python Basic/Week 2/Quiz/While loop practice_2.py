n = int(input())+1
nums = [0 for i in range(n+1)]
nums[1] = 1000
for i in range(2, n +1):
    nums[i] = int(nums[i-1] *1.15)
res = int(nums[n])
print(res)