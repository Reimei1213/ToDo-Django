from django.urls import path

from . import views

app_name = 'todos'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:todoId>/', views.detail, name='detail'),
    path('post/', views.post, name='post'),
    path('changeStatus/', views.changeStatus, name='changeStatus'),
    path('delete/<int:todoId>/', views.delete, name='delete')
]