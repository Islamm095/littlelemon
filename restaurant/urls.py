#define URL route for index() view
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Menuview, BookingviewSet, SingleMenuItemView, msg
from rest_framework.authtoken.views import obtain_auth_token




router = DefaultRouter()
router.register(r'tables', BookingviewSet, basename='booking')

urlpatterns = [
    #path('', views.index, name='index'),
    path('menu/', Menuview.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
    path('restaurant/booking/', include(router.urls)),
    path('restaurant/msg', msg),
    path('api-token-auth/', obtain_auth_token)
]