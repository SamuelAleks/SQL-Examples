SET SCHEMA U_ALEKS;

SELECT * FROM DB_BOOK.INSTRUCTOR;

SELECT XMLAGG(XMLElement(name "Instructors", XMLAttributes(ID as "instructor_id"),
                                XMLElement(name "name", name), 
                                XMLElement(name "dept_name", DEPT_NAME), 
                                XMLElement(name "salary", SALARY)))
                                From DB_BOOK.INSTRUCTOR WHERE DEPT_NAME='Comp. Sci.'; 
