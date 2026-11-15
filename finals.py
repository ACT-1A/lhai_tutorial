# ==========================================================
# PRELIM TO FINALS TUTORIAL
# PYTHON LEARNING SYSTEM
# ==========================================================
import random

# ----------------------------------------------------------
# LESSON DATABASE
# ----------------------------------------------------------
lessons = {
    "PRELIM": [
        {
            "title": "Introduction to Python",
            "content": """
WHAT IS PROGRAMMING?
Programming is the process of giving instructions
to a computer to perform specific tasks.

WHAT IS A PROGRAMMING LANGUAGE?
A programming language is used to communicate
instructions to a computer.

WHAT IS PYTHON?
Python is a high-level, beginner-friendly
programming language.

WHO CREATED PYTHON?
Python was created by Guido van Rossum.
It was first released in 1991.

WHY LEARN PYTHON?
- Easy to learn
- Simple syntax
- Used in web development
- Used in artificial intelligence
- Used in automation and data analysis

WHAT DO YOU NEED?
- Computer
- Python interpreter
- Code editor such as VS Code
"""
        },
        {
            "title": "Python Basic Syntax",
            "content": """
WHAT IS PYTHON SYNTAX?
Syntax refers to the rules for writing
valid Python instructions.

1. CASE SENSITIVITY
Python distinguishes uppercase and lowercase letters.

CORRECT:
    name = "Student"
    print(name)

INCORRECT:
    name = "Student"
    print(Name)

Name and name are different variables.

2. INDENTATION
Indentation means adding spaces before a line
of code to show its block or structure.

CORRECT:
    age = 18
    if age >= 18:
        print("You are an adult.")

INCORRECT:
    age = 18
    if age >= 18:
    print("You are an adult.")

The incorrect example causes an IndentationError.

3. PRINTING OUTPUT
The print() function displays information.

Example:
    print("Hello, Student!")
    print("Welcome to Python!")

OUTPUT:
    Hello, Student!
    Welcome to Python!

4. PYTHON COMMENTS
Comments are notes written inside the code.
Python does not execute comments.

Example:
    # This is a comment
    print("Hello!")

The # symbol creates a single-line comment.
"""
        },
        {
            "title": "Variables, Constants and Data Types",
            "content": """
WHAT IS A VARIABLE?
A variable stores information that can be
used and changed while the program runs.

Example:
    name = "John"
    age = 20

WHAT IS A CONSTANT?
A constant is a value intended to remain unchanged.
Python uses uppercase naming by convention.

Example:
    PI = 3.14159

COMMON PYTHON DATA TYPES:

1. STRING (str) - Text
    name = "John"

2. INTEGER (int) - Whole numbers
    age = 20

3. FLOAT (float) - Decimal numbers
    height = 1.75

4. BOOLEAN (bool) - True or False
    is_student = True

VARIABLE DECLARATION:

Example:
    student_name = "Maria"
    student_age = 19

    print(student_name)
    print(student_age)

Python automatically identifies the data type
based on the assigned value.
"""
        },
        {
            "title": "Basic Input and Output",
            "content": """
WHAT IS INPUT?
Input allows the user to enter information.

WHAT IS OUTPUT?
Output displays information to the user.

ACCEPTING USER INPUT:

Example:
    name = input("Enter your name: ")
    print("Hello", name)

CONVERTING INPUT TO OTHER DATA TYPES:
The input() function normally returns a string.

To convert it:
    age = int(input("Enter your age: "))
    height = float(input("Enter your height: "))

    print("Age:", age)
    print("Height:", height)

REMEMBER:
int() converts to an integer.
float() converts to a decimal number.
str() converts to a string.
"""
        }
    ],

    "MIDTERM": [
        {
            "title": "Arithmetic Operators and Expressions",
            "content": """
WHAT ARE ARITHMETIC OPERATORS?
These operators perform mathematical calculations.

OPERATOR TABLE:
    +   Addition
    -   Subtraction
    *   Multiplication
    /   Division
    //  Floor Division
    %   Modulus (Remainder)
    **  Exponentiation

EXAMPLE:
    a = 10
    b = 3

    print(a + b)    # 13
    print(a - b)    # 7
    print(a * b)    # 30
    print(a / b)    # 3.333...
    print(a // b)   # 3
    print(a % b)    # 1
    print(a ** b)   # 1000

WHAT IS AN EXPRESSION?
An expression combines values and operators
to produce a result.

Example:
    result = (10 + 5) * 2
    print(result)

OUTPUT:
    30
"""
        },
        {
            "title": "Relational Operators",
            "content": """
WHAT ARE RELATIONAL OPERATORS?
These operators compare two values.
The result is either True or False.

OPERATORS:
    ==  Equal to
    !=  Not equal to
    >   Greater than
    <   Less than
    >=  Greater than or equal to
    <=  Less than or equal to

EXAMPLE:
    a = 10
    b = 5

    print(a == b)   # False
    print(a != b)   # True
    print(a > b)    # True
    print(a < b)    # False
    print(a >= b)   # True
    print(a <= b)   # False
"""
        },
        {
            "title": "The If Statement",
            "content": """
WHAT IS AN IF STATEMENT?
It executes a block of code when a condition is True.

EXAMPLE:
    age = 18

    if age >= 18:
        print("You are an adult.")

OUTPUT:
    You are an adult.

If the condition is False, the code inside
the if statement will not execute.
"""
        },
        {
            "title": "The If-Else Statement",
            "content": """
WHAT IS AN IF-ELSE STATEMENT?
It provides two possible paths.

- IF: Executes when the condition is True.
- ELSE: Executes when the condition is False.

EXAMPLE:
    age = 16

    if age >= 18:
        print("You are eligible.")
    else:
        print("You are not eligible.")

OUTPUT:
    You are not eligible.
"""
        },
        {
            "title": "The If-Elif-Else Statement",
            "content": """
WHAT IS IF-ELIF-ELSE?
It allows a program to check multiple conditions.

- IF checks the first condition.
- ELIF checks another condition.
- ELSE executes when none of the conditions are True.

EXAMPLE:
    grade = 85

    if grade >= 90:
        print("Excellent")
    elif grade >= 80:
        print("Very Good")
    elif grade >= 75:
        print("Passed")
    else:
        print("Failed")

OUTPUT:
    Very Good
"""
        },
        {
            "title": "Nested Conditional Statements",
            "content": """
WHAT IS A NESTED CONDITION?
A nested condition is an if statement
placed inside another if statement.

EXAMPLE:
    age = 20
    has_id = True

    if age >= 18:
        if has_id:
            print("Access granted.")
        else:
            print("Please present your ID.")
    else:
        print("Access denied.")

OUTPUT:
    Access granted.

The second condition is checked only
when the first condition is True.
"""
        }
    ],

    "FINALS": [
        {
            "title": "Introduction to Logical Operators",
            "content": """
WHAT ARE LOGICAL OPERATORS?
Logical operators combine or reverse conditions.

There are three main logical operators:

1. AND
Both conditions must be True.

2. OR
At least one condition must be True.

3. NOT
Reverses the Boolean result.

EXAMPLE:
    age = 20
    has_id = True

    print(age >= 18 and has_id)

OUTPUT:
    True
"""
        },
        {
            "title": "AND, OR and NOT Truth Tables",
            "content": """
AND TRUTH TABLE

    A       B       RESULT
    True    True    True
    True    False   False
    False   True    False
    False   False   False

OR TRUTH TABLE

    A       B       RESULT
    True    True    True
    True    False   True
    False   True    True
    False   False   False

NOT TRUTH TABLE

    A       RESULT
    True    False
    False   True

PYTHON EXAMPLES:
    print(True and False)
    print(True or False)
    print(not True)

OUTPUT:
    False
    True
    False
"""
        },
        {
            "title": "Introduction to Iteration and Loops",
            "content": """
WHAT IS ITERATION?
Iteration means repeating a set of instructions
until a certain condition is met.

WHAT ARE LOOPS?
Loops allow a program to execute the same
instructions multiple times.

TWO COMMON TYPES OF LOOPS:

1. FOR LOOP
Used when iterating through a sequence
or a known range of values.

2. WHILE LOOP
Repeats as long as a condition remains True.
"""
        },
        {
            "title": "Python For Loop",
            "content": """
WHAT IS A FOR LOOP?
A for loop repeats code for each item
in a sequence.

EXAMPLE:
    for number in range(1, 6):
        print(number)

OUTPUT:
    1
    2
    3
    4
    5

range(1, 6) generates numbers from 1 to 5.

ANOTHER EXAMPLE:
    fruits = ["Apple", "Banana", "Mango"]

    for fruit in fruits:
        print(fruit)

The loop prints each item in the list.
"""
        },
        {
            "title": "Python While Loop",
            "content": """
WHAT IS A WHILE LOOP?
A while loop repeats a block of code
while its condition is True.

EXAMPLE:
    number = 1

    while number <= 5:
        print(number)
        number += 1

OUTPUT:
    1
    2
    3
    4
    5

The number increases by 1 every time
the loop executes.

When number becomes 6, the condition
becomes False and the loop stops.

IMPORTANT:
Always make sure the condition can
eventually become False to avoid
an infinite loop.
"""
        }
    ]
}

# ----------------------------------------------------------
# LEARNING PROGRESS
# ----------------------------------------------------------
completed_lessons = []


# ----------------------------------------------------------
# DISPLAY A LESSON
# ----------------------------------------------------------
def display_lesson(section, index):
    lesson = lessons[section][index]

    print("\n" + "=" * 55)
    print("LESSON:", lesson["title"])
    print("=" * 55)
    print(lesson["content"])
    print("=" * 55)

    answer = input("Would you like to try a code demonstration? (y/n): ")

    if answer.lower() == "y":
        run_demo(lesson["title"])

    if lesson["title"] not in completed_lessons:
        completed_lessons.append(lesson["title"])
        print("\nLesson marked as completed!")

    input("\nPress ENTER to return...")


# ----------------------------------------------------------
# CODE DEMONSTRATIONS
# ----------------------------------------------------------
def run_demo(title):
    print("\n===== CODE DEMONSTRATION =====")

    if title == "Introduction to Python":
        print("Hello, Student!")
        print("Welcome to Python Programming!")

    elif title == "Python Basic Syntax":
        name = "Student"
        print("Hello", name)

        age = 18
        if age >= 18:
            print("You are an adult.")

    elif title == "Variables, Constants and Data Types":
        name = "Maria"
        age = 19
        height = 1.65
        is_student = True
        PI = 3.14159

        print("Name:", name)
        print("Age:", age)
        print("Height:", height)
        print("Student:", is_student)
        print("PI:", PI)

        print("\nData Types:")
        print(type(name))
        print(type(age))
        print(type(height))
        print(type(is_student))

    elif title == "Basic Input and Output":
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))

        print("Hello", name)
        print("Your age is", age)

    elif title == "Arithmetic Operators and Expressions":
        a = 10
        b = 3

        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b)
        print("Floor Division:", a // b)
        print("Modulus:", a % b)
        print("Exponentiation:", a ** b)

    elif title == "Relational Operators":
        a = 10
        b = 5

        print("10 == 5:", a == b)
        print("10 != 5:", a != b)
        print("10 > 5:", a > b)
        print("10 < 5:", a < b)
        print("10 >= 5:", a >= b)
        print("10 <= 5:", a <= b)

    elif title == "The If Statement":
        age = int(input("Enter your age: "))

        if age >= 18:
            print("You are an adult.")

    elif title == "The If-Else Statement":
        age = int(input("Enter your age: "))

        if age >= 18:
            print("You are eligible.")
        else:
            print("You are not eligible.")

    elif title == "The If-Elif-Else Statement":
        grade = int(input("Enter your grade: "))

        if grade >= 90:
            print("Excellent!")
        elif grade >= 80:
            print("Very Good!")
        elif grade >= 75:
            print("Passed!")
        else:
            print("Failed!")

    elif title == "Nested Conditional Statements":
        age = int(input("Enter your age: "))
        has_id = input("Do you have an ID? (yes/no): ")

        if age >= 18:
            if has_id.lower() == "yes":
                print("Access granted!")
            else:
                print("Please present your ID.")
        else:
            print("Access denied!")

    elif title == "Introduction to Logical Operators":
        age = 20
        has_id = True

        print("AND:", age >= 18 and has_id)
        print("OR:", age >= 18 or has_id)
        print("NOT:", not has_id)

    elif title == "AND, OR and NOT Truth Tables":
        print("\nAND:", True and False)
        print("OR:", True or False)
        print("NOT:", not True)

    elif title == "Introduction to Iteration and Loops":
        for number in range(1, 4):
            print("Iteration:", number)

    elif title == "Python For Loop":
        for number in range(1, 6):
            print(number)

    elif title == "Python While Loop":
        number = 1

        while number <= 5:
            print(number)
            number += 1


# ----------------------------------------------------------
# SECTION MENU
# ----------------------------------------------------------
def section_menu(section):
    while True:
        print("\n" + "=" * 55)
        print(section + " - LESSON MENU")
        print("=" * 55)

        for i, lesson in enumerate(lessons[section], start=1):
            status = "[COMPLETED]" if lesson["title"] in completed_lessons else ""
            print(f"{i}. {lesson['title']} {status}")

        print("0. Back to Main Menu")

        choice = input("\nSelect a lesson: ")

        if choice == "0":
            break

        if choice.isdigit() and 1 <= int(choice) <= len(lessons[section]):
            display_lesson(section, int(choice) - 1)
        else:
            print("Invalid selection. Please try again.")


# ----------------------------------------------------------
# ALL LESSONS
# ----------------------------------------------------------
def all_lessons():
    print("\n===== ALL LESSONS =====")

    for section in ["PRELIM", "MIDTERM", "FINALS"]:
        print("\nNOW STUDYING:", section)

        for index in range(len(lessons[section])):
            display_lesson(section, index)


# ----------------------------------------------------------
# PYTHON KNOWLEDGE QUIZ
# ----------------------------------------------------------
def knowledge_quiz():
    questions = [
        ("Who created Python?",
         ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie"], "B"),

        ("Which function displays output?",
         ["A. input()", "B. display()", "C. print()"], "C"),

        ("Which data type stores whole numbers?",
         ["A. int", "B. float", "C. str"], "A"),

        ("Which symbol is used for comments?",
         ["A. //", "B. #", "C. @"], "B"),

        ("Which operator is used for multiplication?",
         ["A. +", "B. /", "C. *"], "C"),

        ("Which statement checks a condition?",
         ["A. if", "B. print", "C. input"], "A"),

        ("Which operator requires both conditions to be True?",
         ["A. OR", "B. AND", "C. NOT"], "B"),

        ("Which loop repeats while a condition is True?",
         ["A. for", "B. if", "C. while"], "C")
    ]

    score = 0

    print("\n===== PYTHON KNOWLEDGE QUIZ =====")

    for question, options, answer in questions:
        print("\n" + question)

        for option in options:
            print(option)

        user_answer = input("Your answer: ").upper()

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect! Correct answer:", answer)

    print("\n===== QUIZ RESULT =====")
    print("Your Score:", score, "/", len(questions))

    input("\nPress ENTER to continue...")


# ----------------------------------------------------------
# MINI GAMES
# ----------------------------------------------------------
def mini_games():
    while True:
        print("\n===== MINI GAMES =====")
        print("1. Number Guessing Game")
        print("2. Mathematics Challenge")
        print("0. Back to Main Menu")

        choice = input("\nSelect a game: ")

        if choice == "1":
            secret = random.randint(1, 10)
            attempts = 3

            print("\nGuess the number from 1 to 10.")
            print("You have 3 attempts.")

            for attempt in range(attempts):
                guess = int(input("Enter your guess: "))

                if guess == secret:
                    print("Congratulations! You guessed it!")
                    break
                elif guess < secret:
                    print("Too low!")
                else:
                    print("Too high!")
            else:
                print("Game over! The number was", secret)

        elif choice == "2":
            a = random.randint(1, 20)
            b = random.randint(1, 20)

            answer = int(input(f"\nWhat is {a} + {b}? "))

            if answer == a + b:
                print("Correct! Great job!")
            else:
                print("Incorrect! The answer is", a + b)

        elif choice == "0":
            break

        else:
            print("Invalid selection.")


# ----------------------------------------------------------
# FINAL EXAMINATION
# ----------------------------------------------------------
def final_examination():
    questions = [
        ("What is the output of print(5 + 5)?", "10"),
        ("What is the data type of 3.14?", "float"),
        ("What operator means equal to?", "=="),
        ("What does 10 % 3 return?", "1"),
        ("What keyword checks another condition?", "elif"),
        ("What logical operator requires both conditions?", "and"),
        ("What is the result of not True?", "false"),
        ("Which loop uses range() commonly?", "for"),
        ("Which loop depends on a condition?", "while"),
        ("What function receives user input?", "input")
    ]

    score = 0

    print("\n" + "=" * 55)
    print("                 FINAL EXAMINATION")
    print("=" * 55)
    print("There are 10 questions.")
    print("Answer each question carefully.")

    for i, (question, answer) in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {question}")

        user_answer = input("Your answer: ").strip().lower()

        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! Correct answer:", answer)

    print("\n===== FINAL EXAMINATION RESULT =====")
    print("Score:", score, "/", len(questions))

    percentage = (score / len(questions)) * 100
    print("Percentage:", percentage, "%")

    if percentage >= 75:
        print("Congratulations! You passed the examination.")
    else:
        print("Keep studying. You can do better next time!")

    input("\nPress ENTER to continue...")


# ----------------------------------------------------------
# FINAL PROJECT
# ----------------------------------------------------------
def final_project():
    print("\n" + "=" * 55)
    print("                 FINAL PROJECT")
    print("=" * 55)

    print("""
PROJECT TITLE:
Student Grade Calculator

OBJECTIVE:
Create a simple program that accepts a student's
name and grades, calculates the average, and
determines whether the student passed or failed.

REQUIREMENTS:
1. Use variables to store student information.
2. Use input() to accept information.
3. Use float() to convert grades.
4. Use arithmetic operators to calculate the average.
5. Use if-else to determine the result.
6. Use print() to display the output.

SAMPLE CODE:

    name = input("Enter student name: ")

    grade1 = float(input("Enter first grade: "))
    grade2 = float(input("Enter second grade: "))
    grade3 = float(input("Enter third grade: "))

    average = (grade1 + grade2 + grade3) / 3

    print("Student:", name)
    print("Average:", average)

    if average >= 75:
        print("Result: PASSED")
    else:
        print("Result: FAILED")

CHALLENGE:
Improve the program by adding:
- Grade remarks
- Multiple students
- A loop for repeated calculations
- Input validation
""")

    input("\nPress ENTER to return to Main Menu...")


# ----------------------------------------------------------
# MY LEARNING PROGRESS
# ----------------------------------------------------------
def learning_progress():
    total = sum(len(lessons[section]) for section in lessons)
    completed = len(completed_lessons)

    print("\n" + "=" * 55)
    print("              MY LEARNING PROGRESS")
    print("=" * 55)

    print("Total Lessons:", total)
    print("Completed Lessons:", completed)
    print("Remaining Lessons:", total - completed)

    percentage = (completed / total) * 100
    print("Progress:", round(percentage, 2), "%")

    print("\nSECTION PROGRESS:")

    for section in lessons:
        section_total = len(lessons[section])
        section_completed = sum(
            1 for lesson in lessons[section]
            if lesson["title"] in completed_lessons
        )

        print(
            f"{section}: {section_completed}/{section_total} completed"
        )

    input("\nPress ENTER to return...")


# ----------------------------------------------------------
# MAIN MENU
# ----------------------------------------------------------
def main_menu():
    while True:
        print("\n")
        print("=" * 55)
        print("           PRELIM TO FINALS TUTORIAL")
        print("=" * 55)

        print("\nWelcome, Student!")
        print("\nChoose your learning destination:\n")

        print("1. PRELIM  - Python Fundamentals")
        print("2. MIDTERM - Operators and Conditions")
        print("3. FINALS  - Logical Operators and Loops")
        print("4. All Lessons")
        print("5. Python Knowledge Quiz")
        print("6. Mini Games")
        print("7. Final Examination")
        print("8. Final Project")
        print("9. My Learning Progress")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            section_menu("PRELIM")
        elif choice == "2":
            section_menu("MIDTERM")
        elif choice == "3":
            section_menu("FINALS")
        elif choice == "4":
            all_lessons()
        elif choice == "5":
            knowledge_quiz()
        elif choice == "6":
            mini_games()
        elif choice == "7":
            final_examination()
        elif choice == "8":
            final_project()
        elif choice == "9":
            learning_progress()
        elif choice == "0":
            print("\nThank you for using PRELIM TO FINALS TUTORIAL!")
            print("Keep learning and keep programming!")
            break
        else:
            print("\nInvalid choice! Please select from 0 to 9.")


# ----------------------------------------------------------
# RUN THE PROGRAM
# ----------------------------------------------------------
main_menu()