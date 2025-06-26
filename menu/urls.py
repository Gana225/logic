from django.urls import path
from .views import menu_list,food,order,test

urlpatterns = [
    path('api/menu/', menu_list),
    path("api/memu/",food),
    path("api/order/",order),
    path("api/test/",test)
]