from threading import Thread
import time
bread = 0
num = 0
money = 300
lan = 0
lannum = 0
class Cooker(Thread):
    username = ""

    def run(self) -> None:
        global bread,num
        while True:
            if bread < 100:
                bread = int(bread) + 1
                num = num +1
                print(self.username,"已经做了",num,"个面包！")
            else:
                time.sleep(2)
                if bread >100:
                    break
class Guker(Thread):
    username = ""

    def run(self) -> None:
        global bread,num,money,lan,lannum
        while True:
            if bread > 0:
                bread = bread - 1
                num = num +1
                money = money -2.5
                lan = lan+1

                if money<0:
                    print("您已经没钱了!!")
                    break
                elif lan >=100:
                    print("您已经装满一个篮子了！！")
                    lannum = lannum + 1
                    lan = 0
                else:
                    print(self.username, "已经抢了", num, "个面包！","花了",money,"元","篮子还能盛",500-lan,"个面包！！已经装了",lannum,"个篮子的面包了")
            else:
                time.sleep(3)
a1 = Cooker()
a2 = Cooker()
a3 = Cooker()
b1 = Guker()
b2 = Guker()
b3 = Guker()
b4 = Guker()
b5 = Guker()
b6 = Guker()

a1.username = "A1"
a2.username = "A2"
a3.username = "A3"
b1.username = "B1"
b2.username = "B2"
b3.username = "B3"
b4.username = "B4"
b5.username = "B5"
b6.username = "B6"

a1.start()
a2.start()
a3.start()
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()