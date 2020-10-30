from django.conf.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[  
     path('',views.home,name = 'home'),
     path('login/',views.loginPage, name="login"),
     path('register/',views.registerPage, name="register"),
     path('logout/',views.logoutUser, name="logout"),
     path('profile/', views.profile, name = 'profile'),
     path('postImage/', views.new_post, name = 'post_image'),

     
     
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)