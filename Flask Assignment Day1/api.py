from flask.views import MethodView  # Flask에서 클래스 기반 뷰를 제공하는 MethodView를 가져옵니다.
from flask_smorest import Blueprint, abort  # Flask-Smorest의 Blueprint와 abort 함수를 가져옵니다.
from schemas import BookSchema  # BookSchema를 정의한 schemas 모듈을 가져옵니다.

book_blp = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')  
# 'books'라는 블루프린트를 생성하고 URL 접두사를 '/books'로 설정합니다.

books = []  # 책 정보를 저장할 빈 리스트를 초기화합니다.

@book_blp.route('/')  # 블루프린트에 루트 경로('/')를 라우팅합니다.
class BookList(MethodView):  # BookList 클래스를 정의하며 MethodView를 상속받습니다.
    @book_blp.response(200, BookSchema(many=True))  # GET 요청에 대한 응답으로 다수의 BookSchema를 반환하도록 설정합니다.
    def get(self):
        return books  # 저장된 모든 책 목록을 반환합니다.

    @book_blp.arguments(BookSchema)  # POST 요청에서 BookSchema를 인자로 받습니다.
    @book_blp.response(201, BookSchema)  # 성공적인 POST 요청 시 201 상태 코드와 함께 BookSchema를 반환합니다.
    def post(self, new_data):
        new_data['id'] = len(books) + 1  # 새 책에 고유한 ID를 할당합니다.
        books.append(new_data)  # 새 책 데이터를 books 리스트에 추가합니다.
        return new_data  # 추가된 새 책 데이터를 반환합니다.

@book_blp.route('/<int:book_id>')  # 블루프린트에 '/<int:book_id>' 경로를 라우팅합니다.
class Book(MethodView):  # Book 클래스를 정의하며 MethodView를 상속받습니다.
    @book_blp.response(200, BookSchema)  # GET 요청에 대한 응답으로 하나의 BookSchema를 반환하도록 설정합니다.
    def get(self, book_id):
        book = next((book for book in books if book['id'] == book_id), None)  # 해당 ID를 가진 책을 검색합니다.
        if book is None:
            abort(404, message="원하는 책이 없습니다.")  # 책이 없으면 404 에러를 반환합니다.
        return book  # 찾은 책 데이터를 반환합니다.

    @book_blp.arguments(BookSchema)  # PUT 요청에서 BookSchema를 인자로 받습니다.
    @book_blp.response(200, BookSchema)  # 성공적인 PUT 요청 시 200 상태 코드와 함께 BookSchema를 반환합니다.
    def put(self, new_data, book_id):
        book = next((book for book in books if book['id'] == book_id), None)  # 해당 ID를 가진 책을 검색합니다.
        if book is None:
            abort(404, message="원하는 책이 없습니다.")  # 책이 없으면 404 에러를 반환합니다.
        book.update(new_data)  # 책 정보를 업데이트합니다.
        return book  # 업데이트된 책 데이터를 반환합니다.

    @book_blp.response(204)  # DELETE 요청에 대한 응답으로 204 상태 코드를 설정합니다.
    def delete(self, book_id):
        global books  # 전역 변수 books를 사용합니다.
        book = next((book for book in books if book['id'] == book_id), None)  # 해당 ID를 가진 책을 검색합니다.
        if book is None:
            abort(404, message="원하는 책이 없습니다.")  # 책이 없으면 404 에러를 반환합니다.
        books = [book for book in books if book['id'] != book_id]  # 해당 책을 리스트에서 제거합니다.
        return ''  # 빈 응답을 반환합니다.