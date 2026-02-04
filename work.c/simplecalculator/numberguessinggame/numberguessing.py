import random

print("🎯 Welcome to the Number Guessing Game!")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("\nI have chosen a number between 1 and 100.")
    print("You have", max_attempts, "attempts. Good luck! 🍀")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low ⬆️")

        elif guess > secret_number:
            print("Too high ⬇️")

        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

    else:
        print(f"❌ Game Over! The number was {secret_number}")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing! 👋")
        break

     