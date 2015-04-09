def encode_morze(text):
	text = text.upper()

	morse_code = {
	"A" : ".-", 
	"B" : "-...", 
	"C" : "-.-.", 
	"D" : "-..", 
	"E" : ".", 
	"F" : "..-.", 
	"G" : "--.", 
	"H" : "....", 
	"I" : "..", 
	"J" : ".---", 
	"K" : "-.-", 
	"L" : ".-..", 
	"M" : "--", 
	"N" : "-.", 
	"O" : "---", 
	"P" : ".--.", 
	"Q" : "--.-", 
	"R" : ".-.", 
	"S" : "...", 
	"T" : "-", 
	"U" : "..-", 
	"V" : "...-", 
	"W" : ".--", 
	"X" : "-..-", 
	"Y" : "-.--", 
	"Z" : "--.."
}

	morse_message = ''
	for letter in text:
		if letter in morse_code:
			if morse_message != '':
				morse_message += "__"
			for char in morse_code[letter]:
				if char == ".":
					morse_message += "^"
				elif char == "-":
					morse_message += "^^^"
				morse_message += "_"
		elif letter == " ":
			morse_message += "____"
	
	return morse_message[:-1]
		

print encode_morze('I love morse')


