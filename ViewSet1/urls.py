from ViewSet1 import views
from rest_framework.routers import DefaultRouter,SimpleRouter
router = SimpleRouter()
# register viewset with router
router.register("books1", views.ViewSetBook1, basename="books")
urlpatterns = router.urls