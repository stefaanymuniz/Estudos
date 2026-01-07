import java.util.Scanner;

public class Tabuada {
    public static void main(String[] args) {
        
        try(Scanner teclado = new Scanner(System.in)) {
        System.out.println("Tabuada do número...");
        int numTabuada = teclado.nextInt();
        
        for (int num = 1; num <= 10; num++) {
            int resultado;
            resultado = num * numTabuada;
            System.out.println(num + " x " + numTabuada + " = " + resultado);
        }}
    }
}
