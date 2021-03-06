from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('a/', admin.site.urls),
    path('', include('blog.urls')),
    path("api/", include("blog.api.urls")),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
]

urlpatterns += doc_urls


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))

    ]+urlpatterns

urlpatterns += static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
