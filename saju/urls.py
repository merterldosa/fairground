from django.urls  import path
from saju import views
from profileapp.views import ProfileCreateView, ProfileUpdateView


app_name = 'saju'

urlpatterns = [
    path('', views.home),
    path('manselyeug', views.manselyeug, name='manselyeug'),
    path('list', views.list, name='list'),
    path('write', views.write, name='write'),
    path('insert', views.insert, name='insert'),
    path('detail', views.detail, name='detail'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]