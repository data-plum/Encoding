def encode_bacon(string):
	string = string.replace(' ', '')

	bacon_code = { 
	'aaaaa' : 'a',
	'aaaab' : 'b',
	'aaabb' : 'c',
	'aabbb' : 'd',
	'abbbb' : 'e',
	'bbbbb' : 'f',
	'bbbba' : 'g',
	'bbbab' : 'h',
	'bbabb' : 'i',
	'babbb' : 'j',
	'abbba' : 'k',
	'bbbaa' : 'l',
	'bbaab' : 'm',
	'baabb' : 'n',
	'aabba' : 'o',
	'abbab' : 'p',
	'bbaba' : 'q',
	'babab' : 'r',
	'ababb' : 's',
	'babba' : 't',
	'abbaa' : 'u',
	'bbaaa' : 'v',
	'baaab' : 'w',
	'aaaba' : 'x',
	'aabab' : 'y',
	'ababa' : 'z'
	}

	new_string = []
	encode_list = []
	helpful_sell_1 = ''
	helpful_sell_2 = ''
	decoded_word = ''

	for item in string:
		helpful_sell_1 += item
		if len(helpful_sell_1) == 5:
			new_string.append(helpful_sell_1)
			helpful_sell_1 = ''

	for word in new_string:
		for letter in word:
			if letter.islower():
				bacon_encode_letter = "a"
			elif letter.isupper():
				bacon_encode_letter = "b"
			helpful_sell_2 += bacon_encode_letter
			if len(helpful_sell_2) == 5:
				encode_list.append(helpful_sell_2)
				helpful_sell_2 = ''

	for encode_word in encode_list:
		if encode_word in bacon_code:
			decoded_word += bacon_code[encode_word]
	return decoded_word


print encode_bacon('Hot sUn BEATIng dOWN bURNINg mY FEet JuSt WalKIng arOUnD HOt suN mAkiNG me SWeat')