from rest_framework.routers import SimpleRouter
from ViewSet21 import views




router = SimpleRouter()
router.register(
    'books21', views.ViewSetBook21, basename='books'
)
urlpatterns = router.urls