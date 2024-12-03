-- `products` 테이블의 모든 데이터를 선택
SELECT * FROM classicmodels.products;

-- `customers` 테이블에 새 고객을 추가
INSERT INTO customers 
    (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, postalCode, country)  -- 삽입할 필드 목록
VALUES (1, 'Seonhong', 'Mun', 'seonhong', '123-456-7890', '21arr', 'seoul', '12345', 'seoul');  -- 각 필드에 대한 값

-- `products` 테이블에 새 제품을 추가
INSERT INTO products 
    (productCode, productName, productLine, productScale, productVendor, quantityInStock, buyPrice, MSRP)  -- 삽입할 필드 목록
VALUES ('S20_001', 'New Product', 'Classic Cars', '1:18', 'Vendor Inc.', 100, 45.50, 95.00);  -- 각 필드에 대한 값

-- `employees` 테이블에 새 직원을 추가
INSERT INTO employees 
    (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)  -- 삽입할 필드 목록
VALUES (1, 'seonhong', 'mun', 'x1234', 'seon.hong@example.com', 1, 1002, 'CEO');  -- 각 필드에 대한 값

-- `offices` 테이블에 새 사무실을 추가
INSERT INTO offices 
    (officeCode, city, phone, addressLine1, postalCode, country, territory)  -- 삽입할 필드 목록
VALUES (0, 'Seoul', '+1 123-456-7890', '서울 강남', '90001', 'KOREA', 'Seoul');  -- 각 필드에 대한 값

-- 외래 키 제약 조건을 일시적으로 비활성화 (외래 키 무시하고 삽입)
SET foreign_key_checks = 0;  -- 외래 키 검사 비활성화

-- `orders` 테이블에 새 주문을 추가
INSERT INTO orders 
    (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)  -- 삽입할 필드 목록
VALUES (10426, '2024-12-03', '2024-12-12', '2024-12-06', 'Shipped', 'Deliver on time.', 501);  -- 각 필드에 대한 값

-- 외래 키 제약 조건을 다시 활성화
SET foreign_key_checks = 1;  -- 외래 키 검사 활성화

-- `orderdetails` 테이블에 주문 상세 정보를 추가
INSERT INTO orderdetails 
    (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)  -- 삽입할 필드 목록
VALUES (10426, 'S20_001', 2, 45.50, 1);  -- 각 필드에 대한 값

-- 외래 키 제약 조건을 일시적으로 비활성화 (외래 키 무시하고 삽입)
SET foreign_key_checks = 0;  -- 외래 키 검사 비활성화

-- `payments` 테이블에 지불 정보를 추가
INSERT INTO payments 
    (customerNumber, checkNumber, paymentDate, amount)  -- 삽입할 필드 목록
VALUES (501, 'CHK50101', '2024-12-03', 91.00);  -- 각 필드에 대한 값

-- 외래 키 제약 조건을 다시 활성화
SET foreign_key_checks = 1;  -- 외래 키 검사 활성화

-- `productlines` 테이블에 새 제품 라인을 추가
INSERT INTO productlines 
    (productLine, textDescription)  -- 삽입할 필드 목록
VALUES ('New Line', '새로운 제품 라인');  -- 각 필드에 대한 값

-- `customers` 테이블에 또 다른 새 고객을 추가
INSERT INTO customers 
    (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, postalCode, country)  -- 삽입할 필드 목록
VALUES (502, '다른고객', 'KIM', 'OZ', '987-654-3210', '789 Secondary St', 'Seoul', '54321', 'South Korea');  -- 각 필드에 대한 값

-- `products` 테이블에 또 다른 새 제품을 추가
INSERT INTO products 
    (productCode, productName, productLine, productScale, productVendor, quantityInStock, buyPrice, MSRP)  -- 삽입할 필드 목록
VALUES ('S20_002', '다른제품', '오토바이', '1:12', 'Another Vendor Inc.', 50, 65.00, 130.00);  -- 각 필드에 대한 값

--------------------------------------------------------------------------------------------------

-- `customers` 테이블에 여러 새 고객을 한 번에 추가
INSERT INTO customers 
    (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, postalCode, country)  -- 삽입할 필드 목록
VALUES 
    (503, '고객1', '빨강', '색', '111-111-1111', '123 A St', 'guro', '73301', 'korea'),  -- 첫 번째 고객 정보
    (504, '고객2', '파랑', '색', '222-222-2222', '456 B St', 'gangnam', '02215', 'korea'),  -- 두 번째 고객 정보
    (505, '고객3', '초록', '색', '333-333-3333', '789 C St', 'hongda', '60601', 'korea');  -- 세 번째 고객 정보

-- `products` 테이블에 여러 새 제품을 한 번에 추가
INSERT INTO products 
    (productCode, productName, productLine, productScale, productVendor, quantityInStock, buyPrice, MSRP)  -- 삽입할 필드 목록
VALUES
    ('S30_001', '제품1', 'Planes', '1:72', 'Vendor A', 200, 80.00, 150.00),  -- 첫 번째 제품 정보
    ('S30_002', '제품2', 'Trucks and Buses', '1:24', 'Vendor B', 300, 50.00, 120.00),  -- 두 번째 제품 정보
    ('S30_003', '제품3', 'Ships', '1:48', 'Vendor C', 150, 90.00, 180.00);  -- 세 번째 제품 정보

-- `employees` 테이블에 여러 새 직원을 한 번에 추가
INSERT INTO employees 
    (employeeNumber, firstName, lastName, extension, email, officeCode, reportsTo, jobTitle)  -- 삽입할 필드 목록
VALUES
    (2000, 'oz','kim','x5678', 'ozkim@example.com', 1, 1002, 'Sales Rep'),  -- 첫 번째 직원 정보
    (2001, 'coding','kim','x4321', 'codingkim@example.com', 2, 1002, 'Support Rep'),  -- 두 번째 직원 정보
    (2002, 'school','kim','x8765', 'schoolkim@example.com', 3, 1056, 'Manager');  -- 세 번째 직원 정보

-- `orders` 테이블에 새 주문을 추가
INSERT INTO orders 
    (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)  -- 삽입할 필드 목록
VALUES (10427, '2024-12-02', '2024-12-15', '2024-12-10', 'Shipped', 'Handle with care.', 503);  -- 주문 정보

-- `orderdetails` 테이블에 주문 상세 정보를 여러 개 추가
INSERT INTO orderdetails 
    (orderNumber, productCode, quantityOrdered, priceEach, orderLineNumber)  -- 삽입할 필드 목록
VALUES
    (10427, 'S30_001', 3, 80.00, 1),  -- 첫 번째 주문 상세 정보
    (10427, 'S30_002', 2, 50.00, 2);  -- 두 번째 주문 상세 정보

-- `payments` 테이블에 여러 지불 정보를 추가
INSERT INTO payments 
    (customerNumber, checkNumber, paymentDate, amount)  -- 삽입할 필드 목록
VALUES
    (503, 'CHK50301', '2024-12-03', 240.00),  -- 첫 번째 지불 정보
    (504, 'CHK50401', '2024-12-03', 150.00),  -- 두 번째 지불 정보
    (505, 'CHK50501', '2024-12-03', 100.00);  -- 세 번째 지불 정보

-- `customers` 테이블에 새 고객을 추가
INSERT INTO customers 
    (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, postalCode, country)  -- 삽입할 필드 목록
VALUES (506, '고객4', '검정', '색', '555-555-5555', '111 D St', 'seoul', '75201', 'korea');  -- 고객 정보

-- `orders` 테이블에 새 주문을 추가
INSERT INTO orders 
    (orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)  -- 삽입할 필드 목록
VALUES (10428, '2024-12-03', '2024-12-20', NULL, 'In Process', 'Rush order.', 506);  -- 주문 정보

-- `employees` 테이블에 새 직원을 추가
INSERT INTO employees 
    (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)  -- 삽입할 필드 목록
VALUES (2003, 'ozcoding', 'school', 'x6789', 'liam.davis@example.com', 1, 1056, 'Intern');  -- 직원 정보

-- 새로 추가된 직원의 직급을 업데이트
UPDATE employees  -- employees 테이블 업데이트
SET jobTitle = 'Junior Sales Rep'  -- jobTitle을 'Junior Sales Rep'으로 변경
WHERE employeeNumber = 2003;  -- employeeNumber가 2003인 직원에게 적용

-- `products` 테이블에 새 제품을 추가
INSERT INTO products 
    (productCode, productName, productLine, productScale, productVendor, quantityInStock, buyPrice, MSRP)  -- 삽입할 필드 목록
VALUES ('S40_001', 'Product D', 'Trains', '1:87', 'Vendor D', 75, 55.00, 110.00);  -- 제품 정보

-- 새로 추가된 제품의 재고를 증가
UPDATE products  -- products 테이블 업데이트
SET quantityInStock = quantityInStock + 50  -- quantityInStock을 50만큼 증가
WHERE productCode = 'S40_001';  -- productCode가 'S40_001'인 제품에 적용

-- `offices` 테이블에 새 사무실을 추가
INSERT INTO offices 
    (officeCode, city, phone, addressLine1, postalCode, country, territory)  -- 삽입할 필드 목록
VALUES (8, '제주도', '+82 000-000-0000', '987 E St', '98101', '제주도', '코리아');  -- 사무실 정보

-- 새 사무실에 직원을 할당
INSERT INTO employees 
    (employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)  -- 삽입할 필드 목록
VALUES (2006, '주황', '색', 'x1235', '주황색@example.com', 8, 1002, 'Sales Rep');  -- 직원 정보

-- `productlines` 테이블에 새 제품 라인을 추가
INSERT INTO productlines 
    (productLine, textDescription)  -- 삽입할 필드 목록
VALUES ('Super Cars', 'Super car models.');  -- 제품 라인 정보

-- `products` 테이블에 여러 새 제품을 한 번에 추가
INSERT INTO products 
    (productCode, productName, productLine, productScale, productVendor, quantityInStock, buyPrice, MSRP)  -- 삽입할 필드 목록
VALUES
    ('Spr_001', 'Super Car A', 'Super Cars', '1:10', 'SuperCar A', 20, 150.00, 300.00),  -- 첫 번째 제품 정보
    ('Spr_002', 'Super Car B', 'Super Cars', '1:10', 'SuperCar B', 30, 200.00, 400.00);  -- 두 번째 제품 정보
#------------------------------------------------------------------------------------------------
#######  고급 해야함
