from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView # new 
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # previous login view
    #path('login/', views.user_login, name='login'),
    path('custom/<int:pk>', views.custom, name='custom'), # new
    path('documentos-list', views.document_list_view), 
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)