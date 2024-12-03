-- 외래키 옵션해제
SET foreign_key_checks = 0;
-- customerNumber 503 고객을 삭제
DELETE FROM customers WHERE customerNumber = 496;

-- products 테이블에서 S24_3856의 제품을 특정 제품을 삭제
DELETE FROM products WHERE productCode = 'S24_3856';

-- employees 테이블에서 employeeNumber 2000 직원을 삭제
DELETE FROM employees WHERE employeeNumber = '2000';

-- offices 테이블에서 제주도 사무실을 삭제
DELETE FROM offices WHERE officeCode = 8;

-- orders 테이블에서 orderNumber 10426 주문을 삭제
DELETE FROM orders WHERE orderNumber = 10426;

--  orderdetails 테이블에서 orderNumber 10426 주문 상세를 삭제
DELETE FROM orderdetails WHERE orderNumber = 10426;

-- payments 테이블에서 customerNumber 501 지불 내역을 삭제
DELETE FROM payments WHERE customerNumber = 501;

-- productlines 테이블에서 productLine New Line 제품 라인을 삭제
DELETE FROM productlines WHERE productLine = 'New Line';

-- customers 테이블에서 nyc 지역의 모든 고객을 삭제
DELETE FROM customers WHERE city = 'nyc';

-- products 테이블에서 motorcycles 카테고리의 모든 제품을 삭제
DELETE FROM products WHERE productLine = 'Motorcycles';

-- 외래키 옵션설정
SET foreign_key_checks = 1;