from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from korean_lunar_calendar import KoreanLunarCalendar

from saju import sajupyo
from saju.models import Saju


# Create your views here.
def home(request):
    return render(request, "saju/home.html")

def manselyeug(request):
    calendar = KoreanLunarCalendar()
    if request.method == "POST":
        name = request.POST.get('name')
        birth = request.POST.get('birth')
        yangeum = request.POST.get('solar')
        sigan = request.POST.get('sigan')

        # addsaju = Saju(name = name,
        #                birth = birth,
        #                solar = yangeum,
        #                sigan = sigan,
        #                )
        # addsaju.save()  # 레코드 추가

        # return HttpResponseRedirect(reverse('saju:manselyeug'))
        year = int(birth[:4])
        month = int(birth[4:6])
        day = int(birth[6:])

        if yangeum == "solar":
            calendar.setSolarDate(year, month, day)
        else:
            calendar.setLunarDate(year, month, day, False)

        yang = calendar.SolarIsoFormat()
        eum = calendar.LunarIsoFormat()

        nyeonju = calendar.getChineseGapJaString()[:2]
        wolju = calendar.getChineseGapJaString()[4:6]
        ilju = calendar.getChineseGapJaString()[8:10]

        if sigan in sajupyo.gabjapyo['Jiji']:
            ilju_cheon = calendar.getGapJaString()[8:9]
            si = sajupyo.gabjapyo['Jiji'].index(sigan)
            siju = sajupyo.sijupyo[ilju_cheon][si]
            SijuY = sajupyo.gabjapyo['CheonganYangeum'][sajupyo.gabjapyo['CheonganHanja'].index(siju[0])]
            SijuO = (sajupyo.gabjapyo['CheonganOhaeng'][sajupyo.gabjapyo['CheonganHanja'].index(siju[0])] +
                     sajupyo.gabjapyo['JijiOhaeng'][sajupyo.gabjapyo['JijiHanja'].index(siju[1])])

        else:
            siju = ""
            sijuY = ""
            sijuO = ""

        NyeonjuY = sajupyo.gabjapyo['CheonganYangeum'][sajupyo.gabjapyo['CheonganHanja'].index(nyeonju[0])]
        WoljuY = sajupyo.gabjapyo['CheonganYangeum'][sajupyo.gabjapyo['CheonganHanja'].index(wolju[0])]
        IljuY = sajupyo.gabjapyo['CheonganYangeum'][sajupyo.gabjapyo['CheonganHanja'].index(ilju[0])]

        NyeonjuO = (sajupyo.gabjapyo['CheonganOhaeng'][sajupyo.gabjapyo['CheonganHanja'].index(nyeonju[0])] +
                    sajupyo.gabjapyo['JijiOhaeng'][sajupyo.gabjapyo['JijiHanja'].index(nyeonju[1])])
        WoljuO = (sajupyo.gabjapyo['CheonganOhaeng'][sajupyo.gabjapyo['CheonganHanja'].index(wolju[0])] +
                    sajupyo.gabjapyo['JijiOhaeng'][sajupyo.gabjapyo['JijiHanja'].index(wolju[1])])
        IljuO = (sajupyo.gabjapyo['CheonganOhaeng'][sajupyo.gabjapyo['CheonganHanja'].index(ilju[0])] +
                    sajupyo.gabjapyo['JijiOhaeng'][sajupyo.gabjapyo['JijiHanja'].index(ilju[1])])


        # input_value = (name + sigan + yang + eum + siju + "시간 :" + sigan + NyeonjuY + WoljuY + IljuY + NyeonjuO + nyeonju)

        palja = NyeonjuO + WoljuO + IljuO + SijuO

        mog = palja.count("木")
        hwa = palja.count("火")
        to = palja.count("土")
        geum = palja.count("金")
        su = palja.count("水")
        saju_list = Saju.objects.all()

        input_value = ("이름 : " + name + "  양력 : " + yang + "  음력 : " + eum + "  시간 : " + sigan)
        context = {
            'input_value': input_value,
            'nyeonju' : nyeonju,
            'wolju' : wolju,
            'ilju' : ilju,
            'siju' : siju,
            'NyeonjuY' : NyeonjuY,
            'WoljuY' : WoljuY,
            'IljuY' : IljuY,
            'SijuY': SijuY,
            'NyeonjuO' : NyeonjuO,
            'WoljuO' : WoljuO,
            'IljuO' : IljuO,
            'SijuO': SijuO,
            'mog' : mog,
            'hwa' : hwa,
            'to' : to,
            'geum' : geum,
            'su' : su,
            # 'saju_list': saju_list
        }
        return render(request, 'saju/home.html', context)
        # return HttpResponseRedirect(reverse('saju/home.html'))
    else:
        saju_list = Saju.objects.all()
        return render(request, 'saju/home.html', context={'saju_list': saju_list})

def list(request):

    items = Saju.objects.order_by('name')
    #group 함수
    saju_count = Saju.objects.all().count()
    #이제 이 값을 url에 넘겨줘야지.
    return render(request, "saju/sajulist.html", {'items': items, 'address_count':saju_count})


def write(request):
    return render(request, "saju/sajuwrite.html")

# form 파라미터 처리
def insert(request):

# print("name :", request.POST['name'])
# 데이터 베이스에 입력 처리 (idx 는 Oracle의 순번과 동일)
    addsaju = Saju(name=request.POST['name'],
                birth=request.POST['birth'],
                solar=request.POST['solar'],
                sigan=request.POST['sigan'],
                   )
    addsaju.save()  # 레코드 추가

    # redirect 때는 /로 절대경로 설정해주어야함.
    return redirect("/saju/list")

def detail(request):
    idv = request.GET['idx']
    #select * from address_address where idx = idv
    addsaju = Saju.objects.get(idx=idv)
    return render(request,'saju/sajudetail.html',{'addsaju':addsaju})

@csrf_protect
def delete(request):
    idv = request.POST['idx']
    print("idx:", idv)
    # delete * from address_address where idx = idv
    # 선택한 데이터의 레코드가 삭제됨
    addsaju = Saju.objects.get(idx=idv).delete()
    return redirect('/saju/list')


# 수정 기능
@csrf_protect
def update(request):
    id = request.POST['idx']
    name = request.POST['name']
    birth = request.POST['birth']
    solar = request.POST['solar']
    sigan = request.POST['sigan']

    # print("idx:", id)
    # print("name:", name)
    # print("birth:", birth)
    # print("solar:", solar)
    # print("sigan:", sigan)

    addsaju = Saju(idx=id, name=name, birth=birth, solar=solar, sigan=sigan)
    addsaju.save()

    return redirect('/saju/list')