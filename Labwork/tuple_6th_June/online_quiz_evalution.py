# ---------------------------------------------------------
# Program: Online Quiz Evaluation
# ---------------------------------------------------------

correct = ['A', 'C', 'B', 'D', 'A']
student = ['A', 'B', 'B', 'D', 'C']

score = 0
correct_count = 0
wrong_count = 0
incorrect_questions = []

# Compare answers
for i in range(len(correct)):

    if student[i] == correct[i]:
        score += 1
        correct_count += 1
    else:
        wrong_count += 1
        incorrect_questions.append(i + 1)   # Question numbers start from 1

# Calculate percentage
percentage = (score / len(correct)) * 100

# Determine result
if percentage >= 60:
    result = "PASS"
else:
    result = "FAIL"

# Display results
print("Score:", score, "/", len(correct))
print("Correct Answers:", correct_count)
print("Wrong Answers:", wrong_count)
print("Incorrect Question Numbers:", incorrect_questions)
print("Percentage:", percentage, "%")
print("Result:", result)