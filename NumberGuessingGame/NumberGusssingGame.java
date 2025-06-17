import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int totalScore = 0;
        boolean playAgain = true;

        System.out.println("🎯 Welcome to the Number Guessing Game!");

        while (playAgain) {
            int targetNumber = random.nextInt(100) + 1; // 1 to 100
            int maxAttempts = 7;
            int attempts = 0;
            boolean isGuessed = false;

            System.out.println("\nI've picked a number between 1 and 100. Can you guess it?");
            System.out.println("You have " + maxAttempts + " attempts.");

            while (attempts < maxAttempts) {
                System.out.print("Enter your guess: ");
                
                // Validate input
                if (!scanner.hasNextInt()) {
                    System.out.println("❌ Please enter a valid number.");
                    scanner.next(); // skip invalid input
                    continue;
                }

                int userGuess = scanner.nextInt();
                attempts++;

                if (userGuess == targetNumber) {
                    System.out.println("✅ Correct! You guessed the number in " + attempts + " attempts.");
                    totalScore += (maxAttempts - attempts + 1); // more points for fewer attempts
                    isGuessed = true;
                    break;
                } else if (userGuess < targetNumber) {
                    System.out.println("🔻 Too low!");
                } else {
                    System.out.println("🔺 Too high!");
                }
            }

            if (!isGuessed) {
                System.out.println("😞 You've used all attempts. The correct number was " + targetNumber + ".");
            }

            // Ask if the player wants to play again
            System.out.print("\nDo you want to play another round? (yes/no): ");
            scanner.nextLine(); // consume newline
            String response = scanner.nextLine().trim().toLowerCase();
            playAgain = response.equals("yes");
        }

        System.out.println("\n🏁 Game Over! Your final score is: " + totalScore);
        scanner.close();
    }
}