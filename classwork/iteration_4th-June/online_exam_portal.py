# ---------------------------------------------------------
# Program: Online Exam Portal
# Description:
# A student must score at least 40 marks to pass.
# The program keeps asking for marks until the student
# scores 40 or more.
# Input validation ensures marks are between 0 and 100.
# ---------------------------------------------------------

PASS_MARKS = 40

print("Online Assessment Portal")

while True:

    # Accept marks from user
    marks = int(input("Enter Marks: "))

    # Validate marks range
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
        continue

    # Check result
    if marks >= PASS_MARKS:
        print("Result: Pass")
        print("Congratulations! You have cleared the assessment.")
        break
    else:
        print("Result: Fail")
        print("Please try again.\n")