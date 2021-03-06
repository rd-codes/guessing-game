import random

print("Number guessing game")

# generate random integers from 1 to 20
number = random.randint(1, 20)

chances = 0

print("Guess a number (between 1 and 20):")

# while loop will help to count the number of chances
while True:

  #user will enter a number from 1 to 20
  guess = int(input())

  # if number entered by the user is the same as the generated by the random randit, 
  # then we break the loop
  if guess == number:
    print(f"Congrulations! You have guessed the {number} in {chances} attempts!")
    break
    
  # if number guessed by the user was lower than the one generated, 
  # ask user to repeate with a higher number
  elif guess < number:
    print("Mmmm, your guess was too low... Please, try a number higher than that", guess)

  # user's number greater than the generated one
  else:
    print("I'm sorry, but your guess was too high... Please, try a number lower than", guess)

   # increment the value of a chance by 1 for every try
  chances += 1
