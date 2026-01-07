public class Xubirubi { // Classe (Titulo) -> CamelCase (Que também está dentro de um pacote)

	public static void main(String[] args) { // Método Principal | main + ctrl + espaço -> Eclipse
		
		System.out.println("Olá Mundo!"); // syso + ctrl + espaço -> auto completa
		
		// TIPOS PRIMITIVOS
		
		int idade; // DECLARAÇÃO
		idade = 18; // ATRIBUIÇÃO
				
		// long populacao = 8062000000l; // para números acima de 32 bits = 4 bilhões
		String nome = "Stefany";
		// boolean z = true;
		// double pi = 3.14;
		// char sexo = 'F'; // Para um único caracter; usa aspas simples
		
		System.out.println(nome.length()); // mostrar o tamanho da variável
		
		idade = 15;
		
		if (idade < 18) {
			System.out.println("Menor de Idade");
		} else if (idade < 12) {
			System.out.println("Criança");
		} else {
			System.out.println("???");
		}
	}

}
