-- users 테이블에 유저 10명 생성
INSERT INTO users (last_name, email, password, address, contact, gender) VALUES
('김종국','user1@example.com', 'password1',  'Address1','010-0000-0001', 'MALE'), 
('이광수', 'user2@example.com','password2', 'Address2', '010-0000-0002','MALE'), 
('개리', 'user3@example.com','password3', 'Address3','010-0000-0003', 'MALE'),
('지석진', 'user4@example.com','password4',  'Address4','010-0000-0004','MALE'),
('양세찬','user5@example.com', 'password5', 'Address5', '010-0000-0005','MALE'),
('송중기', 'user6@example.com','password6', 'Address6','010-0000-0006','MALE'),
('유재석', 'user7@example.com','password7',  'Address7','010-0000-0007','MALE'),
('지예은', 'user8@example.com','password8', 'Address8', '010-0000-0008','FEMALE'),
('하하', 'user9@example.com','password9',  'Address9','010-0000-0009','MALE'),
('송지효', 'user10@example.com','password10', 'Address10', '010-0000-0010','FEMALE');

-- stocks 테이블에 재고 변동 이력 10개 생성
INSERT INTO sales_records (user_id, store_id, is_refund) 
VALUES 
(1, 1, FALSE),
(2, 1, TRUE),
(1, 1, FALSE),
(2, 1, TRUE),
(1, 1, FALSE),
(2, 1, TRUE),
(1, 1, FALSE),
(2, 1, TRUE),
(1, 1, FALSE),
(2, 1, TRUE);

INSERT INTO sales_items (sales_record_id, product_id, quantity, created_at)
VALUES
(1, 1, 3, NOW()),
(2, 1, 2, '2024-12-01 10:00:00'),
(1, 1, 3, NOW()),
(2, 1, 2, '2024-12-01 10:10:00'),
(1, 1, 3, NOW()),
(2, 1, 2, '2024-12-01 10:20:00'),
(1, 1, 3, NOW()),
(2, 1, 2, '2024-12-01 10:30:00'),
(1, 1, 3, NOW()),
(2, 1, 2, '2024-12-01 10:40:00');


-- products 테이블에 시그니처 메뉴 추가
INSERT INTO products (name, description, price) VALUES
('알쏭달쏭 폭탄', '던지면 터져욧', 10000); -- 시그니처 제품

-- . 매장 2개 늘리기
INSERT INTO stores (name, address,is_active) VALUES
('홍대점', '서울특별시 마포구 홍대입구', TRUE), -- 홍대점
('강남점', '서울특별시 강남구 역삼동', TRUE); -- 강남점

-- employees 테이블에 직원 데이터 삽입
INSERT INTO employees (id, code, type, user_id, store_id, is_active)
VALUES
(1, '1', 'staff', 21, 5, 1),-- 김종국 매장 5 직원
(2, '2', 'manager',22, 7, 1); -- 이광수 매장 7 매니저
