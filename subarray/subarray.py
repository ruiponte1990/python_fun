def maxSubArray(nums):
        max_sum = nums[0]
        current_sum = max_sum
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(current_sum, max_sum)
        return max_sum

print(maxSubArray([5,4,-1,7,8]))