package samuelAleks;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.*;

public class JDBCQuery_0 {
	public static void main(String[] args) {
		
		String systemName = args[0];
		String userId = args[1];
		String password = args[2];
		
		try {
			Connection c = DriverManager.getConnection(
					"SERVER:" + systemName, userId, password);
			long startTime = System.currentTimeMillis();
			String qry = "SELECT I.NAME, COUNT(A.S_ID) AS ADVISEE_COUNT\n"
					+ "			FROM DB_BOOK.ADVISOR A, DB_BOOK.INSTRUCTOR I\n"
					+ "			WHERE A.I_ID=I.ID\n"
					+ "			GROUP BY I.NAME\n"
					+ "			ORDER BY ADVISEE_COUNT DESC\n"
					+ "			FETCH FIRST 10 ROWS ONLY";
			Statement stmnt = c.createStatement(); 
			ResultSet rSet = stmnt.executeQuery(qry);
			ResultSetMetaData rMetaData = rSet.getMetaData(); 
			
			System.out.println(rMetaData.getColumnLabel(1) + "," + rMetaData.getColumnLabel(2));
			while (rSet.next()) {
				System.out.println(rSet.getString("NAME") + "," + rSet.getString("ADVISEE_COUNT"));
			}
			
			long endTime = System.currentTimeMillis();
			System.out.println("The number of milliseconds is "+(endTime-startTime));
			c.close();
		} catch (SQLException e) {
			System.out.println("Exception occurred");
			e.printStackTrace(System.out);
		}
	}
}
