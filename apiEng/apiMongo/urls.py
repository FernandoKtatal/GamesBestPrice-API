from django.conf.urls import url
from rest_framework_mongoengine import routers
from .views import GameViewSet, index

routers = routers.DefaultRouter()
routers.register(r'games', GameViewSet, base_name='game')

urlpatterns = [
    url(r'^$', index),
]

urlpatterns += routers.urls

# gerencia as urls do aplicativo, eh pra ca que foi redirecionado....
# api entre app e bd