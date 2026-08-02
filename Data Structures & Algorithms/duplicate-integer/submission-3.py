class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) < len(nums)
        container = set()
        for i in nums: 
            if i in container:
                return True
            container.add(i)
        return False