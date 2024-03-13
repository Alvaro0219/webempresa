from django.contrib import admin
from django.urls import path, include 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('pages/', include('pages.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
