class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        mid = (l+r)//2
        while l<mid and r>mid:
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                l = mid
            else:
                r = mid
            mid = (l+r)//2
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        return -1