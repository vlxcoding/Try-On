from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventory/', include('inventory.urls')),
    # path('customer_support/', include('customer_support.urls')),

]