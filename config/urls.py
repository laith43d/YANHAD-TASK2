"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from ninja import NinjaAPI
from commerce.controllers import commerce_controller, bonus_controller, bonus_create_controller, \
    bonus_update_controller, bonus_remove_controller

# from

api = NinjaAPI()
api.add_router('', commerce_controller)
api.add_router('getters', bonus_controller)
api.add_router('create', bonus_create_controller)
api.add_router('update', bonus_update_controller)
api.add_router('remove', bonus_remove_controller)


urlpatterns = [
    path('api/', api.urls),

    path('admin/', admin.site.urls),
]
