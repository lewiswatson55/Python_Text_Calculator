def percentage(percent, whole):
    return (percent * whole) / 100.0
def whatIsPercent():
    origin = int(input("what is the ORIGINAL NUMBER? "))
    percent = int(input("What is the PERCENTAGE? "))
    percentage(percent, origin)
def getPercentage(part, whole):
    return 100 * float(part)/float(whole)
def getPercentageRN():
    origin = int(input("What is the number that would be 100%? "))
    part = int(input("What is the number that you want to convert to percentage (e.g. this number out of the number that would be 100%)? "))