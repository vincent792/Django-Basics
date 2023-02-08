
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static


from users.views import(
    home,
    register,
    login,
    logout,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
