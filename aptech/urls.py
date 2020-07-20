
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Accounts import views as account_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainsite.urls')),
    path('register/', account_views.register, name='register'),
    path('login/', account_views.loginPage, name='loginpage'),
    path('logout/', account_views.logoutUser, name='logout'),
    path('accounts/', include("allauth.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
