from django.urls import path

from . import views

app_name = 'courtdata'
urlpatterns = [

    path('<int:courtcase_id>', views.display, name='output'),
]
