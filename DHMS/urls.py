from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.homepage),
    path('about', views.about),
    path('blog',views.blog),
    path('contact',views.Contact),
    path('feature',views.Feature),
    path('service',views.Service),
    path('appointment',views.Appointment),
]

