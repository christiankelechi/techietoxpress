from django.urls import path
from . import views

app_name='cpa'

urlpatterns=[
    path('index',views.index,name='index'),
    path('signup',views.SignUpView.as_view(),name='signup'),
    path('signin',views.SigninView.as_view(),name='signin')
]