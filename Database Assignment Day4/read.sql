-- customers 테이블에서 모든 고객 정보를 조회
SELECT * FROM customers;

-- products 테이블에서 모든 고객 정보를 조회
SELECT * FROM products;

-- employees 테이블에서 직원의 이름과 직급만 선택하여 조회
SELECT firstName, lastName, jobTitle FROM employees;

-- offices 테이블에서 사무실의 도시city와 국가country를 선택하여 조회
SELECT city, country FROM offices;

-- orders 테이블에서 주문 날짜 내림차순 정렬한 후, 상위 10개 행을 선택하여 조회
SELECT * FROM orders ORDER BY orderDate DESC LIMIT 10;

-- 특정 주문 번호에 해당하는 모든 주문 상세 정보를 orderdetails 테이블에서 조회 orderNumber 10426
SELECT * FROM orderdetails WHERE orderNumber = 10426;

-- 특정 고객 번호에 해당하는 모든 지불 정보를 payments 테이블에서 조회 customerNumber 501
SELECT * FROM payments WHERE customerNumber = 501;

-- productlines 테이블에서 제품 라인productLine과 설명textDescription을 조회
SELECT productLine, textDescription FROM productlines;

-- 특정 국가에 속하는 모든 고객을 customers 테이블에서 조회 country korea
SELECT * FROM customers WHERE country = 'korea';

-- products 테이블에서 구매 가격buyPrice 범위 50 ~ 100 제품을 조회
SELECT * FROM products WHERE buyPrice BETWEEN 50.00 AND 100.00;

-- 특정 고객 번호의 모든 주문을 orders 테이블에서 조회 customerNumber 503
SELECT * FROM orders WHERE customerNumber = 503;

-- 특정 제품 코드에 대한 모든 주문 상세 정보를 orderdetails 테이블에서 조회 productCode S30_001
SELECT * FROM orderdetails WHERE productCode = 'S30_001';

-- 특정 기간에 이루어진 모든 지불 정보를 payments 테이블에서 조회 paymentDate 2024-12-01 ~ 2024-12-31
SELECT * FROM payments WHERE paymentDate BETWEEN '2024-12-01' AND '2024-12-31';

-- 특정 직급에 해당하는 모든 직원을 employees 테이블에서 조회 jobTitle Sales Rep'
SELECT * FROM employees WHERE jobTitle = 'Sales Rep';

-- 특정 국가에 위치한 모든 사무실을 offices 테이블에서 조회 country korea
SELECT * FROM offices WHERE country = 'korea';

-- 특정 제품 라인에 속하는 모든 제품을 products 테이블과 productlines 테이블을 조인하여 조회 productLine Planes
SELECT p.* FROM products p JOIN productlines pl 
ON p.productLine = pl.productLine 
WHERE pl.productLine = 'Planes';

-- customers 테이블에서 고객 번호 customerNumber 기준 내림차순정렬 조회 최근 5명의 고객
SELECT * FROM customers ORDER BY customerNumber DESC LIMIT 5;

-- products 테이블에서 재고 수량 모든 제품을 조회 quantityInStock < 50
SELECT * FROM products WHERE quantityInStock < 50;

-- orders 테이블에서 지난 달에 이루어진 모든 주문을 조회
SELECT * FROM orders WHERE orderDate >= '2024-11-01' AND orderDate < '2024-12-01';

-- 특정 주문 번호에 대한 총 금액을 계산, 각 주문 상세의 (수량 * 단가)을 합산 orderNumber 10426
SELECT orderNumber, SUM(quantityOrdered * priceEach) AS totalAmount 
FROM orderdetails WHERE orderNumber = 10426 GROUP BY orderNumber;
