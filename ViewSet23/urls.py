from rest_framework.routers import SimpleRouter
from ViewSet23 import views



router = SimpleRouter()
router.register('books23', views.ViewSetBook23, basename='books')
urlpatterns = router.urls