from flask import Flask, render_template                 # Flask 모듈에서 웹 애플리케이션 생성과 템플릿 렌더링을 위한 함수를 가져옵니다.
from flask_smorest import Api                           # Flask-Smorest를 사용하여 API를 쉽게 만들 수 있는 Api 클래스를 가져옵니다.
from flask_mysqldb import MySQL                         # Flask-MySQLdb를 통해 MySQL 데이터베이스와 연동할 수 있도록 MySQL 클래스를 가져옵니다.
import yaml                                             # YAML 형식 파일을 읽기 위해 yaml 모듈을 가져옵니다.
from posts_routes import create_posts_blueprint         # posts_routes 모듈에서 posts 블루프린트를 생성하는 함수를 가져옵니다.

app = Flask(__name__)                                   # Flask 애플리케이션 객체를 생성합니다. __name__은 현재 모듈명을 전달합니다.

db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader) # 'db.yaml' 파일을 열어 YAML 형식의 데이터베이스 설정 정보를 로드합니다.
app.config['MYSQL_HOST'] = db['mysql_host']             # 애플리케이션 설정에 MySQL 호스트 정보를 설정합니다.
app.config['MYSQL_USER'] = db['mysql_user']             # 애플리케이션 설정에 MySQL 사용자명을 설정합니다.
app.config['MYSQL_PASSWORD'] = db['mysql_password']     # 애플리케이션 설정에 MySQL 비밀번호를 설정합니다.
app.config['MYSQL_DB'] = db['mysql_db']                 # 애플리케이션 설정에 사용할 MySQL 데이터베이스 이름을 설정합니다.

mysql = MySQL(app)                                      # 설정된 애플리케이션을 이용해 MySQL 객체를 초기화합니다.

# bluepring 설정 및 등록
app.config["API_TITLE"] = "Blog API List"               # API의 제목을 설정합니다.
app.config["API_VERSION"] = "v1"                        # API의 버전을 설정합니다.
app.config["OPENAPI_VERSION"] = "3.1.3"                 # OpenAPI 스펙 버전을 설정합니다.
app.config["OPENAPI_URL_PREFIX"] = "/"                  # OpenAPI 관련 URL의 접두사를 설정합니다.
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"   # Swagger UI를 제공할 경로를 설정합니다.
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"  
# Swagger UI를 CDN을 통해 불러오기 위한 URL을 설정합니다.

api = Api(app)                                          # Flask-Smorest Api 객체를 생성하여 애플리케이션에 연결합니다.
post_blp = create_posts_blueprint(mysql)                # MySQL 객체를 인자로 받아 posts 블루프린트를 생성합니다.
api.register_blueprint(post_blp)                        # 생성된 posts 블루프린트를 API에 등록합니다.

@app.route('/blogs')                                    # '/blogs' 경로에 대한 라우트를 정의합니다.
def manage_blogs():                                     # '/blogs' 경로에 접근했을 때 실행되는 함수입니다.
    return render_template("posts.html")                # 'posts.html' 템플릿을 렌더링하여 반환합니다.

if __name__ == "__main__":                              # 이 파일이 직접 실행될 때 아래 블록을 수행합니다.
    app.run(debug=True)                                 # Flask 개발 서버를 디버그 모드로 실행합니다.