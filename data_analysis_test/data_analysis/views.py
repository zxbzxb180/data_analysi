from django.shortcuts import render
from django.views import View
import pymysql

# Create your views here.
def index(request):
    return render(request, 'index.html')

def save_data(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        year_of_project = request.POST.get('year_of_project')
        land_area = request.POST.get('land_area')
        industrial_land_expense = request.POST.get('industrial_land_expense')
        commercial_land = request.POST.get('commercial_land')
        residential_land = request.POST.get('residential_land')
    conn = pymysql.connect(
        host='localhost',
        user ='root',
        password ='123456',
        database ='data_analysis',
        charset ='utf8'
    )
    cursor = conn.cursor()
    sql = 'insert into `basic_data`(`城市`,`项目立项年份`,`土地面积(亩)`, `工业用地费用(万/亩)`, `商业用地(万/亩)`, `住宅用地(万/亩)`) values(%s,%s,%s,%s,%s,%s)'
    values = (city, year_of_project, land_area, industrial_land_expense, commercial_land, residential_land)
    cursor.execute(sql, values)
    conn.commit()

    return render(request, 'index.html')

