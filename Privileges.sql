﻿Set schema U_ALEKS;

CREATE TABLE U_ALEKS.Student  -- Create table from DB_BOOK
AS (SELECT * FROM DB_BOOK.STUDENT) 
WITH DATA;

GRANT SELECT ON U_ALEKS.STUDENT to U_ALEKS2, U_EBERHA2;

SELECT GRANTEE, TABLE_SCHEMA, TABLE_NAME, PRIVILEGE_TYPE, IS_GRANTABLE
FROM QSYS2.SYSTABAUTH WHERE TABLE_SCHEMA='U_ALEKS'
AND GRANTEE = 'U_ALEKS2';

GRANT UPDATE(DEPT_NAME) ON U_ALEKS.STUDENT to U_ALEKS2, U_EBERHA2;
