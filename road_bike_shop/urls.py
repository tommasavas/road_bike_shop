"""road_bike_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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


urlpatterns = [
    path('', include('bike_store_app.urls')),
    path('login/', include('login.urls')),
    path('staffaccount/',include('staff_account.urls')), 
    path('admin/', admin.site.urls),
] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))


# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
# from bike_store_app.views import *
# from django.views.generic import RedirectView

# urlpatterns = [
#     path('',index , name = 'index'),
#     path('bike_store_app/', include('bike_store_app.urls')),
#     path('admin/', admin.site.urls),
#     path('aboutus/', about_us_view, name = 'about'),
#     path('cart/', cart_view, name = 'cart'),
#     path('order/', order_view, name = 'order'),
#     path('cart/order/<int:id>', order, name = 'order'),
#     path('cart/remove/<int:id>', remove, name = 'remove'),
#     path('login/',include('login.urls')),
#     path('description/<int:id>/', description_view, name = 'description'),
#     path('description/<int:id>/add', add, name = 'add'),
#     path('staffaccount/',include('staff_account.urls')),    
#     path('cat/<str:id>', cat, name = 'cat'),
#     path('description/<int:id>/', description_view, name = 'description'),
#     path('description/<int:id>/add', add, name = 'add'),
#     path('staffaccount/',include('staff_account.urls')),    
#     path('cat/<str:id>', cat, name = 'cat'),
#     # path('', RedirectView.as_view(url='bike_store_app/templates', permanent=True)),
# ] + (static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) +
#     static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))