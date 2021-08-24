import xlrd
import pymysql
host = "localhost"
user = "root"
password = "123456"
database = "sales"
exit = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
wd = xlrd.open_workbook(filename=r"D:\Python自动化测试\python基础\day09【pymysql】\2020年每个月的销售情况.xlsx")
con = pymysql.connect(host=host, user=user, password=password, database=database)
cursor = con.cursor()
for i in exit:
    sql = "CREATE TABLE "+ i + "(`日期` varchar(20) DEFAULT NULL,`服装名称` varchar(20) DEFAULT NULL,`价格/件` float(10) DEFAULT NULL,`本月库存数量` float(10) DEFAULT NULL,`销售量/每日` float(10) DEFAULT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8"
    cursor.execute(sql)
    st = wd.sheet_by_name(i)
    for j in range(1,st.nrows):
        param = st.row_values(j)
        sql1 = "insert into " + i + " values(%s,%s,%s,%s,%s)"
        cursor.execute(sql1,param)
        con.commit()
cursor.close()
con.close()
print("完成导入")

