-- 특정 고객 customerNumber 501 => addressLine1 서울 강남으로 갱신
UPDATE customers SET addressLine1 = '서울 강남' WHERE customerNumber = 504;

-- 특정 제품 productCode S20_001 금액을 100.00원으로 갱신
UPDATE products SET buyPrice = 100.00 WHERE productCode = 'S20_001';

-- employeeNumber 2002 직원의 직급을 Senior Manager로 갱신
UPDATE employees SET jobTitle = 'Senior Manager' WHERE employeeNumber = 2002;

-- officeCode 8 전번을 +1 012-345-6789로 갱신
SET SQL_SAFE_UPDATES = 0; -- Safe Update Mode를 비활성화한다.
UPDATE offices SET phone = '+1 012-345-7890' WHERE officeCode = 8;
SET SQL_SAFE_UPDATES = 1; -- Safe Update Mode를 활성화한다.

-- orderNumber 1048 상태를 Shipped로 갱신
UPDATE orders SET status = 'Shipped' WHERE orderNumber = 10428;

-- orderNumber 10426 이고 productCode S20_001인 orderdetails의 주문갯수 quantityOrdered를 3개로 갱신
UPDATE orderdetails SET quantityOrdered = 3 WHERE orderNumber = 10426 AND productCode = 'S20_001';

-- checkNumber CHK50301의 amount를 payment에서 찾아서 250.00원으로 갱신
SET SQL_SAFE_UPDATES = 0; -- Safe Update Mode를 비활성화한다.
UPDATE payments SET amount = 250.00 WHERE checkNumber = 'CHK50301';
SET SQL_SAFE_UPDATES = 1; -- Safe Update Mode를 활성화한다.

-- 특정 제품 Super Car의 설명textDescription을 고성능 슈퍼카 모델로 갱신
UPDATE productlines SET textDescription = '고성능 슈퍼카 모델' WHERE productLine = 'Super Cars';

-- 특정 고객의 이메일을 고객4@example.com으로 갱신 (문제이상) Customers에 email이 존재하지 않음..
# UPDATE customers SET email = '고객4@example.com' WHERE customerNumber = 506;

-- 여러 제품의 구매 가격을 일괄 갱신
UPDATE products 
SET buyPrice = CASE 
    WHEN productCode = 'S30_001' THEN 85.00
    WHEN productCode = 'S30_002' THEN 55.00
    WHEN productCode = 'S30_003' THEN 95.00
    ELSE buyPrice
END 
WHERE productCode IN ('S30_001', 'S30_002', 'S30_003');