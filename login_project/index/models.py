from django.db import models
# Create your models here.


class Type(models.Model):
    id = models.AutoField(' 序号 ', primary_key=True)
    type_name = models.CharField(' 产品类型 ', max_length=20)
    # 设置返回值，若不设置，则默认返回Type对象
    # 如果存在多个下拉框，需要重写初始化函数__init__()

    def __str__(self):
        return self.type_name


# 设置中文
# 设置字段中文名，用于admin后天显示
class Product(models.Model):
    id = models.AutoField(' 序号 ', primary_key=True)
    name = models.CharField(' 名称 ', max_length=50)
    weight = models.CharField(' 重量 ', max_length=20)
    price = models.CharField(' 价格 ', max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name=' 产品类型 ')

    class Meta:
        # 设置verbose_name，在Admin会显示为'产品信息s'
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'

