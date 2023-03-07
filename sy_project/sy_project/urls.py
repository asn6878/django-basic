from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('board/', include('board.urls')),
    path('polls/', include('polls.urls')),
]
