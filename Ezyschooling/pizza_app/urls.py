from rest_framework.routers import DefaultRouter
from .views import PizzaView

router = DefaultRouter()

router.register('v1/pizza', PizzaView, basename='PizzaView')
urlpatterns = router.urls