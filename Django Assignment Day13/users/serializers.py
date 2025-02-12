# DRF의 serializers 모듈을 import합니다.
from rest_framework import serializers  # DRF의 serializers 모듈 import
# 현재 활성 사용자 모델을 가져오기 위해 get_user_model 함수를 import합니다.
from django.contrib.auth import get_user_model  # 사용자 모델 가져오기 함수 import

# 현재 활성 사용자 모델을 User 변수에 할당합니다.
User = get_user_model()  # 사용자 모델 할당

# UserSerializer 정의 (회원가입용)
class UserSerializer(serializers.ModelSerializer):  # ModelSerializer 상속받아 UserSerializer 정의
    class Meta:  # Meta 클래스 시작
        model = User  # 시리얼라이저에서 사용할 모델 지정
        fields = ('id', 'nickname', 'email', 'password', 'is_staff', 'is_superuser')  # 사용할 필드 지정
    def create(self, validated_data):  # 회원가입 시 객체 생성을 위한 create 메서드 오버라이드
        # 사용자 인스턴스를 생성 (비밀번호는 set_password로 처리)
        user = User(  # 사용자 인스턴스 생성 시작
            email=validated_data.get('email'),  # 이메일 필드 설정
            nickname=validated_data.get('nickname')  # 닉네임 필드 설정
            # is_staff, is_superuser는 필요에 따라 추가적으로 설정할 수 있음
        )
        user.set_password(validated_data.get('password'))  # 비밀번호를 해시 처리하여 설정
        user.save()  # 데이터베이스에 사용자 저장
        return user  # 생성된 사용자 인스턴스 반환

# UserDetailSerializer 정의 (회원 정보 조회/수정용)
class UserDetailSerializer(serializers.ModelSerializer):  # ModelSerializer 상속받아 UserDetailSerializer 정의
    class Meta:  # Meta 클래스 시작
        model = User  # 시리얼라이저에서 사용할 모델 지정
        fields = ('id', 'nickname', 'email', 'password', 'profile_image')  # 사용할 필드 지정
        read_only_fields = ('id', 'nickname')  # id와 nickname은 읽기 전용으로 설정
        extra_kwargs = {  # 추가 옵션 설정 시작
            'password': {'write_only': True}  # 비밀번호는 쓰기 전용으로 설정 (클라이언트에 노출하지 않음)
        }
    def update(self, instance, validated_data):  # 업데이트 시 호출되는 update 메서드 오버라이드
        if 'password' in validated_data:  # 만약 비밀번호가 업데이트 데이터에 포함되면
            instance.set_password(validated_data.pop('password'))  # set_password로 비밀번호 업데이트 후 해당 데이터 제거
        for attr, value in validated_data.items():  # 나머지 필드에 대해 반복 처리
            setattr(instance, attr, value)  # 인스턴스의 해당 속성을 업데이트
        instance.save()  # 변경사항을 데이터베이스에 저장
        return instance  # 업데이트된 인스턴스 반환

# UserLoginSerializer 정의 (로그인 시 데이터 검증용)
class UserLoginSerializer(serializers.Serializer):  # 기본 Serializer 상속받아 UserLoginSerializer 정의
    email = serializers.EmailField(required=True)  # 이메일 필드를 필수로 설정
    password = serializers.CharField(required=True, write_only=True)  # 비밀번호 필드를 필수 및 쓰기 전용으로 설정
    def validate(self, attrs):  # 전체 데이터 검증 메서드 오버라이드
        email = attrs.get('email')  # 요청 데이터에서 이메일 추출
        password = attrs.get('password')  # 요청 데이터에서 비밀번호 추출
        # Django의 authenticate 함수를 사용하여 사용자 인증 시도
        from django.contrib.auth import authenticate  # authenticate 함수 import
        user = authenticate(email=email, password=password)  # 이메일과 비밀번호로 사용자 인증 수행
        if not user:  # 인증 실패 시
            raise serializers.ValidationError('유효하지 않은 이메일 또는 비밀번호입니다.')  # 검증 실패 에러 발생
        attrs['user'] = user  # 검증된 사용자 객체를 attrs에 추가
        return attrs  # 검증된 데이터 반환
