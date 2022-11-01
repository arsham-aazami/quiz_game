class User:
	def __init__(self, user_id, username):
		self.user_id = user_id
		self.username = username
		self.follower = 0
		self.following = 0

	def follow(self, user):
		user.follower += 1
	    self.following += 1


user_1 = User("232!@#aae", "arsham229")
user_2 = User("khkh213$^%", "jack123")

user_1.follow(user_2)