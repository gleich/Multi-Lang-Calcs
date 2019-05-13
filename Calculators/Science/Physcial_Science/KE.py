import time
import math


def spacer():
	"""
	Will clear the output screen for a user
	:return: blank lines
	"""
	for i in range(70):
		print("\n")


def ask_question(question, caster):
	"""
	Will ask the user a question and cast it.
	:param question: The question that will be ask by the user
	:param caster: What the user's input will be casted as
	:return: the user's input casted
	"""
	if "int" in caster.lower():
		try:
			spacer()
			users_input = int(input(question))
			return users_input
		except ValueError:
			spacer()
			print("Please make sure that you only enter a integer")
			users_input = int(input(question))
			return users_input
	elif "float" in caster.lower():
		try:
			spacer()
			users_input = float(input(question))
			return users_input
		except ValueError:
			spacer()
			print("Please make sure that you only enter a float")
			users_input = float(input(question))
			return users_input
	elif "list" in caster.lower():
		try:
			spacer()
			users_input = list(input(question))
			return users_input
		except ValueError:
			spacer()
			print("Please make sure that you type something in")
			users_input = list(input(question))
			return users_input
	elif "bool" in caster.lower():
		try:
			spacer()
			users_input = bool(input(question))
			return users_input
		except ValueError:
			spacer()
			print("Please make sure that your input is either True or False")
			users_input = bool(input(question))
			return users_input
	else:
		users_input = input(question)
		return users_input


while True:
	knows_work = ask_question("Do you know the work? If so, type True and if not than type False\n", "boolean")
	knows_speed = ask_question("Do you know the speed/velocity? If so, type True and if not than type False\n", "boolean")
	if knows_work and knows_speed:
		work = ask_question("What is the work?\n", "float")
		speed = ask_question("What is the speed\n", "float")
		answer = 0.5 * work * (speed ** 2)
		print("The kinetic energy is:")
		print(answer + "j")
		print("Here is the work for the problem:")
		print("0.5 * {work_var} ({speed_var}^2)\n".format(work_var=work, speed_var=speed))
		continue_question = ask_question("Would you like to do another calculation?\n")
		if "y" in continue_question.lower():
			spacer()
			continue
		else:
			break
	knows_kinetic_energy = ask_question("Do you know the kinetic energy? If so, type True and if not than type False\n", "boolean")
	elif knows_kinetic_energy and knows_work:
		work = ask_question("What is the work?\n", "float")
		kin_eng = ask_question("What is the kinetic energy?\n", "float")
		answer = sqrt(KE / (0.5 * work))
		print("The velocity is:")
		print(answer)
		print("Here is the work for the problem:")
		print("square root[{kinetic} / (0.5 * {work_var})]".format(kinetic=kin_eng, work_var=work))
		continue_question = ask_question("Would you like to do another calculation?\n")
		if "y" in continue_question.lower():
			spacer()
			continue
		else:
			break
	elif knows_kinetic_energy and knows_speed:
		kin_eng = ask_question("What is the kinetic energy?\n", "float")
		speed = ask_question("What is the speed\n", "float")
		answer = (kin_eng / (speed ** 2)) / 0.5
		print("The work is:")
		print(answer + "j")
		print("Here is the work for the problem:")
		print("({kinetic} / ({speed_var}^2)) / 0.5".format(kinetic=kin_eng, speed_var=speed))
		continue_question = ask_question("Would you like to do another calculation?\n")
		if "y" in continue_question.lower():
			spacer()
			continue
		else:
			break
	else:
		print("There was an error running the program")
		print("Please make sure that you True only twice")
		print("The program will restart in 7 seconds")
		time.sleep(7)
		continue
