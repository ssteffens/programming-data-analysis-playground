import datetime

today = datetime.datetime.today()

# integer value of weekday (0 = Monday, 1 = Tuesday, etc.)
dayofweek = today.weekday()

print("Let's check if it's Tuesday.")

if dayofweek == 1:
    print("It's Tuesday!")
elif dayofweek == 0:
    print("It's not Tuesday.")
    print("Luckily, it will be Tuesday tomorrow")
else:
    print("Unfortunately it's not Tuesday.")

print("Thanks for checking if it's Tuesday.")
