from django.contrib import admin
from saju.models import Saju


# Register your models here.
class SajuAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth', 'solar', 'sigan', 'date_joined')

#디장고의 관리자모드에서 새롭게 관리될 Address, AddressAdmin을 등록한다.(ctrl+space2번)
admin.site.register(Saju,SajuAdmin)
