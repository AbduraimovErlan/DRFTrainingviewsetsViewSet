from rest_framework.routers import SimpleRouter
from ViewSet14 import views


router = SimpleRouter()
router.register('books14', views.ViewSetBook14, basename='books')
urlpatterns = router.urls