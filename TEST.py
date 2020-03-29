calc = "base"
if calc == "base":
    base = int(input('''What base would you like to use?
Available: 2 (binary) 8 (octo) 10 (decimal (normal)) 16 (hex)
Type 2, 8, 10, or 16: '''))
    if base == 2:
        result = bin(input("Type the original number: ")
        printThis = "=" +str(result)
        print(printThis)