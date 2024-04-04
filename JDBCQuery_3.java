package Proj5;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.ResultSetMetaData;
import java.sql.SQLException;
import java.sql.Statement;

public class JDBCQuery_3 {
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
			System.out.println("Query Description: Cube()");
			String qry = "Select Year, JOB_CODE, Salaries\n"
					+ "from P_ALEKS.COMPENSATION2\n"
					+ "Group by cube (Year, JOB_CODE, Salaries)";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			Statement stmnt = c.createStatement();
			ResultSet rSet = stmnt.executeQuery(qry);
			ResultSetMetaData rMD = rSet.getMetaData();
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2) + "," + rMD.getColumnLabel(3));
			int i = 0;
			while (rSet.next() && i < 10) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)) + "," + rSet.getString(rMD.getColumnLabel(3)));
				i += 1;
			}

			long endTime = System.currentTimeMillis();
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 1 -----



			// ----- START OF QUERY 2 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Rollup()");
			qry = "Select Year, JOB_CODE, Salaries\n"
					+ "from P_ALEKS.COMPENSATION2\n"
					+ "Group by rollup(Year, JOB_CODE, Salaries)";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement();
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData();
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2) + "," + rMD.getColumnLabel(3));
			i = 0;
			while (rSet.next() && i < 10) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)) + "," + rSet.getString(rMD.getColumnLabel(3)));
				i += 1;
			}
			endTime = System.currentTimeMillis();
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 2 -----


			// ----- START OF QUERY 3 -----
			startTime = System.currentTimeMillis();
			//Description and query of Query 1
			System.out.println("Query Description: Grouping Sets()");
			qry = "Select Year, JOB_CODE, Salaries\n"
					+ "from P_ALEKS.COMPENSATION2\n"
					+ "Group by grouping sets((Year, JOB_CODE, Salaries),(JOB_CODE))";
			System.out.println("Query: " + qry + "\n");
			//Set Variables
			stmnt = c.createStatement();
			rSet = stmnt.executeQuery(qry);
			rMD = rSet.getMetaData();
			//Print output
			System.out.println(rMD.getColumnLabel(1) + "," + rMD.getColumnLabel(2) + "," + rMD.getColumnLabel(3));
			i = 0;
			while (rSet.next() && i < 10) {
				System.out.println(rSet.getString(rMD.getColumnLabel(1)) + "," + rSet.getString(rMD.getColumnLabel(2)) + "," + rSet.getString(rMD.getColumnLabel(3)));
				i += 1;
			}
			endTime = System.currentTimeMillis();
			System.out.println("The query took "+(endTime-startTime) + " milliseconds\n");
			System.out.println("---------------------------------------------\n");
			// ----- END OF QUERY 3 -----


		} catch (SQLException e) {
			System.out.println("Exception occurred");
			e.printStackTrace(System.out);
		}
	}
}
