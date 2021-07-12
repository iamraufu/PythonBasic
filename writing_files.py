# Opening an existing text file named person and appending to it
employee_file = open("person.txt", "a")

employee_file.write("\nRahman - Software Engineer")

# Creating a new text file named person2 and writing on it. Whenever I write previous data got delete and write newly
employee_file = open("person2.txt", "w")

employee_file.write("This is a new Person File")

# Creating a web page and writing in it
webpage_file = open("index.html", "w")
webpage_file.write("<h1>This webpage is created using Python</h1>")

employee_file.close()