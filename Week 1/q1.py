 def maxSubArraySum(self,arr,n):
        #variable to store the maximum subarray sum
        ans=arr[0]
        #iterating over the array
        for i in range(0,n):
            temp=0
            #generate all subarrays starting from the ith index 
            #and compare its sum with the answer and update the answer with maximum one
            for j in range(i,n):
                temp += arr[j]
                ans = max(ans,temp)
        return ans