from django.contrib import admin
from django.urls import path, include

#imported views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('demo_module.urls'))
]
