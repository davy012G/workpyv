#File Name: quiz.py

import random as r

#-Quiz : The beta version-
"""
class Quiz:

	def __init__(self, initial_number: int, final_number: int, number_of_questions: int) -> None:
		\"""This is the object-oriented form of my Quiz format (test_phase)...\"""
		score = 0
		print("Welcome to the My Quiz Game")

		for i in range(number_of_questions):
			q_, _a = self.questionArranger(initial_number, final_number)
			print("Question Number %d:"%(i+1), q_)
			user_input = input("Answer: ")
			
			if user_input == str(_a): #This is for the sake of one thing and that's the exit part of this condition, else it will not be like this
				score += 1
				print("Your answer was correct. Thumbs up to you")
			elif user_input == "exit":
				print("Exiting the Quiz Game...")
				break
			else:
				print("The answer to Question %d is %d"%(i+1, _a))
		
		print("Score: %d/%d \nRemark: You got a mark %s half mark. %s"%(score, number_of_questions, self.remarkGiver(score, number_of_questions), ["Try harder, you can do this", "Well Done, you really did great"][int(score > number_of_questions//2)]))

	def _questionGenerator(self, initial: int, final: int) -> tuple:
		return r.choice(["add", "subtract", "multiply", "divide"]), r.randrange(initial, final), r.randrange(initial, final)

	def questionArranger(self, initial: int, final:int) -> tuple:
		my_question, num_one, num_two = self._questionGenerator(initial, final)

		match my_question:
			case "add":
				f_question = r.choice(["Add %d and %d and the answer is"%(num_one, num_two), "What is the sum of %d and %d"%(num_one, num_two)])
				answer_to_q = num_one + num_two
			case "subtract":
				f_question = r.choice(["If I subtracted %d from %d what would I get"%(num_one, num_one + num_two), "What is the result when I do %d minus %d"%(num_one + num_two, num_one)])
				answer_to_q = num_two
			case "multiply":
				f_question = r.choice(["If I multiplied %d by %d, What would be the result"%(num_one, num_two), "%d X %d = "%(num_one, num_two)])
				answer_to_q = num_one * num_two
			case "divide":
				f_question = r.choice(["%d divided by %d is equal to "%(num_one * num_two, num_two), "When you takeaway %d from %d your answer is"%(num_two, num_one * num_two)])
				answer_to_q = num_one

		return f_question, answer_to_q

	def error_handler(self, string: str, default: int = 0) -> int: #Deluxe Version
		#unIdentified = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		#answer = 0
		try:
			answer = int(string)
		except ValueError:
			answer = default
		\"""
		#answer = 0 --> This variable was created solely for this one purpose
			for s in string:
				for no, u in enumerate(unIdentified):
					if s == u:
						answer += no
						break
		#This is part of the function is not gonna help me  
		\"""

		return answer
	
	def remarkGiver(self, initial: int, final: int) -> str:
		half_mark = round(final / 2, 0) #This makes it give the illusion of fairness

		if initial > half_mark:
			reply = r.choice(["higher than", "more than"]) 
		elif initial == half_mark:
			reply = r.choice(["equal to", "same as"])
		else:
			reply = r.choice(["lesser compared to", "inferior to"])
		
		return reply

#if __name__ == "__main__":
Quiz(10, 50, 5)

"""