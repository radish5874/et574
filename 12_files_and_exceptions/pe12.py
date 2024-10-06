
def usingloop():
    filename = '/Users/feifanyang/Library/CloudStorage/OneDrive-CityUniversityofNewYork/2022 fall/et574-python/12_files_and_exceptions/pe12.txt'
    with open(filename) as file_object:

        for name in file_object.read():
            print(name.rstrip())



'''
def using_list():
    filename = '/Users/feifanyang/Library/CloudStorage/OneDrive-CityUniversityofNewYork/2022 fall/et574-python/12_files_and_exceptions/pe12.txt'
    with open(filename,'r') as file_object:
        list1=file_object.read()
        print(list1)
'''

def main():
    usingloop()
    #using_list()

main()