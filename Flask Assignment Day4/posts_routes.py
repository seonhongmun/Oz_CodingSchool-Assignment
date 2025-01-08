from flask import request, jsonify                          
from flask_smorest import Blueprint, abort                  
# Flask의 request와 jsonify, Flask-Smorest의 Blueprint와 abort 함수를 가져옵니다.

def create_posts_blueprint(mysql):                         
    # MySQL 객체를 인자로 받아 posts 관련 블루프린트를 생성하는 함수를 정의합니다.
    
    posts_blp = Blueprint("posts", __name__,               
                        description='posts api',         
                        url_prefix='/posts')               
    # "posts"라는 이름의 블루프린트를 생성하고, '/posts' URL 접두사를 설정합니다.

    @posts_blp.route('/', methods=["GET", "POST"])          
    def posts():
        # '/posts/' 경로에 대해 GET과 POST 요청을 처리하는 핸들러를 정의합니다.
        
        cursor = mysql.connection.cursor()                  
        # MySQL 데이터베이스와 통신하기 위한 커서를 생성합니다.
        
        # 게시글 조회
        if request.method == 'GET':                         
            # GET 요청 시 모든 게시글을 조회합니다.
            
            sql = "SELECT * FROM posts"                     
            cursor.execute(sql)                             
            # 모든 게시글을 선택하는 SQL 쿼리를 실행합니다.

            posts = cursor.fetchall()                       
            # 쿼리 결과로 모든 게시글 데이터를 가져옵니다.
            
            cursor.close()                                  
            # 데이터베이스 커서를 닫습니다.

            post_list = []                                  
            # 결과를 저장할 리스트를 초기화합니다.
            
            for post in posts:                              
                # 가져온 각 게시글에 대해 반복합니다.
                
                post_list.append({                          
                    'id': post[0],                         
                    'title': post[1],                      
                    'content': post[2]                     
                })
                # 각 게시글의 ID, 제목, 내용을 딕셔너리로 변환하여 리스트에 추가합니다.

            return jsonify(post_list)                       
            # 게시글 목록을 JSON 형태로 반환합니다.
        
        # 게시글 생성
        if request.method == "POST":                        
            # POST 요청 시 새로운 게시글을 생성합니다.
            
            title = request.json.get('title')               
            content = request.json.get('content')           
            # 요청 본문에서 제목과 내용을 가져옵니다.

            if not title or not content:                    
                abort(400, message="제목이나 내용은 비어 있을 수 없습니다.")  
                # 제목이나 내용이 없으면 400 오류와 함께 메시지를 반환합니다.

            sql = "INSERT INTO posts(title, content) VALUES(%s, %s)" 
            cursor.execute(sql, (title, content))           
            # 새로운 게시글을 데이터베이스에 삽입하는 SQL 쿼리를 실행합니다.

            mysql.connection.commit()                       
            # 데이터베이스에 변경 사항을 커밋합니다.

            return jsonify({                                 
                'msg': '게시글이 성공적으로 생성되었습니다.',   
                "title": title,                            
                "content": content                         
            }), 201                                         
            # 생성 성공 메시지와 함께 201 상태 코드를 반환합니다.

    @posts_blp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE']) 
    def post(id):
        # '/posts/<id>' 경로에 대해 GET, PUT, DELETE 요청을 처리하는 핸들러를 정의합니다.
        
        cursor = mysql.connection.cursor()                  
        # 데이터베이스 커서를 생성합니다.

        # 게시글 확인
        sql = "SELECT * FROM posts WHERE id = %s"            
        cursor.execute(sql, (id,))                          
        # 지정된 ID의 게시글을 조회하는 SQL 쿼리를 실행합니다.
        
        post = cursor.fetchone()                            
        # 쿼리 결과로 해당 게시글 하나를 가져옵니다.

        if not post:                                        
            abort(404, "게시글을 찾을 수 없습니다.")                    
            # 게시글이 없으면 404 오류를 반환합니다.

        if request.method == 'GET':                         
            # GET 요청 시 지정된 게시글 정보를 반환합니다.
            
            return {                                       
                'id': post[0],                             
                'title': post[1],                          
                'content': post[2]                         
            }
        
        elif request.method == 'PUT':                       
            # PUT 요청 시 게시글을 수정합니다.
            
            title = request.json.get('title')               
            content = request.json.get('content')           
            # 요청 본문에서 새로운 제목과 내용을 가져옵니다.

            if not title or not content:                    
                abort(400, "제목과 내용은 비어 있을 수 없습니다.")  
                # 제목이나 내용이 없으면 400 오류를 반환합니다.

            sql = "UPDATE posts SET title = %s, content = %s WHERE id = %s"  
            cursor.execute(sql, (title, content, id))      
            # 게시글을 수정하는 SQL 쿼리를 실행합니다.
            
            mysql.connection.commit()                       
            # 변경 사항을 데이터베이스에 커밋합니다.

            return jsonify({"msg": "제목과 내용이 성공적으로 수정되었습니다."})  
            # 수정 성공 메시지를 JSON 형태로 반환합니다.
        
        elif request.method == 'DELETE':                    
            # DELETE 요청 시 게시글을 삭제합니다.
            
            sql = "DELETE FROM posts WHERE id = %s"         
            cursor.execute(sql, (id,))                      
            # 지정된 ID의 게시글을 삭제하는 SQL 쿼리를 실행합니다.

            mysql.connection.commit()                       
            # 삭제 사항을 데이터베이스에 커밋합니다.

            return jsonify({"msg": "게시글이 성공적으로 삭제되었습니다."})  
            # 삭제 성공 메시지를 JSON 형태로 반환합니다.

    return posts_blp                                       
    # 구성된 posts 블루프린트를 반환합니다.