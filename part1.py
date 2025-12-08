# Task 1: Print the square of numbers from 6 to 19 using a for loop
for num in range(6, 20):  # Loop from 6 to 19
    square = num ** 2     # Calculate the square of the current number
    print(f"Square of {num} is {square}")

# Task 2: Define a function to check grades
def check_grades(grades):
    """
    Takes a list of grades.
    Prints 'Pass' if grade >= 81, else prints 'Try again'.
    """
    for grade in grades:  # Loop through each grade in the list
        if grade >= 81:   # Check if grade is 81 or more
            print(f"{grade}: Pass")  # Print Pass
        else:
            print(f"{grade}: Try again")  # Print Try again


grades_list = [90, 78, 85, 60, 92]  # Sample grades
check_grades(grades_list)  # Call the function with the sample list


# Task 3: Count vowels in a string
def count_vowels(text):
    """
    Counts the total number of vowels in a string.
    Also prints how many times each vowel appears.
    """
    vowels = "aeiou"  # Define vowels
    text_lower = text.lower()  # Convert text to lowercase for uniformity
    total_count = 0  # Initialize total vowel count
    vowel_counts = {}  # Dictionary to store counts of each vowel

    for vowel in vowels:  # Loop through each vowel
        count = text_lower.count(vowel)  # Count occurrences of the vowel
        vowel_counts[vowel] = count  # Store in dictionary
        total_count += count  # Add to total count

    print(f"Total vowels: {total_count}")  # Print total vowels
    for vowel, count in vowel_counts.items():  # Print count per vowel
        print(f"{vowel}: {count}")

# String to analyze
text = "Data science is the civil engineering of data.  Cathy O’Neil & Rachel Schutt"
count_vowels(text)  # Call the function


# Task 4: Collect numbers from the user and calculate total and average
numbers = []  # Initialize empty list to store numbers

while True:  # Start an infinite loop
    user_input = input("Enter a number (or 'done' to finish): ")  # Ask user for input
    if user_input.lower() == "done":  # Stop if user enters 'done'
        break
    elif user_input.isdigit():  # Check if input is a positive whole number
        numbers.append(int(user_input))  # Convert input to int and add to the list
    else:
        print("Invalid input. Try again.")  # Inform user about invalid input

if numbers:  # Check if the list is not empty
    total_values = len(numbers)  # Number of values entered
    average = round(sum(numbers) / total_values, 2)  # Calculate average
    print(f"Total values entered: {total_values}")
    print(f"Average: {average}")
else:
    print("No numbers were entered.")  # If list is empty


# Task 5: Calculate total purchases per customer
purchases = [("Alice", 120), ("Bob", 80), ("Alice", 50), ("Bob", 20), ("Clara", 200)]
total_per_customer = {}  # Dictionary to store total spending

for name, amount in purchases:  # Loop through each purchase
    if name in total_per_customer:  # If customer already exists
        total_per_customer[name] += amount  # Add to existing total
    else:
        total_per_customer[name] = amount  # Initialize total for new customer

# Print total spent per customer
for customer, total in total_per_customer.items():
    print(f"{customer} spent ${total}")
