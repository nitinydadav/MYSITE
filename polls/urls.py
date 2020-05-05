from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('xyz/', views.index_xyz, name='index-xyx'),
    path('abc/', views.index_abc, name='index-abc'),
    path('why/', views.index_why, name='index-why'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

