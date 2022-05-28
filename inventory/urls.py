from django.urls import path
from inventory import views
urlpatterns = [
    path('', views.hello_world),
]
