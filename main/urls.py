from django.urls import path
from . import views    # import view module from current folder

urlpatterns = [
    path('<int:id>', views.index, name="index"),
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
]


