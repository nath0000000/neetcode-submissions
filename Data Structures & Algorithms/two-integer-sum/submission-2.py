class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #brute force solution
        # for i in range(len(nums)):
        #     answer = target - nums[i]
        #     for j in range(i+1, len(nums)):
        #         if nums[j]==answer:
        #             return [i,j]
        # return []
        nums_dict = dict()
        for index, num in enumerate(nums):
            if nums_dict.get(num, None) == None:
                nums_dict[num] = [index]
            else: nums_dict[num].append(index)
        
        for num, _ in nums_dict.items():
            if (target-num) in nums_dict:
                if (target-num) != num:
                    return [nums_dict[num][0], nums_dict[target-num][0]]
                if len(nums_dict[num]) > 1:
                    return [nums_dict[num][0], nums_dict[target-num][1]]
            





        