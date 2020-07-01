from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='polls'),
    path('About/', views.About, name='about'),
    path('Services/', views.Services, name='services'),
    path('Contact/', views.Contact, name='contect'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]

