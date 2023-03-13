s_input = input("请输入4个数字(1~10)，并用英文逗号分隔 :")
print(s_input)


arr_input = s_input.split(",")
print(arr_input)

if len(arr_input) != 4:
    print("输入值错误：必须是4个数字")
    exit()

bInputError = False
s_error = ""
for sin in arr_input:
    print(sin)
    if not (str(sin).strip()).isdigit():
        bInputError = True
        s_error = sin
        break

if bInputError:
    print("输入类型错误：存在非整数:"+s_error)
    exit()

a=int(arr_input[0].strip())
b=int(arr_input[1].strip())
c=int(arr_input[2].strip())
d=int(arr_input[3].strip())

'''
a=8
b=4
c=6
d=7
'''

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
#print(listNums) 
#print(len(listNums))  

for i,a in enumerate(listNums):
#for i,a in enumerate([listNums[0]]):
    s = ""
    x = 0
    
    for c1 in ["-","+","/","*"]:
        #print(c1)
        #if c==0 :
        s1 = str(a[0])+c1+str(a[1]) 
        if c1 == "-":
            x1 = a[0]-a[1]
        elif c1 == "+":
            x1 = a[0]+a[1]
        elif c1 == "/":
            x1 = a[0]/a[1]
        elif c1 == "*":
            x1 = a[0]*a[1]

        for c2 in ["-","+","/","*"]:
            #print(c2)
            #if c==0 :
            s2 = s1+c2+str(a[2]) 
            
            if c2 == "-":
                x2 = x1-a[2]
            elif c2 == "+":
                x2 = x1+a[2]
            elif c2 == "/":
                x2 = x1/a[2]
            elif c2 == "*":
                x2 = x1*a[2]

            for c3 in ["-","+","/","*"]:
                #print(c3)
                #if c==0 :
                s3 = s2+c3+str(a[3])

                if c3 == "-":
                    x3 = x2-a[3]
                elif c3 == "+":
                    x3 = x2+a[3]
                elif c3 == "/":
                    x3 = x2/a[3]
                elif c3 == "*":
                    x3 = x2*a[3]

                s = s3 + "=" +str(x3)

                if x3 == 24:
                    print(s)
                
 
         
                
    #print(s)

#listNums.append(nums)

#print(listNums)

s_exit = input("完成，按任意键推出...")
print(s_exit)