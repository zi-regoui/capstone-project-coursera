from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken'))
]