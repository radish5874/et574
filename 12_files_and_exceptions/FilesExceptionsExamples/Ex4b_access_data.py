## Demonstrate accessing data in a csv file

def main():
    ## Display the countries in a specifed continent.
    continent = input("Enter the name of a continent: ")
    continent = continent.title()   # Allow for all lowercase letters.
    if continent != "Antarctica":
        infile = open("UN.txt", 'r')
        for line in infile:
            #split(): Splits the string at the specified separator,
            #and returns a list
            data = line.split(',')

            if data[1] == continent:
                print(data[0])
    else:
        print("There are no countries in Antarctica.")

main()
