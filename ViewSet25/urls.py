from rest_framework.routers import SimpleRouter
from ViewSet25 import views



router = SimpleRouter()
router.register('books25', views.ViewSetBook25, basename='books')
urlpatterns = router.urls