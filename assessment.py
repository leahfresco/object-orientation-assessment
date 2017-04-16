"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   - Abstraction: The ability to use a class or method that one does not know
   the exact details of how it works but can use it regardless. Being able to
   use something based on its functionality and not implementation.
   - Polymorphism: See also inheritance. The idea that one object can be similar
   to another object and inherit all or some of its functionality.
   - Encapsulation: Keeping data close to where it needs be used.

2. What is a class? A class is a set of attributes and methods for a certain 
functionality.

3. What is an instance attribute? An variable associate with a specific instance
of a class.

4. What is a method? A method is a function internal to a certain class (and
    its subclasses). 

5. What is an instance in object orientation? An instance is one specific
version of a class created within a program.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is an attribute shared by all instances of a certain class
   while an instance attribute is instantiated with every new instance of a class.
   An example is that a Dog class has a class attribute for species ("dog") while
   an instance variable for the Dog class could be age which is instantiated with
   every new Dog created.

"""
# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
    """ A Student that has a first, last name and address """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __repr__(self):
        return self.first_name + " " + self.last_name

class Question(object):
    """ A question and its corresponding answer """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        return "Q: {} \nA: {}".format(self.question, self.answer)

    def ask_and_evaluate(self):
        """ Asks question and returns if user got the answer right """
        user_answer = raw_input(self.question + " > ")
        if user_answer == self.answer:
            return True
        else:
            return False

class Exam(object):
    """ A named exam and its questions """

    def __init__(self, name):
        self.name = name
        self.questions = []

    def __repr__(self):
        return "{} Exam".format(self.name)

    def add_question(self, question, correct_answer):
        """ Adds question to list of exam questions 

        Takes inputs question and correct answer to create
        new question.
        """
        # Create new Question and appends it to list of questions
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        """ Administers all of exams questions and return score

        Returns score as a percentage of correct correct answers
        """

        correct_answers = 0 # Keep track of total correct answers

        # Loop through each question and perform the ask and evaluate
        # method from the Question class to determine correctness
        for question in self.questions:
            if question.ask_and_evaluate():
                correct_answers += 1

        # Return correct answers divided by total questions multiplied
        # by 100 to represent score
        return (float(correct_answers)/len(self.questions)) * 100

class StudentExam(object):
    """ A student and their score for an exam """

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def __repr__(self):
        if not self.score:
            return "{} did not take {} yet".format(self.student, self.exam)
        else:
            return "{} completed {} with a score {}".format(self.student, self.exam, self.score)

    def take_test(self):
        """ Administers exam to student and prints score """
        self.score = self.exam.administer()
        print "{}'s score: {}".format(self.student, self.score)

def example():
    assessment = Exam('Assessment')
    assessment.add_question("What gets wetter the more it dries?", "a towel")
    assessment.add_question("What goes up and down but remains in the same place?", "stairs")
    assessment.add_question("What am I?", "instance of a question")
    star_student = Student("Leah", "Y", "Hackbright, San Francisco")
    student_assessment = StudentExam(star_student, assessment)
    student_assessment.take_test()

class Quiz(Exam):
    """ An quiz that only has a pass or fail instead of a percent score """

    def __repr__(self):
        return "{} Quiz".format(self.name)

    def administer(self):
        """ Administers all of quiz questions and returns a pass or fail

        Returns score as a 1 for passing or 0 for failing
        """

        correct_answers = 0 # Keep track of total correct answers

        # Loop through each question and perform the ask and evaluate
        # method from the Question class to determine correctness
        for question in self.questions:
            if question.ask_and_evaluate():
                correct_answers += 1

        # Return correct answers divided by total questions multiplied
        # by 100 to represent score
        percent_score = (float(correct_answers)/len(self.questions)) * 100

        # Translate the percent score to a pass or fail
        if percent_score >= 50:
            self.score = 1
        else:
            self.score = 0

        return self.score

class StudentQuiz(StudentExam):
    """ A student and their pass or fail score 

    A score of 1 indicates passing quiz and a 0 indicated a failed quiz
    """

    def __repr__(self):
        if not self.score:
            return "{} did not take {} yet".format(self.student, self.exam)
        elif self.score == 1:
            return "{} passed {}".format(self.student, self.exam)
        else:
            return "{} failed {}".format(self.student, self.exam)

    def take_test(self):
        """ Administers test to student and prints results """
        self.score = self.exam.administer()
        if self.score == 1:
            print "{} passed.".format(self.student)
        else:
            print "{} failed.".format(self.student)


def quiz_example():
    assessment = Quiz('Quiz')
    assessment.add_question("What gets wetter the more it dries?", "a towel")
    assessment.add_question("What goes up and down but remains in the same place?", "stairs")
    assessment.add_question("What am I?", "instance of a question")
    star_student = Student("Leah", "Y", "Hackbright, San Francisco")
    student_assessment = StudentQuiz(star_student, assessment)
    student_assessment.take_test()





