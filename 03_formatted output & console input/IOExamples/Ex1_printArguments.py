# Variables
# J. Sun
# Enhanced output can be produced by the print function
# with optional arguments, sep and end

## Demonstrate use of print argument sep
# Print function uses string consisting of one space character as separator
print("1) Hello", "World!")        # default sep vaule = " "
print("2) Hello", "World!", sep = " ")

# Optionally change the separator to any string we like with the sep argument
print("3) Hello", "World!", sep = "")
print("4) Hello", "World!", sep ="**")
print("5) 1", "two", "3", sep = " ")
print("6) Name: Apple", "Brand: Gala",
"Color: Red", "B-code: 123456", sep ="\t")
print("7) Hello", "Python", "World!", sep ="\n")
print("8) Hello", "\n", "Python", "\n", "World!", sep="")
print()


## Demonstrate use of print argument end
# Print statement ends by executing a newline operation.
print("a) Hello")              # default end vaule = "\n"
print("b) World!")
print("c) Hello", end = "\n")
print("d) World!", end = '\n')

# Optionally change the ending operation with the end argument
print("e) Hello", end = " ")
print("World!")
print("f) Hello", end = "*")
print("World!")
print("g) Hello", end = " Python ")
print("World!")
print("h) Hello", end = "")
print("World!")
print()


## Demonstrate use of escape sequences and expandtabs()
# expandtabs() controls the number of position between horizontal tab stops
print("01234567890123456")  # use numbers as a ruler to show spaces
print("a\tb\tc")            # default \t vaule = 8 spaces
print("a\tb\tc".expandtabs(8))
print("a\tb\tc".expandtabs(5))

print("01234567890123456789")
print("Home,\tSweet\tHome!".expandtabs(5))

print("012345678901234567890")
print("123\t456\n789\tabc".expandtabs(10))
print()
