"""CalculationAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from calculation_module.views import calculate_sequential, calculate_generator, calculate_comprehension, calculate_multiprocess
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculation/sequential/', calculate_sequential),
    path('calculation/generator/', calculate_generator),
    path('calculation/comprehension/', calculate_comprehension),
    path('calculation/multiprocess/', calculate_multiprocess),

]
