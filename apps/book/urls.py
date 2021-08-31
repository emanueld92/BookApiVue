from rest_framework import routers
from .views import BookViewSet

routers=routers.DefaultRouter()
routers.register("book",BookViewSet)

urlpatterns = routers.urls   

