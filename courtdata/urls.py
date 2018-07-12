from django.urls import path

from . import views

urlpatterns = [

    path('<int:courtcase_id>', views.output, name='output')
]
