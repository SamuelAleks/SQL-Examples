import java.io.*;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.sql.*;

public class JDBCQuery_1 extends HttpServlet {
	
	private void resultSetToHTML(ResultSet rs, PrintWriter out) throws SQLException {
		ResultSetMetaData rsmd = rs.getMetaData();
		int numCols = rsmd.getColumnCount();
		out.println("<table border=1>");
		out.println("<tr>");
		for (int i=0; i < numCols; i++) {
			out.println("<th>"+ rsmd.getColumnName(i+1));
		}
		out.println("");
		while (rs.next()) {
			out.println("<tr>");
			for (int i=0; i < numCols; i++)
				out.println("<td>"+ rs.getString(i+1));
		}
		out.println("");
		out.println("</table>");
	}
	
	
	String message = "Hello World!";
	public void doGet(HttpServletRequest request,
			HttpServletResponse response)
					throws ServletException, IOException {
		response.setContentType("text/html");
		
		String URL = "SERVER";
		String user =request.getParameter("user");
		String password = request.getParameter("password");
		
		PrintWriter out = response.getWriter();
		if (user == null || password == null) {
			if (user == null)
				user = "";
			if (password == null)
				password = "";
			out.println("<form action=\"welcome\">");
			out.println("<label for=\"user\">User:<label><br>");
			out.println("<input type=\"text\" id=\"user\" value=\"" + user + "\"><br>");
			out.println("<label for=\"password\">Password:<label><br>");
			out.println("<input type=\"password\" id=\"password\" name=\"password\" value=\"" + password + "\"><br><br>");
			out.println("<input type=\"submit\" value=\"Submit\">");
			out.println("<form>");
		}
		
		
		out.println("<HEAD><TITLE>Query result</TITLE></HEAD>");
		out.println("<BODY>");
		out.println("<h1>Query result</h1>");
		try {
			Class.forName("DRIVER");
			Connection c = DriverManager.getConnection(URL,user,password);
			Statement stmt = c.createStatement();
			String query = "SELECT I.NAME, COUNT(A.S_ID) AS ADVISEE_COUNT\n"
					+ 					"FROM DB_BOOK.ADVISOR A, DB_BOOK.INSTRUCTOR I\n"
					+ 					"WHERE A.I_ID=I.ID\n"
					+ 					"GROUP BY I.NAME\n"
					+					"ORDER BY ADVISEE_COUNT DESC\n"
					+ 					"FETCH FIRST 10 ROWS ONLY";
			ResultSet rs = stmt.executeQuery(query);
			resultSetToHTML(rs, out);
			rs.close();
			stmt.close();
			c.close();
			
		}
		catch (Exception e) {
			out.println("<pre>");
			e.printStackTrace(out);
			out.println("</pre>");
		}
		out.println("</BODY>");
	}
}

