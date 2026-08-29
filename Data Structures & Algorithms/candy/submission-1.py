class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        res=[1]*n
        for i in range(1,n):
            local_max=True

            if ratings[i]<=ratings[i-1]:
                local_max=False

            if local_max==True:
                if i==0:
                    res[i]+=1
                else:
                    res[i]=res[i-1]+1

        for i in range(n-2,-1,-1):
            local_max=True

            if ratings[i]<=ratings[i+1]:
                local_max=False

            if local_max==True:
                if i!=n-1:
                    res[i]=max(res[i],res[i+1]+1)
        return sum(res)