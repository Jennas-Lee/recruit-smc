from django.contrib import admin
from django.urls import path, include

from authentication.urls import urlpatterns as authentication_urlpatterns
from check.urls import urlpatterns as check_urlpatterns
from docs.urls import urlpatterns as docs_urlpatterns
from index.urls import urlpatterns as index_urlpatterns
from info.urls import urlpatterns as info_urlpatterns
from score.urls import urlpatterns as score_urlpatterns
from recruit.urls import urlpatterns as recruit_urlpatterns

urlpatterns = [
    path('', include(index_urlpatterns)),
    path('auth/', include(authentication_urlpatterns)),
    path('check/', include(check_urlpatterns)),
    path('docs/', include(docs_urlpatterns)),
    path('info/', include(info_urlpatterns)),
    path('score/', include(score_urlpatterns)),
    path('recruit/', include(recruit_urlpatterns)),
    path('admin/', admin.site.urls),
]
