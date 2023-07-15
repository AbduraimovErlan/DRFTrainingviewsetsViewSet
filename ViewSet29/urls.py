from rest_framework.routers import SimpleRouter
from ViewSet29 import views



router = SimpleRouter()
router.register('books29', views.ViewSetBook29, basename='books')
urlpatterns = router.urls