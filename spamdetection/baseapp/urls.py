from baseapp import views
from django.urls import path
from .views import homePageView


urlpatterns = [
    path('',views.homePageView,name='homepage'),
    
]
