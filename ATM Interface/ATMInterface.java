import java.util.Scanner;

// BankAccount class: manages account balance
class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        this.balance = initialBalance;
    }

    public double getBalance() {
        return balance;
    }

    public boolean withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            return true;
        }
        return false;
    }

    public boolean deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            return true;
        }
        return false;
    }
}

// ATM class: provides ATM functionalities
class ATM {
    private BankAccount account;
    private Scanner scanner;

    public ATM(BankAccount account) {
        this.account = account;
        this.scanner = new Scanner(System.in);
    }

    public void start() {
        int option;
        do {
            System.out.println("\n🏧 ATM Menu:");
            System.out.println("1. 💸 Withdraw");
            System.out.println("2. 💰 Deposit");
            System.out.println("3. 📈 Check Balance");
            System.out.println("4. ❌ Exit");
            System.out.print("Choose an option (1-4): ");
            option = scanner.nextInt();

            switch (option) {
                case 1:
                    handleWithdraw();
                    break;
                case 2:
                    handleDeposit();
                    break;
                case 3:
                    handleCheckBalance();
                    break;
                case 4:
                    System.out.println("👋 Thank you for using the ATM. Goodbye!");
                    break;
                default:
                    System.out.println("⚠️ Invalid option. Please try again.");
            }
        } while (option != 4);
    }

    private void handleWithdraw() {
        System.out.print("Enter amount to withdraw: ₹");
        double amount = scanner.nextDouble();
        if (account.withdraw(amount)) {
            System.out.println("✅ Withdrawal successful. Remaining balance: ₹" + account.getBalance());
        } else {
            System.out.println("❌ Insufficient funds or invalid amount.");
        }
    }

    private void handleDeposit() {
        System.out.print("Enter amount to deposit: ₹");
        double amount = scanner.nextDouble();
        if (account.deposit(amount)) {
            System.out.println("✅ Deposit successful. Current balance: ₹" + account.getBalance());
        } else {
            System.out.println("❌ Invalid deposit amount.");
        }
    }

    private void handleCheckBalance() {
        System.out.println("📊 Your current balance is: ₹" + account.getBalance());
    }
}

// Main class to run the program
public class ATMInterface {
    public static void main(String[] args) {
        // Initialize with ₹5000
        BankAccount account = new BankAccount(5000.0);
        ATM atm = new ATM(account);
        atm.start();
    }
}