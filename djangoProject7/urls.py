from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url



urlpatterns = [

    path('admin/', admin.site.urls),
    path('posting/', include('posting.urls')),
]



