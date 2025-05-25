from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/pedidos/mapa/', permanent=True)),
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),
]
