import pymysql

# 데이터베이스 연결 설정
conn = pymysql.connect(
    host='localhost',  # 데이터베이스 서버 주소
    user='root',       # 데이터베이스 사용자 이름
    password='****',   # 데이터베이스 비밀번호
    db='db_test',      # 데이터베이스 이름
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with conn.cursor() as cur:
        
        # 1) 새로운 사용자 "8ki joa" 추가
        sql = """
        INSERT INTO users (first_name, last_name, email, password, address, contact, gender, is_active, is_staff)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(sql, ('8ki', 'joa', '8ki@example.com', 'pass123', '강남', '012-3456-7890', 'MALE', True, False))
        conn.commit()

        # 2) 사용자 "8ki joa"의 주소 변경
        sql = """
        UPDATE users
        SET address = %s
        WHERE first_name = %s AND last_name = %s
        """
        cur.execute(sql, ('홍대', '8ki', 'joa'))
        conn.commit()

        # 3) 사용자 "8ki joa"의 주문 생성
        # 주문 기록 추가
        sql = """
        INSERT INTO sales_records (user_id, store_id, is_refund)
        VALUES ((SELECT id FROM users WHERE first_name = %s AND last_name = %s) LIMIT 1, %s, FALSE)
        """
        cur.execute(sql, ('8ki', 'joa', 1))
        conn.commit()

        # 판매된 제품을 sales_items에 추가
        sql = """
        INSERT INTO sales_items (sales_record_id, product_id, quantity)
        VALUES ((SELECT id FROM sales_records WHERE user_id = (SELECT id FROM users WHERE first_name = %s AND last_name = %s) LIMIT 1), %s, %s)
        """
        # fish Bun
        cur.execute(sql, ('8ki', 'joa', 1, 3))
        
        # Red Bean Bun 붕어빵 2개 (product_id = 2)
        cur.execute(sql, ('8ki', 'joa', 2, 2))
        
        # 시그니처 메뉴 5개 (product_id = 5)
        cur.execute(sql, ('8ki', 'joa', 5, 5))
        conn.commit()

        # 4) 발주이력 3건 생성
        sql = """
        INSERT INTO order_records (employee_id, supplier_id, raw_material_id, quantity)
        VALUES (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s)
        """
        cur.execute(sql, (21, 1, 101, 50, 2, 2, 102, 30, 3, 1, 103, 20))
        conn.commit()

        # 5) 원재료 사용 이력 3건 추가
        sql = """
        INSERT INTO stocks (raw_material_id, pre_quantity, quantity, change_type, store_id)
        VALUES (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s), (%s, %s, %s, %s, %s)
        """
        cur.execute(sql, (101, 500, 100, 'OUT', 1, 102, 300, 50, 'OUT', 2, 103, 200, 30, 'OUT', 3))
        conn.commit()

        # 최근 사용 이력 3건 조회
        sql = "SELECT * FROM stocks ORDER BY create_at DESC LIMIT 3"
        cur.execute(sql)
        print("\n최근 원재료 사용 이력:")
        for row in cur.fetchall():
            print(row)

        # 6) "8ki joa"가 주문한 내역 조회 (비싼 금액 순)
        sql = """
        SELECT p.name AS product_name, si.quantity, p.price * si.quantity AS total_price
        FROM sales_items si
        JOIN products p ON si.product_id = p.id
        WHERE si.sales_record_id IN (SELECT id FROM sales_records WHERE user_id = (SELECT id FROM users WHERE first_name = %s AND last_name = %s))
        ORDER BY total_price DESC
        """
        cur.execute(sql, ('8ki', 'joa'))
        print("\n사용자 '8ki joa'의 주문 내역:")
        for row in cur.fetchall():
            print(row)

finally:
    conn.close()
