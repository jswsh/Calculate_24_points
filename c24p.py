a=8
b=4
c=6
d=7

nums = [a,b,c,d]
print(nums)

#print(str(a)+","+str(b)+"," + str(c)+"," + str(d))

listNums = []

nums_arr=[]
i_count=0
for i,x1 in enumerate(nums):
    for j,x2 in enumerate(nums):
        if j==i:
            continue
        for k,x3 in enumerate(nums):
            if k==i:
                continue
            if k==j:
                continue
            for l,x4 in enumerate(nums):
                if k==l:
                    continue
                if i==l:
                    continue
                if j==l:
                    continue
                idx_arr=[i,j,k,l]
                nums_arr=[nums[i],nums[j],nums[k],nums[l]]
                i_count += 1
                #print(str(i_count) + " -- " + str(idx_arr) + ":"+str(nums_arr))
                listNums.append(nums_arr)
print(listNums) 
print(len(listNums))  
#print(listNums[0])  
#print(listNums[0][0])
for i,a in enumerate(listNums):
    x = a[0]+a[1]+a[2]+a[3]
    print(str(a) + " = " + str(x))

#listNums.append(nums)

#print(listNums)
