import java.util.Date;
import java.util.Locale;
import java.awt.Toolkit;
import java.awt.Dimension;

public class DadosSistema {

    public static void main(String[] args) {
        
        System.out.println("Olá! Aqui estão alguns dados do seu sistema:\n");
        Date horario = new Date(); // relogio é um Objeto, pois ele recebe um "new"

        Locale idioma = Locale.getDefault();

        // fornece métodos para interagir com o sistema nativo
        Toolkit systemToolkit = Toolkit.getDefaultToolkit();
        Dimension screenDimension = systemToolkit.getScreenSize();

        int largura_tela = screenDimension.width;
        int altura_tela = screenDimension.height;

        System.out.println("A horário atual é:");
        System.out.println(horario.toString()); 
        System.out.println("O idioma da máquina atual está em " + idioma.getDisplayLanguage()); // sem o getDisplayLanguage, o print é "pt-BR"
        System.out.println("A resolução da sua tela é " + largura_tela + "x" + altura_tela);
    }
}
