from django.urls import path
from . import views
from blog.views import register

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/chatbot/', views.chatbot, name='chatbot'),
    path('registrar/', views.register.as_view() , name='registrar'),
]