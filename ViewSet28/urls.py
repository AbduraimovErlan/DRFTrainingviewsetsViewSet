from rest_framework.routers import SimpleRouter
from ViewSet28 import views



router = SimpleRouter()
router.register('books28', views.ViewSetBook28, basename='books')
urlpatterns = router.urls