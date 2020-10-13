
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Just dating API",
      default_version='v1',
      description=''' Documentation
      The `ReDoc` view can be found [here](/doc).
      The Mobile Ionic app can be found [here](/mobi).
      The Web app can be found [here](/web).
      The Admin app can be found [here](/admin).
      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zdimon77@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

from web.views import index_web, index_mobi

urlpatterns = [
    path('web/', index_web),
    path('mobi/', index_mobi),
    path('mobi/folder/Inbox', index_mobi),
    path('mobi/<slug:slug>', index_mobi),
    path('mobi/chat/<slug:slug>', index_mobi),

    

    path('v1/',include([
        path('account/',include('account.urls')),
        path('usermedia/',include('usermedia.urls')),
        path('chat/',include('chat.urls')),
        path('contact/',include('contact.urls'))
    ])),
    path('swagger/<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-doc'),
    path('admin/', admin.site.urls),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
