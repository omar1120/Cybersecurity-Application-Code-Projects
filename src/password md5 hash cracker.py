#password md5 hash cracker
import hashlib
target = "7519e1b72f63f662b667f72bedcb88b8" #hash of password in dictionary
found = False
while found == False:
	with open("dictionary.txt","r") as file:
		for line in file.readlines():
			cleaned_line = line.strip()
			hash_target = hashlib.md5(cleaned_line.encode()).hexdigest()
			if hash_target == target:
				found = True
				print("password is:",cleaned_line)
				break
if not found:
	print("password is not found in dictionary or invalid hash")