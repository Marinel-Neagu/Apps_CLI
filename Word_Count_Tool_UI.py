count = 0
document = 'Document.txt'

with open(document) as file:
	file1 = file.read()
	file1 = file1.strip()
	for i in file1.split():
		count += 1
		print(count)
