'''
Given an integer array, find a subarray where the sum of numbers is zero.
Your code should return the index of the first number and the index of the last number.

 Notice

There is at least one subarray that it's sum equals to zero.

Have you met this question in a real interview? Yes
Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].

'''

class Solution:
    def subarraySum(self, nums):
        hs = {0:-1}
        sum = 0
        sums = []
        for i in range(len(nums)):
            sum += nums[i]
            if sum in hs:
                sums.append([hs[sum] + 1, i])

            hs[sum] = i
        return sums


s = Solution()
a = [-3, 1, 2, -3, 4]
print(s.subarraySum(a))
