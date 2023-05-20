from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view, logout_view, registration
from lms.views import home_view


urlpatterns = [
    path('login/', login_view, name='authentication'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration, name='registration'),
    path('admin/', admin.site.urls),
    path('course/', include('course.urls')),
    path('', home_view, name='home'),

]