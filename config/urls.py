"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from saju.views import home

urlpatterns = [
    path('', home, name='index'),
    path("admin/", admin.site.urls),
    path("accounts/", include('accountapp.urls')),
    path("profiles/", include('profileapp.urls')),
    path("saju/", include('saju.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 추가
# urlpatterns 에 담긴 path 들 뿐만 아니라 추가로 MEDIA_URL 과 MEDIA_ROOT 를 연결시켜
# 서버가 img 를 불러올 수 있게 되어 img 가 보이게 된다
