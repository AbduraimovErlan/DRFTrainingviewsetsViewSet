from rest_framework.routers import SimpleRouter
from ViewSet15 import views



router = SimpleRouter()
router.register('books15', views.ViewSetBook, basename='books')
urlpatterns = router.urls