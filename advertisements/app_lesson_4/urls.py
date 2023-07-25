from django.urls import path
from .views import index_0, index_DZ_4

urlpatterns = [
    path('', index_0),
    path('lesson-4/', index_DZ_4)
]