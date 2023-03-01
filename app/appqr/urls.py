from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('img/<int:id>', ImageShow, name='imageshow'),
    path('img_edit/<int:id>', ImageEdite, name='imageedit'),
    path('list', ImageList, name='imagelist'),
    path('register', Register, name='register'),
    path('login', Login, name='login'),
    path('logout', Logout, name='logout'),
    path('', QrCreateView, name='imagecreate'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)