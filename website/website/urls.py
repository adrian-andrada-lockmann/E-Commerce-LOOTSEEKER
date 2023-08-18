from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, help, sell, logout, login, shoppingcart,signup

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('', frontpage, name='frontpage'),    
    path('help.html', help, name='help'),
    path('sell.html', sell, name='sell'),
    path('logout.html', logout, name='logout'),
    path('shoppingcart.html', shoppingcart, name='shoppingcart.html'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
