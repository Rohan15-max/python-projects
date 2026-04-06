import random

print("🎮 Number Guessing Game by Babita")
print("Choose difficulty: easy / hard")

level = input("Enter level: ")

if level == "easy":
    number = random.randint(1, 10)
    max_attempts = 7
else:
    number = random.randint(1, 50)
    max_attempts = 5

attempts = 0

while True:
    guess_input = input("Guess the number: ")

    # input validation
    if not guess_input.isdigit():
        print("❌ Please enter a valid number!")
        continue

    guess = int(guess_input)
    attempts += 1

    # hint system
    diff = abs(guess - number)

    if guess > number:
        print("Too high 👇")
    elif guess < number:
        print("Too low 👆")
    else:
        score = 100 - (attempts * 10)
        print("🎉 Correct!")
        print("Attempts:", attempts)
        print("⭐ Score:", score)
        break

    if diff <= 2:
        print("🔥 Very close!")
    elif diff <= 5:
        print("🙂 Close!")
    else:
        print("❄️ Far away!")

    if attempts >= max_attempts:
        print("❌ Game Over!")
        print("Correct number was:", number)
        break

# play again feature
play = input("Play again? (yes/no): ")

if play == "yes":
    print("Restart the program to play again 👍")
else:
    print("Thanks for playing! 🎮")
    