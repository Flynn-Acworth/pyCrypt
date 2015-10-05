# Author is Flynn Acworth
import string

def caesar_decrypt(message, shift):
	unshift = ""

	for c in message:
		if c not in string.ascii_lowercase:
			unshift += c
		else:
			unshift += string.ascii_lowercase[original_alphabet[c] - shift]
	return unshift

def split_message(message):
	key = message[0:len(message) / 2]
	message = message[len(message) / 2: len(message)]
	return key, message

def otp_decrypt(key, message):
	full = ""
	for i in range(0, len(key)):
		if key[i] not in string.ascii_lowercase:
			full += key[i]
		else:
			if ((original_alphabet[message[i]] - original_alphabet[key[i]]) % 26) < 0:
				full += string.ascii_lowercase[((original_alphabet[message[i]] - original_alphabet[key[i]]) % 26) + 26]
			else:
				full += string.ascii_lowercase[(original_alphabet[message[i]] - original_alphabet[key[i]]) % 26]

	return full

def main():
	choice = raw_input("Do you want to read message from file? y/n ")
	if choice == "y":
		filename = raw_input("Enter the file to read from: ")
		f = open(filename, "r")
		message = f.read()
		f.close()
	else:
		message = raw_input("Enter the message: ")
	
	shift1 = int(raw_input("Enter the first shift value: "))
	shift2 = int(raw_input("Enter the second shift value: "))
	key, message = split_message(message)
	real_key = caesar_decrypt(key, shift2)
	message = otp_decrypt(real_key, message)
	print caesar_decrypt(message, shift1)

original_alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
	"o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} # alphabet dictionary

main()
