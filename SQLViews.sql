set schema P_ALEKS;

-- First View
Create View E42V1 as
Select Year, semester, COURSE_ID, GRADE
from DB_BOOK.TAKES
Group by cube (year, semester, COURSE_ID, grade);
select * from E42V1;

--Combine Grade with percent
CREATE VIEW E42V2 AS SELECT
    E.Year,
    E.Semester,
    E.COURSE_ID,
    G.PERCENT
    FROM E42V1 E Left JOIN DB_BOOK.GRADE_PERCENT G
    on E.GRADE = G.GRADE;
SELECT * FROM E42V2;

-- Include average grade
CREATE VIEW E42V3 AS SELECT 
    Year,
    Semester,
    COURSE_ID,
    avg(percent) as Percent
    FROM E42V2 
    --left join DB_Book.Course USING (course_id)
    GROUP BY rollup(year, semester, course_id);
SELECT * FROM E42V3
Order by Year ASC; 

--Combine Course with course_name
CREATE VIEW E42V4 AS SELECT
    E.Year,
    E.Semester,
    C.Title,
    E.Percent
    FROM E42V3 E JOIN DB_BOOK.Course C
    on E.COURSE_ID = C.COURSE_ID;
SELECT * FROM E42V4;

--Final for part1, sorted
SELECT * From E42V4
Order By Year, semester ASC;


CREATE VIEW E42V5 AS; SELECT 
    Year,
    Semester,
    COURSE_ID,
    Count() as Count
    FROM E42V2 
    --left join DB_Book.Course USING (course_id)
    GROUP BY year, semester, course_id;
SELECT * FROM E42V4;

--Final for part2, sorted
SELECT * From E42V5
Order By Year, semester ASC;

Select * From DB_Book.Course;
Select * From DB_Book.Takes;
Select * From DB_Book.grade_Percent;

Select Year, JOB_CODE, Salaries
from P_ALEKS.COMPENSATION2
Group by cube (Year, JOB_CODE, Salaries);
FETCH FIRST 10 ROWS ONLY;


Select Year, JOB_CODE, Salaries
from P_ALEKS.COMPENSATION2
Group by rollup(Year, JOB_CODE, Salaries);


Select Year, JOB_CODE, Salaries
from P_ALEKS.COMPENSATION2
Group by grouping sets((Year, JOB_CODE, Salaries),(JOB_CODE));


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
