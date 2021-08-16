'''
编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组
.元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数
'''
'''
nums = input("请输入一些数字")
num = nums.split(" ")
num = [int(num[i]) for i in range(len(num))]

def cacluate(num):
    avg = sum(num)/len(num)
    da = []
    for i in num:
        if i>avg:
            da.append(i)
    return avg,da
print(cacluate(num))
'''
'''
编写函数, 接收一个列表和一个索引，返回这个列表中对应索引的数据，
如果索引超出范围，返回-1.
'''

nums = input("请输入一些数字")
n = input("请输入一个数字")
n = int(n)
num = nums.split(" ")
num = [int(num[i]) for i in range(len(num))]
def liesuo(num,n):
    if n >= len(num) or n<0:
        return -1
    else:
        return num[n-1]
print("列表的第",n,"个数字为",liesuo(num,n))


'''
不使用for或者while循环，
就使用方法完成1~150之间的数的打印。（方法的递归调用）
'''
'''
def digui(i):
    if i<=150:
        print(i)
        i = i+1
        digui(i)
digui(1)
'''
'''
同样使用方法的递归，求1~300所有数的和。
'''
'''
jia = 0
def diguihe(i):
    global jia
    if i<=300:
        jia = jia + i
        i = i + 1
        diguihe(i)
diguihe(1)
print("总和为：",jia)
'''
'''
用三个列表表示三门学科的选课学生姓名(一个学生可以同时选多门课)
语文 = ['小明','小张','小黄','小杨']
数学 = ['小黄','小李','小王','小杨','小周']
英语 = ['小杨','小张','小吴','小冯','小周']
1)求选课学生总共有多少人
2)求只选了第一个学科的人的数量和对应的名字
3)求只选了一门学科的学生的数量和对应的名字
'''
'''
yu = ['小明','小张','小黄','小杨']
shu = ['小黄','小李','小王','小杨','小周']
ying = ['小杨','小张','小吴','小冯','小周']
sum = yu + shu + ying
#1、求选课学生一共有多少
sum1 = []
for i in range(len(sum)):
    if sum[i] not in sum1:
        sum1.append(sum[i])
    else:
        continue
print("选课学生总共有",len(sum1),"人，分别为",sum1)

#2、
sum2 = []
for i in range(len(yu)):
    if yu[i] not in shu:
        if yu[i] not in ying:
            sum2.append(yu[i])
    else:
        continue
print("只选了第一门学科的人的数量为：",len(sum2),"名字为",sum2)

#3、
sum3 = []
for i in range(len(sum)):
    if sum.count(sum[i])==1:
        sum3.append(sum[i])
        continue
print("只选了一门学科的人的数量为",len(sum3),"名字是",sum3)
'''
'''
def daoNxN():
    for i in range(9, 0, -1):
        for j in range(1, i + 1):
            print(j, "x", i, "=", (i * j), "\t", end="")
        print()
daoNxN()
'''