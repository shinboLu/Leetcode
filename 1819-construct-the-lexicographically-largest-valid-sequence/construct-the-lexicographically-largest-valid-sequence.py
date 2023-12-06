class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr=[0]*((n*2)-1)
        self.ans=None
        def dfs(arr,i):
          #Traverse Reverse as we need highest lexicographic number
            for num in range(n,0,-1):
                if num not in arr:
                    if num==1:
                      #place is occupied
                        if arr[i]!=0:
                            continue
                        #Occupy the one place
                        else:
                            arr[i]=1
                    else:
                      #place is occupied or invalid
                        if arr[i]!=0 or (i+num)>=len(arr) or arr[i+num]!=0:
                            continue
                        else:#Occupy the two place
                            arr[i]=num
                            arr[i+num]=num
                    if 0 in arr:#means few places are still vacant
                        if dfs(arr,arr.index(0)):
                            return True
                        if arr[i]==1:#Backtracking vacate the one place
                            arr[i]=0
                        else:#Backtracking vacate both the two occupied place
                            arr[i]=0
                            arr[i+num]=0
                    else:#Yay no place is vacant 
                        self.ans=arr
                        return True
                    
        dfs(arr,0)
        return self.ans