class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = [[]]
        def back_track(nums,temp,start,sub_lenght):
            
            if len(temp)==sub_lenght:
                temp_copy = temp[:]
                output.append(temp_copy)
                return
            
            for i in range(start,len(nums)):
                temp.append(nums[i])
                back_track(nums,temp,i+1,sub_lenght)
                temp.pop()
        
        for j in range(1,len(nums)+1): 
            back_track(nums,[],0,j)
        
        
        return output
            


nums = [0]           
obj = Solution()

print(obj.subsets(nums))
            
            
            
            