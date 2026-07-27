class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        write = 0

        # Move non-zero elements to the front
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # Fill remaining positions with zeros
        while write < len(nums):
            nums[write] = 0
            write += 1