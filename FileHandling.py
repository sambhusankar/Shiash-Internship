# r+ mode
file = open("D:\\Shiash Internship\\CodingPractices\\sample.txt", "r+")
file.seek(1)
file.write("/")


# w+ mode 
file1 = open("D:\\Shiash Internship\\CodingPractices\\sample.txt", "w+")
file1.seek(5)
file1.write("write testing")
file1.close()

# a+ mode 
file2 = open("D:\\Shiash Internship\\CodingPractices\\sample.txt", "a+")

file2.write("append testing")
file2.close()