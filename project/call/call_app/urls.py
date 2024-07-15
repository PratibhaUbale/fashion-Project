
from django.urls import path
from call_app import views
urlpatterns = [
    path('about',views.About),
    path('home',views.Home),
    # path('hello',views.hello),
    path('create',views.create),
    path('',views.dashboard)
]


