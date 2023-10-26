from django.db import models

from saju.choice import SOLAR_CHOICES, SIGAN_CHOICES


# Create your models here.
class Saju(models.Model):
    #idx(필드명,컬럼명) = 자료형(속성)
    idx = models.AutoField(primary_key=True)
    #길이제한, 빈값을 허용, nulll값 허용
    name = models.CharField(max_length=30,blank=False,null=False)
    birth = models.CharField(max_length=8,blank=False,null=False)
    solar = models.CharField(choices=SOLAR_CHOICES, max_length=6, verbose_name="양력")
    sigan = models.CharField(choices=SIGAN_CHOICES, max_length=6, verbose_name="자")
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)