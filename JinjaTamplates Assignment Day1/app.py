from flask import Flask, render_template  # Flask와 템플릿 렌더링 모듈 임포트

app = Flask(__name__)  # Flask 애플리케이션 인스턴스 생성

# 사용자 데이터를 정의합니다.
users = [
    {"username": "traveler", "name": "Alex"},  # 첫 번째 사용자
    {"username": "photographer", "name": "Sam"},  # 두 번째 사용자
    {"username": "gourmet", "name": "Chris"}  # 세 번째 사용자
]

# 루트 URL에 대한 라우트 정의
@app.route('/')
def index():
    return render_template('index.html', users=users)  # 사용자 데이터를 템플릿에 전달

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)  # 디버그 모드로 애플리케이션 실행