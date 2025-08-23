
'''
# Age Group Categorization classify a person's age group: Child(<13), Teenager(13-19), Adult (20-59), Senior(60+)

your_Age = int(input("Enter Your Age: "))
if your_Age < 13:
    print("Your are a Child.")
elif your_Age <= 19:
    print("Your are a Teenager.")
elif your_Age <= 59:
    print("Your are a Adult.")
else: 
    print("Your are a Senior.")
'''

'''
# Movie Ticket Pricing: Price based on age: $12 for Adults(18 and over). $ 8 for children. Everyone gets a $2 discount on wednesday.
your_Age = int(input("Enter Your Age: "))
day = input("Enter day: ")

price = 12 if your_Age >= 18 else 8
if day == "wednesday":
    price = price - 2

print("Your ticket price is: ", price)
'''

'''
# Grade Calculator: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60) 
marks = int(input("Enter your marks:"))
if marks < 0 or marks > 100:
    print("Invalid Marks! Please enter between 0-100.")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")
'''

# Fruit ripeness checker: banana: Green- Unripe, Yellow-Ripe, Brown - Overripe 
friut
# Weather activity Suggestion: sunny - Go for a walk, rainy- read a book, snowy - Build a snowman 
# Transportation Mode Selection: < 3km → Walk, 3–15km → Bike/Car, 15–200 km → Bus/Train, > 200km → Flight
# Coffe Cusomization: small, medium, large, sugar, extra sugar, no sugar
# Password Strength Checker: weak, medium, strong. <6 (week), 6-10 (medium), 10 (Strong)
# Leap Year Checker: %4 !%100 ,%400
# Pet Food Recommendation: dog < 2 = Puppy food, Cat > 5 = Senior cat food