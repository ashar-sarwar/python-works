import unittest
class survey():
    def __init__(self,question):
       self.question=question
       self.responses=[]

    def show_ques(self):
        print(self.question)

    def store_response(self,new_response):
        self.responses.append(new_response)

    def show_result(self):
        print("Survey results:")
        for response in self.responses:
            print("- " + response)


question = "What language did you first learn to speak?"
my_survey = survey(question)

print("enter q anytime too quit")

while True:
    response=input("Language:")
    if response=='q':
        break

    my_survey.store_response(response)

print("Jani shukria ")
my_survey.show_result()

class Testsurvey(unittest.TestCase):

    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey=survey(question)
        my_survey.store_response('english')
        self.assertIn('english',my_survey.responses)


    def test_store_multi_response(self):
      print("Enter 'q' to quit")
      question = "What language did you first learn to speak?"
      while True:
        my_survey=survey(question)
        lang=input("Language: ")
        if lang=='q':
            break
        my_survey.store_response(lang)

      self.assertIn('q',lang,my_survey.responses)


unittest.main()