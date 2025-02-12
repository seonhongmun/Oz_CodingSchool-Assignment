"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('restaurants.urls')),  # restaurants 앱의 URL 패턴 포함 (루트 URL에 매핑)
    path('users/', include('users.urls')),  # 'users/' 경로에 users 앱의 urls.py 포함
    path('', include('reviews.urls')),  # 기본 경로에 reviews 앱의 urls.py 포함 (필요에 따라 다른 경로로 구성 가능)
]
