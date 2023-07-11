from rest_framework.routers import SimpleRouter
from ViewSet7 import views



router = SimpleRouter()
router.register('books7', views.ViewSetBook7, basename='books7')
urlpatterns = router.urls