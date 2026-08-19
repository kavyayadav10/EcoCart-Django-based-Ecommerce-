
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path('admin/', admin.site.urls, name="admin"),
    path('', include('homepage_site.urls')),
    path("cart/", include("carts.urls")),
    path('store/', include('store.urls')),
    path('aboutus/', include('about_us_farm.urls')),
    path('account/',include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
