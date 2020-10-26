from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.home, name='index'),
    path('postImage/', views.new_post, name = 'post_image'),
    path('profile/', views.profile, name = 'profile')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
