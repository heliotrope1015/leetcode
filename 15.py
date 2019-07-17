class Solution(object):

    def sums(self,nums,index,c,step,arr,list1):
        if step >3:
            return
        if c==0 and step ==3:
            arr1=arr[:]
            if len(list1)==0:
                list1.append(arr1)
            else:
                for i in range(len(list1)):
                    if list(set(list1[i]).difference(set(arr1)))==[] and list(set(arr1).difference(set(list1[i])))==[]:
                        return
                list1.append(arr1)
                return

        if index<0:
            return
        self.sums(nums,index-1,c,step,arr,list1)
        if step<3:
            arr[step] = nums[index]
            self.sums(nums,index-1,c-nums[index],step+1,arr,list1)
            arr[step] = 0
    def threeSum(self, nums):
        size=len(nums)
        c=0
        arr=[0]*3
        list1 = []
        self.sums(nums,size-1,c,0,arr,list1)
        return list1


if __name__ == '__main__':
    ans=Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
)
    print ans