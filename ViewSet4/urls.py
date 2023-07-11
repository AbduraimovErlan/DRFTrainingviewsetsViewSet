from rest_framework.routers import SimpleRouter
from ViewSet4 import views



router = SimpleRouter()
router.register('books4', views.ViewSetBook4, basename='books')
urlpatterns = router.urls