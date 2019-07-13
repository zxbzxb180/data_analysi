from django.db import models

# Create your models here.


# class basic_data(models.Model):
#     year_of_project = models.CharField(max_length=10, verbose_name='项目立项年份' )
#     city = models.CharField(max_length=10, verbose_name='城市')
#     land_area = models.FloatField(verbose_name='土地面积(亩)')
#     industrial_land_expense = models.FloatField(verbose_name='工业用地费用(万/亩)')
#     commercial_land = models.FloatField(verbose_name='商业用地(万/亩)')
#     residential_land = models.FloatField(verbose_name='住宅用地(万/亩)')
#
#     class Meta:
#         db_table = 'data_analysis_test'
#         ordering = ['year_of_project']
