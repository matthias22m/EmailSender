from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

urlpatterns = [
    path("api_schema/", get_schema_view(title='Api',
         description='Api Guied'), name='api_schema'),
    path('swagger-ui/', TemplateView.as_view(template_name='docs.html',extra_context = {'schema_url':'api_schema'}), name='swagger-ui'),
    path('', include('emailapp.urls')),
    # path('send-email/', send_email),
]
