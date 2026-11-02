class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(0, len(arr)-1):
            
            rightMaxEle = 0
            for j in range(i+1,len(arr)):
                if arr[j] > rightMaxEle:
                    rightMaxEle = arr[j]
            
            arr[i] = rightMaxEle
        
        arr[len(arr)-1] = -1
        
        return arr
        