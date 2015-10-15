import string
import random
import os

def first_layer(message):
	# the code below instantiates the variables necessary for the first layer to be completed.
	shift = int(raw_input("Enter shift value: ")) # value to shift the alphabet to the right by
	shifted_alphabet = [] # empty list which will be filled with the shifted (crypted) alphabet.


	for i in range(0,26): # loop 26 times
		shifted_alphabet.append(string.ascii_lowercase[(i + shift) % 26])
		# append to shifted_alphabet alphabet[i(num from 0-26) PLUS shift value, modulo by 26 to keep in alphabet range.
		# this creates a whole alphabet list which is 'shifted' to the right to the value of shift.


	crypted_message = "" # Empty string variable will hold the crypted message.
	
	for c in message: # Loop for every character in message
		if c.lower() not in string.ascii_lowercase: # If that character is not in the alphabet(Numbers, punctuation)
			crypted_message += c # Add that character to the crypted message WITHOUT crypting it.
		else:	# Otherwise
			crypted_message += shifted_alphabet[original_alphabet[c.lower()]]
			# add to crypted message the value of original_alphabet[character] called to shifted_alphabet.
			# For example: Character = A, original_alphabet[a] = 0, shifted_alphabet[0] = Z (if shifted by 1)

	return crypted_message # return the cryped message

def second_layer(message):
	key = "" # Empty string that will store the 'key' value
	message_crypt = "" # Empty string that will store the encrypted message

	for c in message: # for every character in message
		if c not in string.ascii_lowercase:
			key += c # add that space into the key
		else: # Otherwise
			key += string.ascii_lowercase[random.randint(0,25)] # Add a random letter from the alphabet to the key string.

	for i in range(0, len(message)): # For numbers in the range of 0, to the length of the message
		if message[i] not in string.ascii_lowercase:
			message_crypt += message[i]
		else: # Otherwise
			# get values of message[i] and key[i] (this could be message[1] and key[1] This returns a letter. Call original_alphabet for letter
			# values, then add them both together, modulo by 25 to return a number within 25, and call string.ascii_lowercase[end result].
			message_crypt += string.ascii_lowercase[(original_alphabet[message[i]] + original_alphabet[key[i]]) % 26] 



			
	full = first_layer(key) + message_crypt # Encrypt the key after it has been used to crypt the message. Add it to the message.

	return full # Return the full variable, which holds a caesar shifted key as well as the encrypted message.

def main():
	filename = raw_input("Enter the file to write to: ")
	f = open(filename, "w")
	message_list = raw_input("Enter a message: ") # get user input, then put each character into a list.
	f.write(second_layer(first_layer(message_list)))
	f.close()





original_alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13,
"o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25} # alphabet dictionary

main()






