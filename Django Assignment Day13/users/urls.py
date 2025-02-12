# Django의 path 함수를 import합니다.
from django.urls import path  # URL 패턴 생성을 위한 path 함수 import
# 사용자 관련 뷰들을 import합니다.
from users.views import UserSignupView, UserLoginView, UserDetailView  # 사용자 뷰 import
# Django의 내장 LogoutView를 import합니다.
from django.contrib.auth.views import LogoutView  # LogoutView import

# URL 패턴 리스트 정의 시작
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),  # 'login/' 경로에 UserLoginView 연결, 이름: 'user-login'
    path('signup/', UserSignupView.as_view(), name='user-signup'),  # 'signup/' 경로에 UserSignupView 연결, 이름: 'user-signup'
    path('logout/', LogoutView.as_view(), name='user-logout'),  # 'logout/' 경로에 LogoutView 연결, 이름: 'user-logout'
    path('profile/<int:pk>/', UserDetailView.as_view(), name='user-detail'),  # 'profile/<int:pk>/' 경로에 UserDetailView 연결, 이름: 'user-detail'
]
