import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index + 1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice


score = 0
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "correct answer"
    else:
        result = "incorrect answer"

    message = f"{index + 1}. Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']} ({result})"
    print(message)

percent_score = float(score / len(data) * 100)
print("your score is", score, "/", len(data), "which is", percent_score, "%")
print("goodbye!")
