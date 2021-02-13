
from django.contrib import admin
from django.urls import path,include
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,{'check':'OK'}, name="home"),
    path('student/', include('enroll.urls')),
]
