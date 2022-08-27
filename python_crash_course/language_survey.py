from survey import AnonymousSurvey

question = "What is your name?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()

while True:
    response = input("Here - ")
    if response == "q":
        break
    else:
        my_survey.store_response(response)

my_survey.show_results()
