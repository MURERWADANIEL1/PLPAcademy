# 🎉 Welcome to the Fun Calculator! 🎉
# We're going to add, subtract, multiply, and divide two numbers like a boss! 😎

# Step 1: Ask the user to input the first number
# We're using 'float()' to make sure our numbers can have decimals too. Fancy, right? ✨
num1 = float(input("Enter the first number: "))

# Step 2: Ask the user to input the second number
# Same trick here—using 'float()' for decimal magic! 🧙‍♂️
num2 = float(input("Enter the second number: "))

# Step 3: Time to do some math! 🧠 Let's compute the sum, difference, product, and quotient.

# Add the two numbers (Yay! Addition is the first step to fun!) ➕
sum_result = num1 + num2
print(f"The sum is: {sum_result}")

# Subtract the second number from the first (Negative vibes, but necessary! 😜) ➖
difference_result = num1 - num2
print(f"The difference is: {difference_result}")
# Multiply the two numbers (More bang for your buck! 💥) ✖️
product_result = num1 * num2
print(f"The product is: {product_result}")
# Divide the first number by the second (Be careful with zero here, no math disasters! 😅) ➗

if num2 ==0:
    print("Oops! You can't divide by zero. Let's try that again with a different number! 🚫")
    
else:
    quotient_result=num1/num2
    print(f"The quotient is: {quotient_result:.2f}")

    
# We'll assume the user is being responsible and not dividing by zero for✖