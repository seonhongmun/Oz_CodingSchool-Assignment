import pymysql
from datetime import datetime  
import time  

time.strftime('%Y-%m-%d %H:%M:%S')
now = datetime.now()

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='8573',
    db='sakila',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cursor:
        # actor 테이블에 내이름 추가
        sql = "INSERT INTO actor (actor_id, first_name, last_name, last_update) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (0, 'SEONHONG', 'MUN', '2000-12-06 02:16:20'))
        conn.commit()

        # city 테이블에 서울 추가
        # 오류 해결사항 country_id foreign key가 맞지 않아서 업로드가 안되었었음
        sql = "INSERT INTO city (city_id, city, country_id, last_update) VALUES(%s, %s, %s, %s)" 
        cursor.execute(sql, (601,"seoul", 1,'2000-01-01 01:00:00' ))
        conn.commit()

        # city 테이블에 제주도 날짜 datatime으로 추가
        sql = "INSERT INTO city (city_id, city, country_id, last_update) VALUES(%s, %s, %s, %s)" 
        cursor.execute(sql, (602,"제주도", 1, now ))
        conn.commit()

        # payments 테이블에서 customer_id 1의 고객 amount를 1.1배하여 갱신
        sql = "UPDATE payment SET amount = amount * 1.1 WHERE customer_id = 1"
        cursor.execute(sql)
        conn.commit()


        # 월 별 총 매출 조회 
        sql = (''' SELECT YEAR(p.payment_date) as year, MONTH(p.payment_date) as month, SUM(p.amount) as total_sales FROM payment p GROUP BY YEAR(p.payment_date), MONTH(p.payment_date)''')
        cursor.execute(sql)
        datas = cursor.fetchall()
        print(datas)

        # 대여 ID가 1인 대여 기록의 상태를 'returned'로 변경하시오.
        sql = 'UPDATE rental SET return_date = NOW() WHERE rental_id = 1'
        cursor.execute(sql)
        conn.commit()

finally:
    conn.close()
