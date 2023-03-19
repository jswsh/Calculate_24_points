
if __name__=="__main__":
    #设置计算目标：24
    TARGET_NUM = 24

    ''' 默认的abcd4个数字，在debug模式下，可以用于测试计算 '''
    a=1
    b=4
    c=6
    d=2
    
    # a=1
    # b=4
    # c=4
    # d=2
    
    DEBUG_MODE = True
    if not DEBUG_MODE: #在非调试，即正常运行模式下时，需要用户输入4个整数
        #要求输入
        s_input = input("请输入4个数字(1~10)，并用英文逗号分隔 :")
        #转换为[]
        arr_input = s_input.split(",")
        #print(arr_input)
        #输入合法性检查
        if len(arr_input) != 4: #检查是4个
            print("输入值错误：必须是4个数字")
            exit()
        #检查必须为整数
        bInputError = False
        s_error = ""
        for sin in arr_input:
            if not (str(sin).strip()).isdigit():
                bInputError = True
                s_error = sin
                break

        if bInputError:
            print("输入类型错误：存在非整数:"+s_error)
            exit()

        #数字赋值
        a=int(arr_input[0].strip())
        b=int(arr_input[1].strip())
        c=int(arr_input[2].strip())
        d=int(arr_input[3].strip())
 

    #参与计算数字赋值[]，并打印出来
    nums = [a,b,c,d]
    print(nums)

    listNumsTemp = []
    listNums = []

    nums_arr=[]
    i_count=0
    for i,x1 in enumerate(nums): #从第一个数开始循环
        for j,x2 in enumerate(nums): #计算式的第二个数轮流换（除第一个数外，每个数字只能用一次）
            if j==i:
                continue
            for k,x3 in enumerate(nums): #计算式的第三个数轮流换（与第一、第二重复的数除外）
                if k==i:
                    continue
                if k==j:
                    continue
                for l,x4 in enumerate(nums):#计算式的第四个数轮流换（与第一、第二、第三重复的数除外）
                    if k==l:
                        continue
                    if i==l:
                        continue
                    if j==l:
                        continue
                    idx_arr=[i,j,k,l]
                    nums_arr=[nums[i],nums[j],nums[k],nums[l]]
                    i_count += 1
                    listNumsTemp.append(nums_arr)
                    # listNums.append(nums_arr)
                    #打印出组合出来的数字计算顺序
                    # if DEBUG_MODE:
                    #     print(str(i_count) + " -- " + str(idx_arr) + ":"+str(nums_arr))
    
    print("--------------------------------")
    
    for arr_n in (listNumsTemp):
        if arr_n not in listNums:
            listNums.append(arr_n)
            print(arr_n)
            
    print("--------------------------------")
                    
    #print(listNums)  #print(len(listNums)) 
    # 指定特殊数字，调试用
    #listNums.clear()
    #listNums.append([4,1,2,6]) 

    #for i,a in enumerate([listNums[0]]): #测试用，注释掉
    for i,a in enumerate(listNums):
        #初始化算式描述字符串s和最终计算结果x
        s = "" 
        x = 0
        
        for c1 in ["-","+","/","*"]:
            #print(c1)
            #if c==0 :
            if c1 == "-":
                x1 = a[0]-a[1]
            elif c1 == "+": 
                x1 = a[0]+a[1]
            elif c1 == "/" and a[1] != 0:
                x1 = a[0]/a[1]
            elif c1 == "*":
                x1 = a[0]*a[1]

            s1 = str(a[0])+c1+str(a[1]) #算式12项
            if c1 == "-" or c1 == "+": #加上括号
                s1 = "(" + s1 + ")"

            #直接 1->2->3->4顺序计算
            for c2 in ["-","+","/","*"]:
                #print(c2)
                #if c==0 :
                s2 = s1+c2+str(a[2]) 
                
                if c2 == "-":
                    x2 = x1-a[2]
                elif c2 == "+":
                    x2 = x1+a[2]
                elif c2 == "/" and a[2] != 0:
                    x2 = x1/a[2]
                elif c2 == "*":
                    x2 = x1*a[2]

                for c3 in ["-","+","/","*"]:
                    #print(c3)
                    #if c==0 :
                    s3 = s2+c3+str(a[3])

                    if c3 == "-":
                        x = x2-a[3]
                    elif c3 == "+":
                        x = x2+a[3]
                    elif c3 == "/" and a[3] != 0:
                        x = x2/a[3]
                    elif c3 == "*":
                        x = x2*a[3]

                    s = s3 + "=" +str(x)

                    if x3 == TARGET_NUM:
                        print(s)

            #计算后两位先运算的情况 1->2->(3->4)
            for c2 in ["-","+","/","*"]:
                for c3 in ["-","+","/","*"]:
                    if c3 == "-":
                        x4 = a[2]-a[3]
                    elif c3 == "+":
                        x4 = a[2]+a[3]
                    elif c3 == "/" and a[3] != 0:
                        x4 = a[2]/a[3]
                    elif c3 == "*":
                        x4 = a[2]*a[3]
                    s4 =  str(a[2])+c3+str(a[3])  #算式34项 
                    if c3 == "-" or c3 == "+": #加上括号
                        s4 = "(" + s4 + ")"
                
                    if c2 == "-":
                        x = x1-x4
                    elif c2 == "+":
                        x = x1+x4
                    elif c2 == "/"  and x4 != 0:
                        x = x1/x4
                    elif c2 == "*":
                        x = x1*x4

                    s5 = s1+c2+s4
                    s = s5 + "=" +str(x)
                    if x == TARGET_NUM:
                            print(s)


    #listNums.append(nums)
    #print(listNums)

    s_exit = ""
    s_exit = input("完成，按任意键推出...")
    print(s_exit)