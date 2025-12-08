# Task 1: Print the square of numbers from 6 to 19 using a for loop
for num in range(6, 20):  # Loop from 6 to 19
    square = num ** 2     # Calculate the square of the current number
    print(f"Square of {num} is {square}")

output : 
Square of 6 is 36
Square of 7 is 49
Square of 8 is 64
Square of 9 is 81
Square of 10 is 100
Square of 11 is 121
Square of 12 is 144
Square of 13 is 169
Square of 14 is 196
Square of 15 is 225
Square of 16 is 256
Square of 17 is 289
Square of 18 is 324
Square of 19 is 361

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

output : 
90: Pass
78: Try again
85: Pass
60: Try again
92: Pass

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

output :
Total vowels: 24
a: 6
e: 8
i: 7
o: 2
u: 1


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

output :
Enter a number (or 'done' to finish):
Invalid input. Try again.
Enter a number (or 'done' to finish): 
Invalid input. Try again.
Enter a number (or 'done' to finish): 2
Enter a number (or 'done' to finish): 3
Enter a number (or 'done' to finish): 8
Enter a number (or 'done' to finish): done
Total values entered: 3
Average: 4.33


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

output :
Alice spent $170
Bob spent $100
Clara spent $200

Task 6:

import requests  # Used to call the World Bank API

# Loop through years 2010 to 2020
for year in range(2010, 2021):

    # Build API URL for each year
    url = f"https://api.worldbank.org/v2/country/RO/indicator/SP.POP.TOTL?format=json&date={year}"

    # Send request to World Bank API
    response = requests.get(url)

    # Convert JSON response to Python data structure
    data = response.json()

    # Extract population value from JSON
    population = data[1][0]["value"]

    # Print results in clean format
    print("Country: Tuvalu")
    print("Year:", year)
    print("Population:", population)
    print("---------------------------")



output :

Country: Tuvalu
Year: 2010
Population: 20246871
---------------------------
Country: Tuvalu
Year: 2011
Population: 20147528
---------------------------
Country: Tuvalu
Year: 2012
Population: 20058035
---------------------------
Country: Tuvalu
Year: 2013
Population: 19983693
---------------------------
Country: Tuvalu
Year: 2014
Population: 19908979
---------------------------
Country: Tuvalu
Year: 2015
Population: 19815616
---------------------------
Country: Tuvalu
Year: 2016
Population: 19702267
---------------------------
Country: Tuvalu
Year: 2017
Population: 19588715
---------------------------
Country: Tuvalu
Year: 2018
Population: 19473970
---------------------------
Country: Tuvalu
Year: 2019
Population: 19371648
---------------------------
Country: Tuvalu
Year: 2020
Population: 19265250
---------------------------


