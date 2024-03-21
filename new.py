import random
import math

# Input Lower Number
lower = int(input("Enter Lower bound:- "))

# Input Higher Number
upper = int(input("Enter Upper bound:- "))

# Generate random number between
# the lower and upper number
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")

# Number of guesses
count = 0

# to calculate the minimum number of guesses
# depending on the range
while count < math.log(upper - lower + 1, 2):
      count += 1

# guess input
      guess = int(input("Guess a number:- "))

# test the condition
      if x == guess:
            print("Congratulations you did it in ",
                  count, " try")
      # once guessed right, the condition breaks
            break
      elif x > guess:
            print("You guessed too low!")
      elif x < guess:
            print("You guessed too high!")

# Output if guessing is more than required guesses
if count >= math.log(upper - lower + 1, 2):
      print("\nThe number is %d" % x)
      print("\tBetter Luck Next time!")
