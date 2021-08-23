class Solution:
    #time: O(N), where N is the length of input list;
    #space: O(M), where M is the max length of the stack (sorted list).
    def summaryRanges(self, nums: List[int]) -> List[str]:
        nums = nums + [-1] # padding with one more number as we need to compare nums[i] with nums[i+1].
        res = []
        stack = []
        for i in range(len(nums)-1): # traverse the list
            stack.append(nums[i]) # push into the stack
            if nums[i]+1 != nums[i+1]: # if we found a compete sorted list
                if len(stack) == 1: # this list contains only one element
                    res.append(str(stack.pop()))
                else: # this list contains more than one elements
                    res.append("{0}->{1}".format(stack[0], stack[-1]))
                stack = [] # reset the stack for each sorted list
        return res
