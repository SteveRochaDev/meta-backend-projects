from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView

from menu.views import MenuItemViewSet
from bookings.views import BookingViewSet

router = DefaultRouter()
router.register(r'api/menu', MenuItemViewSet)
router.register(r'api/bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # HTML Pages
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('menu/', TemplateView.as_view(template_name='menu.html')),
    path('book/', TemplateView.as_view(template_name='book.html')),
    
    # API
    path('', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]