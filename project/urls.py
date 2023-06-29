from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home,name="home"),
    path('user_authentication/', include('user_authentication.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
]
