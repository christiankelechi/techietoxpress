from django.urls import path
from . import views

app_name='blog'
urlpatterns=[
    path('list',views.postlist,name='list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]