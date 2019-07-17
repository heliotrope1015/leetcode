class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        ans = 0
        i=0
        while i <len(height):
            j=i+1
            while j <len(height):
                if height[j]<height[i]:
                    j+=1
                else:
                    if j-i>1:
                        for k in range(i+1,j):
                            ans=ans+(height[i]-height[k])
                    i=j
                    break
            if j ==len(height):
                i+=1
        return ans



if __name__ == '__main__':
    ans=Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print ans
