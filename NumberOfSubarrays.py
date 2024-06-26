# https://leetcode.com/problems/count-number-of-nice-subarrays/?envType=daily-question&envId=2024-06-22
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

# Example 2:
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.

# Example 3:
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            left = count = result = 0
            
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    k -= 1
                
                while k < 0:
                    if nums[left] % 2 == 1:
                        k += 1
                    left += 1
                
                result += right - left + 1
            
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)


