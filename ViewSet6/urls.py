from rest_framework.routers import SimpleRouter
from ViewSet6 import views




router = SimpleRouter()

router.register('books6', views.ViewSetBook6, basename='books')
urlpatterns = router.urls

