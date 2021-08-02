from django.urls import path

from accounts import views



urlpatterns = [
    # path('login', views.loginView),
    path('login/', views.loginView,name="login"),
    path('logout/', views.logoutView),
    path('profile/', views.profileView),
    # path('profileEdit', views.profileEditView),
    path('profileRegister', views.profileRegisterView)
   
]