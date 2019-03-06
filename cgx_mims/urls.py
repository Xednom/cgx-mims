"""cgx_mims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .routers import router

urlpatterns = [
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('cgx/', include(('cgx.urls', 'cgx'), namespace='cgx')),
    path('supply/', include('supplies.urls')),
    path('', include('web.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin Site Config
admin.sites.AdminSite.site_header = 'TSG Administration'
admin.sites.AdminSite.site_title = 'TSG Administration'
admin.sites.AdminSite.index_title = 'Home'
