from operator import index
from django.urls import path

from authentication.views import index, logged, logout

urlpatterns = [
    path('login/', index, name='login'),
    path('logged/', logged, name='logged'),
    path('logout/', logout, name='logout')
]