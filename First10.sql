﻿SET SCHEMA P_ALEKS;

SELECT * FROM COMPENSATION2;
SELECT * FROM ORGANIZATION_GROUP;
SELECT * FROM JOB_FAMILY;
SELECT * FROM JOB;
SELECT * FROM DEPARTMENT;
SELECT * FROM UNION;

SELECT * FROM SPENDREV2;
SELECT * FROM PROGRAM;
SELECT * FROM CHARACTER;
SELECT * FROM OBJECT;
SELECT * FROM SUB_OBJECT;
SELECT * FROM FUND_TYPE;
SELECT * FROM FUND;
SELECT * FROM FUND_CATEGORY;

-- Are There more Job Families than Unions
SELECT C.SALARIES, J.JOB
    FROM COMPENSATION2 C JOIN JOB J
    ON C.JOB_CODE = J.JOB_CODE
    ORDER BY C.SALARIES DESC
    FETCH FIRST 10 ROWS ONLY;


SELECT C.SALARIES, U.UNION
    FROM COMPENSATION2 C JOIN UNION U
    ON C.UNION_CODE = U.UNION_CODE
    ORDER BY C.SALARIES DESC
    FETCH FIRST 10 ROWS ONLY;


SELECT C.RETIREMENT, O.ORGANIZATION_GROUP
    FROM P_ALEKS.COMPENSATION2 C JOIN P_ALEKS.ORGANIZATION_GROUP O
    ON C.ORGANIZATION_GROUP_CODE = O.ORGANIZATION_GROUP_CODE
    ORDER BY C.RETIREMENT DESC
    FETCH FIRST 10 ROWS ONLY;


SELECT S.AMOUNT, F.FUND
    FROM P_ALEKS.SPENDREV2 S JOIN P_ALEKS.FUND F
    ON S.FUND_CODE = F.FUND_CODE
    WHERE S.REVENUE_OR_SPENDING = 'Spending'
    ORDER BY S.AMOUNT DESC
    FETCH FIRST 10 ROWS ONLY;


SELECT
    FROM
    WHERE
    ORDER BY
    FETCH FIRST 10 ROWS ONLY;




