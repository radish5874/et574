## Demonstrate accessing data in a txt file


#filename = 'pi_million_digits.txt'
filename = '/Users/feifanyang/Library/CloudStorage/OneDrive-CityUniversityofNewYork/2022 fall/et574-python/12_files_and_exceptions/FilesExceptionsExamples/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
     