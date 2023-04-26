"""
URL configuration for sf_sprint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .yasg import urlpatterns as doc_urls

from pereval.views import submitData

router = routers.SimpleRouter()
router.register(r'submitData', submitData, basename='submitData')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    #path('api/v1/submit-data/', SubmitDataListView.as_view(), name='submit-data-list'),
    # path('api/v1/pereval/', PerevalViewSet.as_view({'get': 'list'})),
    # path('api/v1/pereval/<int:pk>', PerevalViewSet.as_view({'put': 'update'})),
]

urlpatterns += doc_urls