import pymysql
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "data_analysis", charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM basic_data"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchone()
    print(results)
    print(len(results))

    num_racks = float(results[6])
    final_shelving_rate = float(results[17])
    full_mouth_on_rack = float(results[18])
    # 打印结果
    print(num_racks, final_shelving_rate, full_mouth_on_rack)
    # print(results)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()


