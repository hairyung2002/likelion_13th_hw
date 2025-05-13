from django.urls import path
from users.views import *
from django.conf import settings
from django.conf.urls.static import static

app_name="users"

urlpatterns = [
    path('mypage/<int:id>', mypage, name="mypage"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)