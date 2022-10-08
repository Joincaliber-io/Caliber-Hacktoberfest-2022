
# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

# Encrypt

# create a PdfFileWriter object
out = PdfFileWriter()

# Open our PDF file with the PdfFileReader
file = PdfFileReader("CV.pdf")

# Get number of pages in original file
num = file.numPages

# Iterate through every page of the original
# file and add it to our new file.
for idx in range(num):
	
	# Get the page at index idx
	page = file.getPage(idx)
	
	# Add it to the output file
	out.addPage(page)


# Create a variable password and store
# our password in it.
password = "12345"

# Encrypt the new file with the entered password
out.encrypt(password)

# Open a new file "myfile_encrypted.pdf"
with open("CV.pdf", "wb") as f:
	
	# Write our encrypted PDF to this file
	out.write(f)


# -------------------------------------------------------------------------------------

# Decrypt
"""
# import PdfFileWriter and PdfFileReader
# class from PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader

# Create a PdfFileWriter object
out = PdfFileWriter()

# Open encrypted PDF file with the PdfFileReader
file = PdfFileReader("CV.pdf")

# Store correct password in a variable password.
password = "12345"

# Check if the opened file is actually Encrypted
if file.isEncrypted:

	# If encrypted, decrypt it with the password
	file.decrypt(password)

	# Now, the file has been unlocked.
	# Iterate through every page of the file
	# and add it to our new file.
	for idx in range(file.numPages):
		
		# Get the page at index idx
		page = file.getPage(idx)
		
		# Add it to the output file
		out.addPage(page)
	
	# Open a new file "myfile_decrypted.pdf"
	with open("CV.pdf", "wb") as f:
		
		# Write our decrypted PDF to this file
		out.write(f)

	# Print success message when Done
	print("File decrypted Successfully.")
else:
	
	# If file is not encrypted, print the
	# message
	print("File already decrypted.")
"""