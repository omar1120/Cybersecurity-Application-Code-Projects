def encode_message(text, hidden_message):
	# Convert the hidden message to a binary string
	binary_msg = "".join(format(ord(char), '08b') for char in hidden_message)
	encoded_text = []
	msg_index = 0
	for char in text:
		if msg_index < len(binary_msg):
			if binary_msg[msg_index] == '1':
				encoded_text.append(char + ' ') # Add a space for binary 1
			else:
				encoded_text.append(char) # No space for binary 0
				msg_index += 1
		else:
			encoded_text.append(char)

	return ''.join(encoded_text)

def decode_message(encoded_text):
	decoded_message = []
	current_char = ""
	for char in encoded_text:
		if char != " ":
			current_char += char
		else:
			decoded_message.append(current_char)
			current_char = ""
			
	# Add the last character if there's no trailing space
	if current_char:
		decoded_message.append(current_char)

	return ''.join(decoded_message)

#------------------------------------- main starts here -------------------------------------

original_text = "Welcome to Cybersecurity Programming."
secret_message = "Hi"
# Encoding the message
encoded_text = encode_message(original_text, secret_message)
print("Encoded text:", encoded_text)

# Decoding the message
decoded_message = decode_message(encoded_text)
print("Decoded message:", decoded_message)