from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from djangotest import settings

urlpatterns = [
    path( 'admin/',  admin.site.urls ),
    path('',include('books.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
