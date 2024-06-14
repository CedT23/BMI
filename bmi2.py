# Calculate BMI
def bodymassindex(height, weight):
    return round((weight / height**2),2)

 # Taking user input
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

print("Welcome to the BMI calculator.")

# Print the result
bmi = bodymassindex(height, weight)
print("Your BMI is: ", bmi)

#BMI category
if bmi <= 18.5:
    print("You are underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")
