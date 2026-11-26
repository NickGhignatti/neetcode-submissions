class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        first = 0
        last = len(nums) - 1
        s = sorted(nums)

        while first < last:
            current = s[first] + s[last]
            if current == target:
                idx = nums.index(s[first])
                idy = nums.index(s[last])
                if idx == idy:
                    idy = nums.index(s[last], idx + 1)
                return [idx, idy] if idx < idy else [idy, idx]
            elif current > target:
                last -= 1
            else:
                first += 1
        
        return [0, 0]
