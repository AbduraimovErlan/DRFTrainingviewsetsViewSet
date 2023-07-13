from rest_framework.routers import SimpleRouter
from ViewSet17 import views



router = SimpleRouter()
router.register(
    'books17', views.ViewSetBook17, basename='books'
)
urlpatterns = router.urls