from data import question_data as data


class Question:
	def __init__(self, text, answer):
		self.text = text
		self.answer = answer
		self.score = 0
		self.input = input(f"{text}(True/False): ")


	def checking_answer(self):
		if self.answer == self.input:
			print("great! one score")
			self.score += 1
		else:
			print("wrong answer")


q1 = Question(data[1]["text"], data[1]["answer"])

q1.checking_answer()