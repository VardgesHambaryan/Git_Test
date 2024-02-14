from django.urls import path
from .views import HomeListView
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404


urlpatterns = [
    path('' , HomeListView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        
    

handler404 = 'main.handlers.handler404'
