from django.urls import path

from . import views
from .views import SentenceView

urlpatterns = [
    path('', SentenceView.as_view()),
]