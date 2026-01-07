public class Fibonacci {
    
    public static void main(String[] args) {
		
		// Imprime os 20 primeiros números de Fibonacci (0, 1, 1, 2, 3...)

		int x = 0;
		int y = 1;
		System.out.println(x);
		System.out.println(y);
		
		for (int i = 2; i < 18; i++) { // Como já foram os primeiros dois números, repete 18 vezes
			/* A medida que a sequência continua, o x recebe o valor do y, o y recebe o valor que foi impresso
			 * na tela e ocorre a soma deles para gerar o próximo número da sequência... */
			int novoValor = x + y;
			x = y;
			y = novoValor;
			System.out.println(novoValor);
		}
	}
}

