import java.util.Random;
import java.util.Scanner;

public class NumberGame {

    public static int playRound(int roundNumber, int maxAttempts, Scanner scanner) {
        Random random = new Random();
        int numberToGuess = random.nextInt(100) + 1;
        int attempts = 0;

        System.out.println("\n🎯 Round " + roundNumber + " - Guess the number between 1 and 100!");

        while (attempts < maxAttempts) {
            System.out.print("Attempt " + (attempts + 1) + "/" + maxAttempts + ": Your guess? ");

            if (!scanner.hasNextInt()) {
                System.out.println("⚠️ Please enter a valid number.");
                scanner.next(); // discard invalid input
                continue;
            }

            int guess = scanner.nextInt();
            attempts++;

            if (guess < numberToGuess) {
                System.out.println("🔻 Too low!");
            } else if (guess > numberToGuess) {
                System.out.println("🔺 Too high!");
            } else {
                System.out.println("✅ Correct! You guessed it in " + attempts + " attempt(s).");
                return maxAttempts - attempts + 1; // Points awarded
            }
        }

        System.out.println("❌ Out of attempts! The correct number was " + numberToGuess + ".");
        return 0; // No points for failing the round
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int totalScore = 0;
        int round = 1;
        int maxAttempts = 7;

        System.out.println("🎮 Welcome to the Number Guessing Game!");

        while (true) {
            int roundScore = playRound(round, maxAttempts, scanner);
            totalScore += roundScore;
            System.out.println("🏆 Round " + round + " Score: " + roundScore + " | Total Score: " + totalScore);

            System.out.print("🔁 Play another round? (yes/no): ");
            String playAgain = scanner.next().trim().toLowerCase();

            if (!playAgain.equals("yes")) {
                System.out.println("\n🎉 Game Over! Your final score is: " + totalScore);
                break;
            }
            round++;
        }

        scanner.close();
    }
}