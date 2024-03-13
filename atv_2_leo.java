import java.util.Scanner;

public class atv_2_leo {
    static int soma = 0;
    static int i = 1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite um número inteiro positivo: ");
        int n = scanner.nextInt();
        scanner.close();
        soma = 0;
        soma = recursividade(n);
        
        System.out.println("A soma dos números de 1 a " + n + " é: " + soma);
    }

    public static int recursividade(int n) {
        if (n == 1) {
            return 1;
        } else {
            soma += i;
            i++;
            return n + recursividade(n - 1);
        }
    }
}
