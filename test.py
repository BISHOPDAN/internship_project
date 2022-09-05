"""
def solution (strings,source):
    strr = ''
    prefix = []
    response = []
    for r in strings:
        strr = strr + r
        prefix.append(strr)
    for sor in source:
        if sor in prefix:
            response.append(True)
        else:
            response.append(False)

    return response

my_data = solution(["one", "two", "three"], ["four", "five"])
print(my_data)
"""


def twoSum(nums: list[int], target: int) -> list[int]:
    nums2 = sorted(nums)
    left = 0
    right = len(nums)-1
    while left < right:
        if nums2[left] + nums2[right] == target:
            x = nums.index(nums2[left])
            nums[x]=None
                
            y=nums.index(nums2[right])
            return [x,y]
        elif nums2[left] + nums2[right] < target:
            left+=1
            
            
            
        else:
            
            right -=1

p1 = twoSum([2,7,11,15],13)
print(p1)


def twoSum(nums: list[int], target: int) -> list[int]:
    output = []
    for i in nums:
        for j in nums:
            if i + j == target and nums.index(i) != nums.index(j):
                output.append(nums.index(i))
                output.append(nums.index(j))
                return output

outputs = twoSum([3,4,6,7],9)
out = twoSum([3,2,4],6)
print(outputs)
print(out)



     