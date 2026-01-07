public class IdadeLegal {

    public static void main(String[] args) {
		
		int numero = 15;

		// Usando o Ternário:
		// Se a maioridade for true, imprima "Maior de idade", senão imprima "Menor de Idade"
		String maioridade = (numero >= 18) ? "Maior de Idade" : "Menor de Idade"; 
		System.out.println(maioridade);
	}
}