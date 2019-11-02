from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import view,function
 
urlpatterns = [
    path('', function.home),
    path('count/', function.count),
    path('about/', function.about),

]

# 在这里增加--path(get路径,view匹配要返回的项）