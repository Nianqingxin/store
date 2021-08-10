'''
    猜数字游戏：
        1.系统随机产生一个随机数字（0~1000）
        2.用户从键盘输入数字，与随机数字进行比对 （让用户循环输入20）
            若大了：温馨提示，大了
            若小了：温馨提示，小了
            猜中
        3.循环：一直到猜中为止，退出程序。
    技术分析：
    1.随机数
        random
    2.input
    3.判断
        if ...elif ...else
    4.循环
        while : 当型循环条件型循环
    5.退出程序
        break
    任务：
        加入初始化金币功能，猜错1次扣500金币。
        猜中直接奖励10000，询问是否继续第二轮随机数猜测。

        10次没猜中，系统直接锁定。
'''
print("*"*10,"欢迎来到武魂殿大型猜数字现场","*"*10)
print("首先介绍一下规则：")
print("1、开始你有5000金魂币做赌注，需要在一至五百内猜一个数字，猜错一次扣除500金魂币，猜对一次奖励一万金魂币！")
print("2、如果猜中可选择是否要继续！")
print("3、如果超过十次没有猜中的的话，就不好意思了，直接冻结全部资金，并宣布失败！")
print("好了，规则基本上就是这样了，请开始你的表演吧！")
print("*"*30)
# 1.让系统随机产生一个随机数
import random
num = random.randint(0,500)
count = 0
# 只允许让用户输入20次
i = 1
j = 5000
while i <= 20 :
    count = count + 1
    # 2. 让用户数据
    print("你还有", j, "枚金魂币~")
    chose = input("请输入本次猜的数字：") # "123"  --> 123
    chose = int(chose)
    if chose<0 or chose>500:
        print("不遵守规则者，没收所有金魂币，并驱逐出武魂殿！！！！！")
        break
    else:
        if  j <= 0:
            print("您已经没有金魂币了，即将被武魂殿强制驱逐出去，请重新再来吧~")
            break
        elif count >= 10:
            print("猜题次数超过十次了，即将被武魂殿强制驱逐出去，请重新再来吧~")
        # 3.判断是否猜中
        elif chose > num:
            print("大了！")
            j = j - 500
        elif chose < num:
            print("小了！")
            j = j - 500
        else:
            print("恭喜，本次猜中，本次幸运数字为：",num,"，本次猜了",count,"次")
            j = j + 10000
            i = i + 1
            count = 0
            print("您的所剩金魂币为", j, "是否继续玩")
            k = input("请输入1.继续    2.退出")
            k = int(k)
            if k==1 and j==0:
                print("不好意思你没钱了，不能再玩了，再见~")
                break
            elif k == 1:
                print("好的，希望你还能继续猜中哟~")
            elif k == 2:
                print("期待下次见面哟~  Good luck~")
                break
            else:
                print("请按规则输入1/2，不要妄图破坏规则，否则将要承受武魂殿的怒火")














