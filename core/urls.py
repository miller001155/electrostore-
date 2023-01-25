from rest_framework.routers import DefaultRouter

from clients.api.v1.views.balance_view import BalanceViewSet
from clients.api.v1.views.client_view import ClientViewSet
from product.api.v1.views.category_view import CategoryViewSet
from product.api.v1.views.product_view import ProductViewSet
from product.api.v1.views.raiting_view import RaitingViewSet
from suppliers.api.v1.views.supplier_view import SupplierViewSet

router = DefaultRouter()

router.register(r'balance', BalanceViewSet)
router.register(r'client', ClientViewSet)
router.register(r'product', ProductViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'raiting', RaitingViewSet)
router.register(r'suppliers', SupplierViewSet)


urlpatterns = router.urls