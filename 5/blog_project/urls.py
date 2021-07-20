from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
# from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'
# schema_view = get_schema_view(title=API_TITLE)
schema_view = get_swagger_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE,
                                    description=API_DESCRIPTION)),
    # path('schema/', schema_view),
    path('swagger-docs/', schema_view),

]
