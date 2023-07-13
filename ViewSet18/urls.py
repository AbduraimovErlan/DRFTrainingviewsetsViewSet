from rest_framework.routers import SimpleRouter
from ViewSet18 import views



router = SimpleRouter()
router.register('books18', views.ViewSetBook18, basename='books')
urlpatterns = router.urls