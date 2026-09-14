from stegano import lsb

def hide_text_in_image(image_path, text, output_path):
	secret = lsb.hide(image_path, text)
	secret.save(output_path)
	print(f"Text hidden successfully in {output_path}.")

def extract_text_from_image(image_path):
	extracted_text = lsb.reveal(image_path)
	print(f"Extracted hidden text: {extracted_text}")


original_image_path = "car.jpg"
stego_image_path = "stego_image.png"
# The text message to hide
text_to_hide = "Python is helpful!"
# Hide text in image
hide_text_in_image(original_image_path, text_to_hide, stego_image_path)
# Extract text from image
extract_text_from_image(stego_image_path)