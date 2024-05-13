from django.urls import path, include
from rest_framework import routers #routers toma todas las vistas y genera las urls automaticamente
from tasks import views
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskView, 'tasks')

urlpatterns = [
    path("api/v1/", include(router.urls)), #obtiene todas las urls generadas por router
    path("docs/", include_docs_urls(title="Tasks API"))
]