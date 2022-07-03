def main():
	# write your code here
	time = input("Enter a number from 1 to 12")
	item = input("Enter a noun (plural)")
	name = input("Enter a name")

	scream = input("Enter any sentence")

	action = input("Enter a verb")

	print(f" It was {time} when I heard a knock at the door")
	print(f"I opened the door and there was a box full of {item} with a note saying From Mr. {name.capitalize()}.")
	print(f"Just as I closed the door I heard a scream{scream.upper()}")
	print(f"I froze in place and all I could do was{action}")



if __name__ == '__main__':
	main()