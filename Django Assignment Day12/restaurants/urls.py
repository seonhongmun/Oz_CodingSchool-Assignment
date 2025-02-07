from rest_framework.routers import DefaultRouter  # DRF의 DefaultRouter 임포트
from restaurants.views import RestaurantViewset  # RestaurantViewset 임포트

router = DefaultRouter()  # DefaultRouter 인스턴스 생성
router.register(r'restaurants', RestaurantViewset, basename='restaurant')  # 'restaurants' 엔드포인트에 뷰셋 등록

urlpatterns = router.urls  # 라우터에서 생성된 URL 패턴을 urlpatterns에 할당
