package samuelAleks;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCQuery_2 {
	public static void main(String[] args) {
		
		String systemName = args[0];
		String userId = args[1];
		String password = args[2];
		
		try {
			Connection c = DriverManager.getConnection(
					"SERVER" + systemName, userId, password);
			
			// ----- START OF QUERY 1 -----
			long startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Base salary sorted by job position");
			String qry = "SELECT C.SALARIES, J.JOB\n"
					+ "    FROM P_ALEKS.COMPENSATION2 C JOIN P_ALEKS.JOB J\n"
					+ "    ON C.JOB_CODE = J.JOB_CODE\n"
					+ "    ORDER BY C.SALARIES DESC\n"
					+ "    FETCH FIRST 10 ROWS ONLY";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			Statement stmnt = c.createStatement(); 
			ResultSet rSet = stmnt.executeQuery(qry);
			ResultSetMetaData rMD = rSet.getMetaData(); 
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)));
			}
			
			long endTime = System.currentTimeMillis(); 
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 1 -----
			
			
			
			// ----- START OF QUERY 2 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Highest-paying Union");
			qry = "SELECT C.SALARIES, U.UNION\n"
					+ "    FROM P_ALEKS.COMPENSATION2 C JOIN P_ALEKS.UNION U\n"
					+ "    ON C.UNION_CODE = U.UNION_CODE\n"
					+ "    ORDER BY C.SALARIES DESC\n"
					+ "    FETCH FIRST 10 ROWS ONLY";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement(); 
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData(); 
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)));
			}
			endTime = System.currentTimeMillis(); 
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 2 -----


			// ----- START OF QUERY 3 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Highest health and dental plans, joined with department");
			qry = "SELECT C.HEALTH_AND_DENTAL, D.DEPARTMENT\n"
					+ "    FROM P_ALEKS.COMPENSATION2 C JOIN P_ALEKS.DEPARTMENT D\n"
					+ "    ON C.DEPARTMENT_CODE = D.DEPARTMENT_CODE\n"
					+ "    ORDER BY C.HEALTH_AND_DENTAL DESC\n"
					+ "    FETCH FIRST 10 ROWS ONLY";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement(); 
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData(); 
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)));
			}
			endTime = System.currentTimeMillis(); 
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 3 -----


			// ----- START OF QUERY 4 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Highest retirements, joined with organization group");
			qry = "SELECT C.RETIREMENT, O.ORGANIZATION_GROUP\n"
					+ "    FROM P_ALEKS.COMPENSATION2 C JOIN P_ALEKS.ORGANIZATION_GROUP O\n"
					+ "    ON C.ORGANIZATION_GROUP_CODE = O.ORGANIZATION_GROUP_CODE\n"
					+ "    ORDER BY C.RETIREMENT DESC\n"
					+ "    FETCH FIRST 10 ROWS ONLY";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement(); 
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData(); 
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)));
			}
			endTime = System.currentTimeMillis(); 
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 4 -----


			// ----- START OF QUERY 5 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Highest spending sorted by department");
			qry = "SELECT S.AMOUNT, F.FUND\n"
					+ "    FROM P_ALEKS.SPENDREV2 S JOIN P_ALEKS.FUND F\n"
					+ "    ON S.FUND_CODE = F.FUND_CODE\n"
					+ "    WHERE S.REVENUE_OR_SPENDING = 'Spending'\n"
					+ "    ORDER BY S.AMOUNT DESC\n"
					+ "    FETCH FIRST 10 ROWS ONLY";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement(); 
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData(); 
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)));
			}
			endTime = System.currentTimeMillis(); 
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			// ----- END OF QUERY 5 -----
			
			c.close();
		} catch (SQLException e) {
			System.out.println("Exception occurred");
			e.printStackTrace(System.out);
		}
	}
}
