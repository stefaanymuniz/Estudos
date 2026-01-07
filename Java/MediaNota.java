import java.util.Scanner;

public class MediaNota {

    public static void main(String[] args) {
        
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite sua primeira nota: ");
        float n1 = teclado.nextFloat();
        System.out.print("Digite sua segunda nota: ");
        float n2 = teclado.nextFloat();
        float media = (n1+n2)/2;

        System.out.println("Sua média é " + media);

        if (media >= 8) {
            System.out.println("Parabéns!");
        }
    }
}
