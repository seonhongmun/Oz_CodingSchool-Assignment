from flask import Flask  # Flask 클래스를 flask 패키지에서 임포트하여 Flask 애플리케이션 인스턴스를 생성합니다.
from flask_smorest import Api  # flask_smorest 패키지에서 Api 클래스를 임포트하여 API 구성을 관리합니다.
from api import book_blp  # api 모듈에서 book_blp 블루프린트를 임포트합니다.

app = Flask(__name__)  # Flask 애플리케이션의 인스턴스를 생성합니다.
app.config['API_TITLE'] = 'Book API'  # Flask-Smorest API의 제목을 'Book API'로 설정합니다.
app.config['API_VERSION'] = 'v1'  # Flask-Smorest API의 버전을 'v1'로 설정합니다.
app.config['OPENAPI_VERSION'] = '3.0.2'  # OpenAPI 스펙의 버전을 '3.0.2'로 설정합니다.
app.config["OPENAPI_URL_PREFIX"] = "/"  # OpenAPI 문서의 URL 프리픽스를 '/'로 설정합니다.
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/UI"  # Swagger UI가 '/UI' 경로에서 접근 가능하도록 설정합니다.

app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  
# Swagger UI 리소스를 CDN에서 불러옵니다.

api = Api(app)  # Api 객체를 생성하고 Flask 애플리케이션과 연동합니다.
api.register_blueprint(book_blp)  # 임포트한 book_blp 블루프린트를 Api 객체에 등록하여 API에 포함시킵니다.

if __name__ == '__main__':
    app.run(debug=True)  # Flask 애플리케이션을 디버그 모드로 실행합니다.