from django.urls import path
from django.views.i18n import JavaScriptCatalog
from . import views
urlpatterns = [
    path('', views.cert_list, name='cert_list'),
    path('cert/<int:pk>/', views.cert_detail, name='cert_detail'),
    path('cert/new', views.cert_new, name='cert_new'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
