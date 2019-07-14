from django.shortcuts import render
from django.views import View
import pymysql
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'index.html')
#     #return HttpResponseRedirect

def save_data(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        year_of_project = request.POST.get('year_of_project')
        land_area = request.POST.get('land_area')
        industrial_land_expense = request.POST.get('industrial_land_expense')
        commercial_land = request.POST.get('commercial_land')
        residential_land = request.POST.get('residential_land')
        num_racks = request.POST.get('num_racks')
        single_stand_power = request.POST.get('single_stand_power')
        built_price = request.POST.get('built_price')
        KW_equipment_cost = request.POST.get('KW_equipment_cost')
        KW_project_cost = request.POST.get('KW_project_cost')
        final_shelving_rate = request.POST.get('final_shelving_rate')
        full_mouth_on_rack = request.POST.get('full_mouth_on_rack')
        KW_price = request.POST.get('KW_price')
        PUE = request.POST.get('PUE')
        simultaneous_coefficient = request.POST.get('simultaneous_coefficient')
        electric_charge = request.POST.get('electric_charge')
        water_charge = request.POST.get('water_charge')
        water_use_rate = request.POST.get('water_use_rate')
        broadband_rent = request.POST.get('broadband_rent')
        rack_bandwidth = request.POST.get('rack_bandwidth')
        new_people_num = request.POST.get('new_people_num')
        annual_average_wage = request.POST.get('annual_average_wage')
        wage_add_rate = request.POST.get('wage_add_rate')
        welfare_funds = request.POST.get('welfare_funds')
        low_value_consumables = request.POST.get('low_value_consumables')
        management_fee = request.POST.get('management_fee')
        depreciation_years = request.POST.get('depreciation_years')
        land_architecture = request.POST.get('land_architecture')
        equipment = request.POST.get('equipment')
        residual_rate = request.POST.get('residual_rate')
        depreciation_method = request.POST.get('depreciation_method')
        VAT_rate = request.POST.get('VAT_rate')
        electromechanical_equipment = request.POST.get('electromechanical_equipment')
        Installation_works = request.POST.get('Installation_works')
        electric_oil_VAT = request.POST.get('electric_oil_VAT')
        water_VAT = request.POST.get('water_VAT')
        company_income_tax_rate = request.POST.get('company_income_tax_rate')
        borrow_interest = request.POST.get('borrow_interest')
        borrow_years = request.POST.get('borrow_years')
        borrow_matching = request.POST.get('borrow_matching')
        borrow_poundage = request.POST.get('borrow_poundage')
        discount_rate = request.POST.get('discount_rate')
        VAT = request.POST.get('VAT')
        cabinet_rental_VAT = request.POST.get('cabinet_rental_VAT')
        bandwidth_service_VAT = request.POST.get('bandwidth_service_VAT')
        cloud_computing_service_VAT = request.POST.get('cloud_computing_service_VAT')
        VAT_supertax_rate = request.POST.get('VAT_supertax_rate')
        land_VAT = request.POST.get('land_VAT')
        construction_tax = request.POST.get('construction_tax')

        conn = pymysql.connect(
            host='localhost',
            user ='root',
            password ='123456',
            database ='data_analysis',
            charset ='utf8'
        )
        cursor = conn.cursor()
        sql = 'insert into `basic_data`(`城市`,`项目立项年份`,`土地面积(亩)`, `工业用地费用(万/亩)`, `商业用地(万/亩)`, `住宅用地(万/亩)`, `机架数量（个）`, `单机架IT功率（KW）`,  `机架总IT功率（KW）`, `建筑面积 (m2)`, `建筑物造价（元/m2)`, `单KW机电投资（万元，含税）`, `单KW机电设备建设成本（万元）`, `单KW机电工程建设成本（万元）`, `机电总投资（万元）`, `机电设备总投资（万元）`, `机电安装工程总投资（万元）`, `终局上架率`, `机架上满月数`, `单KW价格(含税，RMB/月/KW)`, `PUE`, `同时系数`, `电费（元/度, 含税)`, `水费（元/立方米）`, `耗水率`, `宽带租金（元/1G/月)`, `100M贷款租金（元/月）`, `单机架配带宽 （100M/机架，共享）`, `新增人员数量（管理+运维）`, `年人均工资（万元）`, `工资年增长率`, `职工福利费（占工资比例）`, `低值易耗品（办公用品，占职工福利费）`, `经营管理费（占营业收入）`, `固定资产折旧年限（年）`, `土地建筑 （年）`, `设备（年）`, `固定资产残值率`, `固定资产折旧方法`, `增值税税率`, `机电设备`, `安装工程`, `电，油增值税`, `水增值税`, `企业所得税率`, `借贷利息`, `贷款年限`, `贷款配比`, `贷款手续费`, `折现率`, `增值税`, `机柜租赁增值税（不动产）`, `带宽服务增值税`, `云计算服务增值税`, `增值税附加税率`, `土地增值税`, `建筑工程税费`) ' \
              'values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        values = (city, year_of_project, land_area, industrial_land_expense, commercial_land, residential_land, num_racks, single_stand_power, float(single_stand_power)*float(num_racks), float(num_racks)*10, built_price, float(KW_equipment_cost)+float(KW_project_cost), KW_equipment_cost, KW_project_cost, (float(single_stand_power)*float(num_racks))*(float(KW_equipment_cost)+float(KW_project_cost)), float(KW_equipment_cost)*float(single_stand_power)*float(num_racks), float(KW_project_cost)*float(single_stand_power)*float(num_racks), final_shelving_rate, full_mouth_on_rack, KW_price, PUE, simultaneous_coefficient, electric_charge, water_charge, water_use_rate, broadband_rent, float(broadband_rent)/10, rack_bandwidth, new_people_num, annual_average_wage, wage_add_rate, welfare_funds, low_value_consumables, management_fee, depreciation_years, land_architecture, equipment, residual_rate, depreciation_method, VAT_rate, electromechanical_equipment, Installation_works, electric_oil_VAT, water_VAT, company_income_tax_rate, borrow_interest, borrow_years, borrow_matching, borrow_poundage, discount_rate, VAT, cabinet_rental_VAT, bandwidth_service_VAT, cloud_computing_service_VAT, VAT_supertax_rate, land_VAT, construction_tax)
        cursor.execute(('TRUNCATE TABLE `basic_data`'))
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    return render(request, 'index.html')

def show_1(request):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        database='data_analysis',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = "SELECT * FROM basic_data"
    cursor.execute(sql)
    results = cursor.fetchone()
    conn.close()
    print(results)
    print(len(results))
    num_racks = int(results[6])
    final_shelving_rate = float(results[17])
    full_mouth_on_rack = int(results[18])



    return render(request, 'show_1.html', {'num_racks': num_racks,
                                           'final_shelving_rate': int(final_shelving_rate*100),
                                           'full_mouth_on_rack': full_mouth_on_rack
                                           })




def show_2(request):
    return render(request, 'show_2.html')

