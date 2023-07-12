from rest_framework.routers import SimpleRouter
from ViewSet8 import views



router = SimpleRouter()
router.register('books8', views.ViewSetBook8, basename='books')
urlpatterns = router.urls