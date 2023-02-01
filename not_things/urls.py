from django.urls import path
from .views import Not_ThingList, Not_ThingDetail


urlpatterns = [
    path('', Not_ThingList.as_view(), name='not_thing_list'),
    path('<int:pk>/', Not_ThingDetail.as_view(), name='not_thing_detail'),
]
