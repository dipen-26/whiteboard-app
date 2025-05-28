from django.urls import path
from .views import RegisterView, OwnerOnlyView, EditorOnlyView, ViewerOnlyView, SecureView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('owner/', OwnerOnlyView.as_view(), name='owner'),
    path('editor/', EditorOnlyView.as_view(), name='editor'),
    path('viewer/', ViewerOnlyView.as_view(), name='viewer'),
    path('secure/', SecureView.as_view(), name='secure'),
]
