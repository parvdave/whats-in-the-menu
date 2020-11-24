from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.home,name="menu-home"),
    # path('august_cafe',views.renderTemplate,name="august-menu"),
    path('template5',TemplateView.as_view(template_name="menu/template5.html"),name="template-5"),
]
