import random

print("Number guessing game")

number = random.randint(1, 20)

chances = 0

print("Guess a number (between 1 and 20):")

while True:

  guess = int(input())

  if guess == number:
    print(f"Congrulations! You have guessed the {number} in {chances} attempts!")
    break

  elif guess < number:
    print("Mmmm, your guess was too low... Please, try a number higher than that", guess)

  else:
    print("I'm sorry, but your guess was too high... Please, try a number lower than", guess)

  chances += 1
