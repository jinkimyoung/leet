import time

class TwoSum:
    def __init__(self):
        """
            Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
            You may assume that each input would have exactly one solution, and you may not use the same element twice.
            You can return the answer in any order.
        """
        pass
    def twoSum_BruthForth(self, nums, target):
        """
            Brute Force
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i,j]

    def twoSum_TwoPassHashMap(self, nums, target):
        """
            Two Pass HashMap
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

    def twoSum_OnePasHashMap(self, nums, target):
        """
            It turns out we can do it in one-pass. 
            While we are iterating and inserting elements into the hash table, we also look back to check if current element's complement already exists in the hash table.
            If it exists, we have found a solution and return the indices immediately.
            - Time complexity: O(n)
            - Space complexity: O(n)
        """
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i
         

two = TwoSum()
print(two.twoSum_BruthForth([2,7,11,15], 9))
print(two.twoSum_TwoPassHashMap([2,7,11,15], 9))
print(two.twoSum_OnePasHashMap([2,7,11,15], 9))