from rest_framework.routers import SimpleRouter
from ViewSet20 import views



router = SimpleRouter()
router.register('books20', views.ViewSetBook20, basename='books')
urlpatterns = router.urls