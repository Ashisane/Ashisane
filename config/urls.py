from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base.html"), name='home'),
    path('home/', TemplateView.as_view(template_name="base.html"), name='home'),
    path('tools/', include('tools.urls')),
    path('games/', include('games.urls')),
    path('projects/', include('projects.urls')),
]
