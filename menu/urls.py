from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import TemplateView

app_name = "menu"

urlpatterns = [
    path('',views.home,name="menu-home"),
    path('best',TemplateView.as_view(template_name="menu/template5-menu.html"),name="template-5-menu"),
    path('template5',TemplateView.as_view(template_name="menu/template5.html"),name="template-5"),
]
# path('august_cafe',views.renderTemplate,name="august-menu"),