from django.urls import path, include

from . import views
# from .views import PostDetail

urlpatterns = [
  path('', views.index, name='index'),
  path('about', views.about, name='about'),
  path('blog', views.blog, name='blog'),
  path('challenge', views.challenge, name='challenge'),
  path('contact', views.contact, name='contact'),
  path('donate', views.donate, name='donate'),
  path('getinvolved', views.getinvolved, name='getinvolved'),
  path('ourwork', views.ourwork, name='ourwork'),
  path('teams', views.teams, name='teams'),
  path('post/<id>/', views.post_details, name='post_details'),
  path('tinymce/', include('tinymce.urls'))
  # path('article/<int:pk>', PostDetail.as_view(), name='post-details'),
]