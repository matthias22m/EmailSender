from django.urls import path
from .views import EmailAPIView

urlpatterns = [
    # Added our EndPoint to url patterns to wire up our API
    path('email/', EmailAPIView.as_view()),
]
