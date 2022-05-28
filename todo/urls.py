from django.urls import path
from todo import views

urlpatterns = [
    path('', views.hello_world),
    path('is_admin',views.is_admin),
    path('django_model_form',views.django_model_form)
]
