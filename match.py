# day = int(input("Enter a day number between 1 to 7 : "))

# match day:
#     case 1:
#         print("MON")
#     case 2:
#         print("TUE")
#     case 3:
#         print("WED")
#     case 4:
#         print("THU")
#     case 5:
#         print("FRI")
#     case 6:
#         print("SAT")
#     case 7:
#         print("SUN")
#     case _:
#         print("Invalid Day Number")

"""
ch = input("Enter a character : ")

match ch:
    # case "A":
    #     print("Vowel")
    # case "a":
    #     print("Vowel")
    # case "E":
    #     print("Vowel")
    # case "e":
    #     print("Vowel")
    # case "I":
    #     print("Vowel")
    # case "i":
    #     print("Vowel")
    # case "O":
    #     print("Vowel")
    # case "o":
    #     print("Vowel")
    # case "U":
    #     print("Vowel")
    # case "u":
    #     print("Vowel")

    case "A" | "a" | "E" | "e" | "I" | "i" | "O" | "o" | "U" | "u":
        print("Vowel")
    case _:
        print("Now Vowel")

"""

print("1 -> Gujarati")
print("2 -> Punjabi")
print("3 -> South Indian")
print("4 -> Chinese")
print("5 -> Italian")

ch = int(input("Enter Your Choice : "))

match ch:
    case 1:
        print("You Selected Gujarati")
        print("1 -> Thepla")
        print("2 -> Fafda")
        ch2 = int(input("Enter Your Choice : "))
        match ch2:
            case 1:
                print("You Selected Thepla")
            case 2:
                print("You Selected Fafda")
    case 2:
        print("You Selected Punjabi")
    case 3:
        print("You Selected South Indian")
    case 4:
        print("You Selected Chinese")
    case 5:
        print("You Selected Italian")
