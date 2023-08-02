from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.urls import include
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('simplify/', views.simplify, name='simplify'),
    path('quadratics/', views.generate_quadratic_equation, name='quadratics'),
    path('generate_graph/', views.generate_graph, name='generate_graph'),
    #path('matrices/', views.matrices, name='matrices'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

