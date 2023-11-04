def madlibs():
	adjective_one = input("Adjective: ")
	body_part = input("Body part: ")

	madlibs = f"I love computer programming because it's {adjective_one}!\
		The journey to becoming a good programmer starts with hope in your mind and\
			a dream in your {body_part}."

	print(madlibs)

if __name__ == "__main__":
	print("Welcome to Programming Excitements Program Mad Libs\n")
	madlibs()