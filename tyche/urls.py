"""tyche URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path
from tyche_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.about, name="about"),
    path("budgeting", views.budgeting, name="budgeting"),
    path("credit-cards", views.credit_cards, name="credit-cards"),
    path("compound-calculator", views.compound_calculator, name="compound-calculator"),
    path("emergency-fund", views.emergency_fund, name="emergency-fund"),
    path("mortgages", views.mortgages, name="mortgages"),
    path("pensions", views.pensions, name="pensions"),
]

