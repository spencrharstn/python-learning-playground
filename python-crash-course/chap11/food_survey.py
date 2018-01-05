from survey import AnonymousSurvey

# Define a question and make a survey
question = "What is your favorite food?"
my_survey = AnonymousSurvey(question)

#Show the question, and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Food: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results
print("Thanks for participating in the survey!")
my_survey.show_results()