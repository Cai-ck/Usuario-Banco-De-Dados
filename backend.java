import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class Backend {

    // Configurações do Banco de Dados
    private static final String URL = "jdbc:mysql://localhost:3306/meu_banco";
    private static final String USER = "root";
    private static final String PASSWORD = "";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("--- Sistema de Cadastro de Usuários ---");
        System.out.print("Digite o nome do usuário: ");
        String nome = scanner.nextLine();
        
        System.out.print("Digite o email do usuário: ");
        String email = scanner.nextLine();

        cadastrarUsuario(nome, email);
        listarUsuarios();
        
        scanner.close();
    }

    public static Connection conectar() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    public static void cadastrarUsuario(String nome, String email) {
        String sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)";

        try (Connection conn = conectar();
             PreparedStatement pstmt = conn.prepareStatement(sql)) {
            
            pstmt.setString(1, nome);
            pstmt.setString(2, email);
            pstmt.executeUpdate();
            System.out.println("Usuário inserido com sucesso!");

        } catch (SQLException e) {
            System.out.println("Erro ao inserir usuário: " + e.getMessage());
        }
    }

    public static void listarUsuarios() {
        String sql = "SELECT id, nome, email FROM usuarios";

        try (Connection conn = conectar();
             PreparedStatement pstmt = conn.prepareStatement(sql);
             ResultSet rs = pstmt.executeQuery()) {

            System.out.println("\nLista de Usuários:");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt("id") + 
                                   " | Nome: " + rs.getString("nome") + 
                                   " | Email: " + rs.getString("email"));
            }

        } catch (SQLException e) {
            System.out.println("Erro ao listar usuários: " + e.getMessage());
        }
    }
}
