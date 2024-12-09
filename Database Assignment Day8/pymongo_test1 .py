from pymongo import MongoClient
from pymongo.errors import PyMongoError
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client.local

# def insert_data():
#     client = MongoClient('mongodb://localhost:27017/')
#     db = client.local  # 'local' 데이터베이스 사용
#     insert_gerne(db)

# # 특정 장르의 책 
# def insert_gerne(db):
#     book = {
#         "title" : "Harry Potter",
#         "author" : "J.K Rowling", 
#         "year": 1997,
#         "genre" : "fantasy"
#         }
#     try:
#         result = db.books.insert_one(book)
#         print('책이 삽입되었습니당')
#     except:
#         print('문서 삽입 실패')

# def find_genre(db):
#     query = {"genre":"fantasy"}
#     try: 
#         books = db.books.find(query)
#         print('찾은 책 목록')
#         for book in books:
#             print(book)
#     except:
#         print("없어요")
def avg_author(db):
    # 'movies' 컬렉션에서 감독별 평점 평균을 계산하고 내림차순으로 정렬하는 함수
    movies = db.movies  # 'movies' 컬렉션 선택
    # 집계 파이프라인 정의
    pipeline = [
        {
            "$group": {
                "_id": "$director",  # 감독을 기준으로 그룹화
                "average": {"$avg": "$rating"}  # 각 감독의 평점 평균 계산
            }
        },
        {
            "$sort": {"average": -1}  # 평균 평점을 기준으로 내림차순 정렬
        }]
    try:
        # 집계 파이프라인 실행
        results = movies.aggregate(pipeline)
        print("감독별 평균 평점:")
        for result in results:
            print(f"감독: {result['_id']}, 평균 평점: {result['average']:.2f}")  # 감독과 평균 평점 출력
    except PyMongoError as e:
        print("평균평점 계산 실패")

avg_author(db)