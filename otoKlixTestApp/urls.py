from django.urls import path
from .views import OtoKlixView

urlpatterns = [

    path('', OtoKlixView.as_view()),
    path('<int:id>', OtoKlixView.as_view())
]