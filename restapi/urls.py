# basic Url Config
from django.urls import include,path
# import routers
from rest_framework import routers
# import everything from views
from .views import *

# define the router
routers = routers.DefaultRouter()
# define the router path and viewset to be used
routers.register(r'geeks', GeekViewSet)
# specify url path for rest_frame

urlpatterns = [
    path('', include(routers.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
