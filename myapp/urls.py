from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('google_bard_response/', views.google_bard_response),
    path('admin/', admin.site.urls),

    # path('counter', views.counter, name='counter'),
    # path('about-us', views.about_us, name='counter')
]
