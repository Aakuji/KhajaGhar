from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "KhajaGhar"
admin.site.site_title = "KhajaGhar Admin"
admin.site.index_title = "Welcome to KhajaGhar Pannel"

urlpatterns = [
    path("", include('users.urls')),
    path("", include('main.urls')),
    path("", include('products.urls')),
    # path('products/', include('products.urls')),
    # path('', include('adminspage.urls')),
    path('admins/', include('adminspage.urls')),
    path('admin/', admin.site.urls),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)