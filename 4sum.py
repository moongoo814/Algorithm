class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    resArr = []
    numsLen = len(nums)
    if (numsLen == 4):
      if (nums[0] + nums[1] + nums[2] + nums[3] == target):
        return [[nums[0], nums[1], nums[2], nums[3]]]
      else:
        return []
    for i in range(0, numsLen - 3):
      if (target < nums[i] * 4) or (target > nums[-1] * 4):
        break
      if (i > 0 and nums[i] == nums[i-1]):
        continue
      
      for j in range(i + 1, numsLen - 2):
        if (target < (nums[i] + nums[j]) * 2) or (target > (nums[-1] + nums[-2])*2):
          break
        if (nums[j] == nums[j-1] and not (nums[i] == nums[j] and nums[i] != nums[i-1]) or nums[j] == nums[j-2]):
          continue
        lp = j + 1
        rp = numsLen - 1
        while lp < rp:
          sum = nums[i] + nums[j] + nums[lp] + nums[rp]
          if sum < target:
            lp += 1
          elif sum > target:
            rp -= 1
          else: # sum == target
            resArr.append([nums[i], nums[j], nums[lp], nums[rp]])
            while(lp < numsLen -1  and nums[lp] == nums[lp+1]):
              lp += 1
            while(rp > 0 and nums[rp-1] == nums[rp]):
              rp -= 1
            lp += 1
            rp -= 1
    return resArr
