# DRF의 제네릭 뷰를 사용하기 위해 import합니다.
from rest_framework import generics  # DRF의 generics 모듈 import
from rest_framework.permissions import AllowAny
# APIView를 사용하기 위해 import합니다.
from rest_framework.views import APIView  # DRF의 APIView import
# Response 객체를 사용하기 위해 import합니다.
from rest_framework.response import Response  # 응답 객체 Response import
# HTTP 상태 코드를 사용하기 위해 import합니다.
from rest_framework import status  # HTTP 상태 코드를 위한 모듈 import
# Django의 로그인 기능을 사용하기 위해 import합니다.
from django.contrib.auth import login  # Django의 login 함수 import
# 현재 활성 사용자 모델을 가져오기 위해 import합니다.
from django.contrib.auth import get_user_model  # 사용자 모델 가져오기 함수 import
# 사용자 관련 시리얼라이저들을 import합니다.
from users.serializers import UserSerializer, UserLoginSerializer, UserDetailSerializer  # 시리얼라이저 import

# 현재 활성 사용자 모델을 User 변수에 할당합니다.
User = get_user_model()  # 사용자 모델 할당

# UserSignupView 정의 (회원가입 APIView)
class UserSignupView(generics.CreateAPIView):  # CreateAPIView 상속받아 회원가입 뷰 정의
    permission_classes = [AllowAny]
    serializer_class = UserSerializer  # 회원가입 시 사용할 시리얼라이저를 UserSerializer로 지정
    # permission_classes는 기본적으로 모든 사용자에게 접근을 허용 (AllowAny)

# UserLoginView 정의 (로그인 APIView)
class UserLoginView(APIView):  # APIView 상속받아 로그인 뷰 정의
    permission_classes = [AllowAny]
    # permission_classes는 기본적으로 모든 사용자에게 접근을 허용 (AllowAny)
    def post(self, request, *args, **kwargs):  # POST 요청 처리 메서드 정의
        serializer = UserLoginSerializer(data=request.data)  # 요청 데이터를 바탕으로 UserLoginSerializer 인스턴스 생성
        if serializer.is_valid():  # 시리얼라이저의 데이터가 유효한지 검증
            user = serializer.validated_data.get('user')  # 검증된 사용자 객체 추출
            login(request, user)  # Django의 login 함수를 사용하여 사용자 로그인 수행
            return Response({'message': '로그인 성공'}, status=status.HTTP_200_OK)  # 성공 메시지와 200 상태 반환
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 오류 발생 시 400 상태 반환

# UserDetailView 정의 (사용자 상세 조회, 수정, 삭제 APIView)
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):  # RetrieveUpdateDestroyAPIView 상속받아 뷰 정의
    serializer_class = UserDetailSerializer  # 사용자 상세 정보 시리얼라이저 지정
    queryset = User.objects.all()  # 모든 사용자에 대한 쿼리셋 지정
    def get_object(self):  # 객체를 반환하는 메서드 오버라이드
        return self.request.user  # 로그인된 사용자만 자신의 정보를 조회, 수정, 삭제하도록 반환
