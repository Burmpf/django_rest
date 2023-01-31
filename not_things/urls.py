from django.urls import path
from .views import Not_Thinglist, Not_Thingdetail


urlpatterns = [
    path('', Not_Thinglist .as_view(), name='not_thing_list'),
    path('<int:pk> /', Not_Thingdetail .as_view(), name='not_thing_detail'),
]
