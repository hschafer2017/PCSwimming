"""pcswimming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from home import urls as home_urls
from accounts import urls as accounts_urls
from posts import urls as posts_urls
from products import urls as products_urls
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve
from django.conf import settings
from cart import urls as cart_urls
from checkout import urls as checkout_urls
from events import urls as events_urls
from alumni import urls as alumni_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls)), 
    path('accounts/', include(accounts_urls)),
    path('posts/', include(posts_urls)),
    path('products/', include(products_urls)), 
    path('cart/', include(cart_urls)),
    path('checkout/', include(checkout_urls)),
    path('events/', include(events_urls)),
    path('alumni/', include(alumni_urls)),
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT }),
    
]
