from pymongo import MongoClient  # pymongo 라이브러리에서 MongoClient 클래스를 임포트
from datetime import datetime  # datetime 모듈에서 datetime 클래스를 임포트

# MongoDB에 연결하기 위한 클라이언트 생성
client = MongoClient('mongodb://localhost:27017/')  # 로컬호스트의 27017 포트에 있는 MongoDB에 연결
db = client.local  # 'local'이라는 이름의 데이터베이스를 선택

# 특정 장르의 책을 삽입하는 함수
def insert_gerne(db):
    base = db.books # 'books' 컬렉션 선택
    # 삽입할 책 정보 정의 
    book = {
        "title" : "Harry Potter",  # 책 제목
        "author" : "J.K Rowling",  # 저자 이름
        "year": 1997,  # 출판 연도
        "genre" : "fantasy"  # 장르
    }
    try:
        result = base.insert_one(book)  # 'books' 컬렉션에 book 문서를 삽입
        print('책이 삽입되었습니당')  # 삽입 성공 메시지 출력
    except:
        print('문서 삽입 실패')  # 삽입 실패 시 오류 메시지 출력

# 특정 장르의 책을 찾는 함수
def find_genre(db):
    query = {"genre":"fantasy"}  # 검색할 쿼리 조건 설정 (genre가 'fantasy'인 문서)
    try: 
        books = db.books.find(query)  # 'books' 컬렉션에서 쿼리에 맞는 문서들을 찾음
        print('찾은 책 목록')  # 찾은 책 목록 출력 시작 메시지
        for book in books:  # 찾은 각 책 문서에 대해 반복
            print(book)  # 책 문서 출력
    except:
        print("없어요")  # 조회 실패 시 메시지 출력

# 감독별 평점 평균을 계산하고 내림차순으로 정렬하는 함수
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
        }
    ]
    try:
        # 집계 파이프라인 실행
        results = movies.aggregate(pipeline)  # 집계 파이프라인을 'movies' 컬렉션에 적용
        print("감독별 평균 평점:")  # 결과 출력 시작 메시지
        for result in results:  # 집계 결과에 대해 반복
            print(f"감독: {result['_id']}, 평균 평점: {result['average']:.2f}")  # 감독 이름과 평균 평점 출력
    except:
        print("평균평점 계산 실패")  # 집계 실패 시 메시지 출력

# 사용자 이동 데이터를 처리하는 함수
def move_user(db):
    move = db.user_actions  # 'user_actions' 컬렉션 선택
    # Aggregation 파이프라인 정의
    pipeline = [
        {"$match": {"user_id": 1}},       # user_id가 1인 문서 필터링
        {"$sort": {"timestamp": 1}},       # timestamp를 기준으로 오름차순 정렬
        {"$limit": 5}                      # 상위 5개 문서만 선택
    ]
    results = move.aggregate(pipeline)  # 집계 파이프라인을 'user_actions' 컬렉션에 적용하여 결과 반환

    # 결과 출력
    for result in results:  # 집계 결과에 대해 반복
        print(result)  # 각 결과 문서 출력

# 출판 추세를 분석하는 함수
def publishing_trend(db):
    trend = db.books  # 'books' 컬렉션 선택

    # Aggregation Pipeline 정의
    pipeline = [
        {"$group": {"_id": "$year", "count": {"$sum": 1}}},  # 연도별로 그룹화하고 책 수 계산
        {"$sort": {"count": -1}}  # 책 수를 기준으로 내림차순 정렬
    ]

    # Aggregate 결과 실행
    results = trend.aggregate(pipeline)  # 집계 파이프라인을 'books' 컬렉션에 적용

    # 결과 출력
    print("출판 연도별 책의 수 (내림차순):")  # 결과 출력 시작 메시지
    for result in results:  # 집계 결과에 대해 반복
        print(f"출판 연도: {result['_id']}, 출판된 책 수: {result['count']}")  # 연도와 책 수 출력

# 사용자 행동 데이터를 업데이트하는 함수
def update_action(db):
    # 1. 컬렉션 선택
    action = db.user_actions  # 'user_actions' 컬렉션 선택

    # 2. 업데이트 조건 설정
    query = {
        "user_id": 1,  # user_id가 1인 문서
        "action": "view",  # action이 'view'인 문서
        "timestamp": {"$lt": datetime(2023, 4, 13)}  # timestamp가 2023년 4월 13일 이전인 문서
    }
    # 업데이트할 내용 정의
    update = {"$set": {"action": "seen"}}  # action 필드를 'seen'으로 변경

    # 3. 업데이트 실행
    result = action.update_many(query, update)  # 조건에 맞는 모든 문서를 업데이트

    # 4. 결과 출력
    if result.matched_count == 0:  # 조건에 맞는 문서가 없을 경우
        print("조건에 맞는 문서가 없습니다.")  # 메시지 출력
    else:
        print(f"조건에 맞는 문서 수: {result.matched_count}")  # 조건에 맞는 문서 수 출력
        print(f"수정된 문서 수: {result.modified_count}")  # 실제로 수정된 문서 수 출력

insert_gerne(db)