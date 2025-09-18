from django.contrib import admin
from django.urls import path
from .views import CardCreateView, CardDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/', CardCreateView.as_view(), name='card-create'),
    path('card/<str:id>/', CardDetailView.as_view(), name='card-detail')
]
