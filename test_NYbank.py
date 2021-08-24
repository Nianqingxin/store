import random
from DBUtils import update
from DBUtils import select
# 银行名
bank_name = "中国农业银行"
def welcome():
    print("-"*20+"欢迎使用中国农业银行"+"-"*20)
    print("1.开户")
    print("2.存钱")
    print("3.取钱")
    print("4.转账")
    print("5.查询")
    print("6.Bye")
    print("-" * 60)
# 银行开户逻辑
def bank_addUser(account, type, name, password, country, province, street, door,money,bank_name):
    #判断是否已满
    sql = "select count(*) from users"
    data = select(sql,[])
    if data[0] [0] >= 100:
        return 3
    #判断是否存在
    sql1 = "select * from users where account = %s"
    data1 = select(sql1,account)
    if len(data1) != 0:
        return 2
    # 正常开户
    #数据存到数据库里
    sql2 = "insert into users values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2 = [account,type,name,password,country,province,street,door,money,bank_name]
    update(sql2,param2)
    return 1
# 添加开户方法
def addUser():
    account = random.randint(10000000, 99999999)
    print("账户为:", account)
    type = int(input("请输入类型："))
    name = input("请输入用户名：")
    password = input("请输入密码：")
    country = input("请输入国家：")
    province = input("请输入省份：")
    street = input("请输入街道：")
    door = input("请输入门牌号：")
    money = int(input("请输入账户余额："))
    bank_name = "中国农业银行"
    n = bank_addUser(account,type,name,password,country,province,street,door,money,bank_name)
    if n == 1:
        print("恭喜开户成功！！！")
        print("-"*20+"账户信息"+"-"*20)
        sql1 = "select * from users where account = %s"
        data1 = select(sql1, account)
        for i in data1:
            print(i)
        print("-" * 55)
    elif n == 2:
        print("该用户已经存在！！！")
    else:
        print("该银行账户已满，不能开户")
# 存钱方法
def saveMoney():
    account = int(input("请输入账户："))
    # 判断是否存在
    sql1 = "select * from users where account = %s"
    data1 = select(sql1, account)
    if len(data1) != 0:
        money = int(input("请输入存款金额："))
        sql = "update users set money = money + %s where account = 'account'"
        param = [money]
        update(sql,param)
        print("存款成功！！！！")
    else:
        print("该账户不存在!!!!")
# 取钱方法
def withdrawMoney():
    account = int(input("请输入账户："))
    # 判断是否存在
    sql1 = "select * from users where account = %s"
    data1 = select(sql1, account)
    if len(data1) != 0:
        password = input("请输入账户密码：")
        sql2 = "select password from users where account = %s and password =%s"
        param = [account,password]
        data2 = select(sql2, param)
        if len(data2) !=0:
            money = int(input("请输入取款金额："))
            sql = "update users set money = money - %s where account = 'account'"
            param = [money]
            update(sql, param)
            print("取款成功！！！！！")
        else:
            print("用户密码不正确！！！！")
    else:
        print("该账户不存在！！！！")
# 汇率
def cost(money):
    if money <= 2000:
        return 1.6
    elif money > 2000 and money <= 5000:
        return 4
    elif money > 5000 and money <=10000:
        return 8
    elif money > 10000 and money <= 50000:
        return 12
    else:
        return money*0.3
# 转账
def transfer():
    account1 = int(input("请输入转出账户："))
    account2 = int(input("请输入转入账户："))
    # 本行转账
    sql1 = "select * from users where account = %s"

    data1 = select(sql1, account1)
    data2 = select(sql1, account2)

    if len(data1) != 0 and len(data2) != 0:
        password = input("请输入转出账户密码：")
        sql2 = "select password from users where account = %s and password =%s"
        param = [account1, password]
        data2 = select(sql2, param)
        if len(data2) != 0:
            money = int(input("请输入转出金额："))
            sql1 = "select money from users where account = %s"
            data1 = select(sql1,account1)
            if money < data1:
                sql2 = "select type from users where account = %s"
                data2 = select(sql2, account1)
                if data2 == 1 and money < 50000:
                    sql3 = "update users set money = money - %s where account = 'account1'"
                    sql4 = "update users set money = money + %s where account = 'account2'"
                    param = [money]
                    update(sql3, param)
                    update(sql4,param)
                    print("转入成功！！！！")
                elif data2 == 2 and money < 20000:
                    sql3 = "update users set money = money - %s where account = 'account1'"
                    sql4 = "update users set money = money + %s where account = 'account2'"
                    param = [money]
                    update(sql3, param)
                    update(sql4, param)
                    print("转入成功！！！！")
                else:
                    print("1.类账户:转出最大5万,2.类账户：转出最大2万")

        else:
            print("余额不足，不能转出！！！！")
    else:
        print("账户密码不正确，请重新办理业务！！！！")


# 查询
def getSelect():
    account = int(input("请输入账户："))
    sql1 = "select * from users where account = %s"
    data1 = select(sql1, account)
    if len(data1) != 0:
        password = input("请输入账户密码：")
        sql2 = "select password from users where account = %s and password =%s"
        param = [account, password]
        data2 = select(sql2, param)
        if len(data2) != 0:
            print("-" * 20 + "账户信息" + "-" * 20)
            sql3 = "select * from users where account = %s"
            data3 = select(sql3, account)
            for i in data3:
                print(i)
            print("-" * 55)
        else:
            print("密码错误!!!!")
    else:
        print("该账户不存在!!!!")

# 实现
def index():
    while True:
        welcome()
        num = input("请输入您的业务编号：")
        if num.isdigit():
            num = int(num)
            if num == 1:
                addUser()
            elif num == 2:
                saveMoney()
            elif num == 3:
                withdrawMoney()
            elif num == 4:
                transfer()
            elif num == 5:
                getSelect()
            elif num == 6:
                print("欢迎下次使用！！！")
                break
            else:
                print("输入非法字符！！！,请选择正确的业务")
        else:
            print("您输入的字符为非法！！，请输入正确的字符!!!!")
if __name__ == '__main__':
    index()



