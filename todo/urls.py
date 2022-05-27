from django.urls import path
from todo import views

urlpatterns = [
    path('', views.hello_world),
    path('is_admin',views.is_admin)
]
