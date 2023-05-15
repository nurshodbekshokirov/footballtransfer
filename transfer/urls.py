
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', about),
    path('club/', club),
    path('player/', player),
    path('latest-transfers/', latest_transfer),
    path('countries/<str:soz>/', davlat),
    path('mavsum/<str:soz>/', bitta_mavsum),
    path('playeru20/', u20),
    path('stats/', stats),
    path('transfer_record/', transfer_record),
    path('transfer-archive/', arxive),
    path('clubs/<int:son>/', bitta_club),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
