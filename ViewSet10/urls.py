from rest_framework.routers import SimpleRouter
from ViewSet10 import views




router = SimpleRouter()
router.register('books10', views.ViewSetBook10, basename='books')
urlpatterns = router.urls