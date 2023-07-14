from rest_framework.routers import SimpleRouter
from ViewSet22 import views



router = SimpleRouter()
router.register('books22', views.ViewSetBook22, basename='books')
urlpatterns = router.urls