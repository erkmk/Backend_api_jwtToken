from django.urls import path
from django.views.generic import TemplateView

app_name = 'employees'

urlpatterns = [
    path('', TemplateView.as_view(template_name="test1/index.html")),
]