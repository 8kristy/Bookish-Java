package org.softwire.training.bookish;

import org.jdbi.v3.core.Handle;
import org.jdbi.v3.core.Jdbi;
import org.jdbi.v3.core.statement.Query;

import java.sql.*;
import java.util.Map;


public class Main {

    public static void main(String[] args) throws SQLException {
        String hostname = "localhost";
        String database = "bookish_db";
        String user = "root";
        String password = "admin";
        String connectionString = "jdbc:mysql://" + hostname + "/" + database + "?user=" + user + "&password=" + password + "&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=GMT&useSSL=false";

        jdbcMethod(connectionString);
        jdbiMethod(connectionString);
    }

    private static void jdbcMethod(String connectionString) throws SQLException {
        System.out.println("JDBC method...");
        Connection connection = DriverManager.getConnection(connectionString);
        String query = "select * from bookinfo order by title asc"; // query goes here

        try (Statement stmt = connection.createStatement()) {
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next()) {
                String title = rs.getString("title"); // content extraction goes here
                String authorName = rs.getString("authorName");
                String authorSurname = rs.getString("authorSurname");
                System.out.println(title + ", " + authorName + ", " + authorSurname);
            }
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }

    }

    private static void jdbiMethod(String connectionString) {
        System.out.println("\nJDBI method...");

        // TODO: print out the details of all the books (using JDBI)
        // See this page for details: http://jdbi.org
        // Use the "Book" class that we've created for you (in the models.database folder)

        Jdbi jdbi = Jdbi.create(connectionString);

        String sql = "select * from bookinfo order by title asc";

        Handle handle = jdbi.open();
//        Query query = handle.createQuery(sql); // TODO: Replace with mapping to list of books and do extraction/printing that way
//        for (Map map : query.mapToMap()) {
//            int id = (int) map.get("id");
//            System.out.println(id);
//        }


    }
}
