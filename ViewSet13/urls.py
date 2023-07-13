from rest_framework.routers import SimpleRouter
from ViewSet13 import views



router = SimpleRouter()
router.register(
    'books13', views.ViewSetBook13, basename='books'
)

urlpatterns = router.urls