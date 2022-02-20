name = input("What is your name?: ")
print("Good day %s!" % name)

month = input("In what month were you born?: ")


def zodiac_sign(month):
    if month == "September":
        print("You are a Libra")
    elif month == "October":
        print("You are a scorpio")
    elif month == "November":
        print("You are a Sagitarious")
    elif month == "December":
        print("You are a Capricorn")
    elif month == "January":
        print("You are a Aquarious")
    elif month == "February":
        print("You are a Pisces")
    elif month == "March":
        print("You are a Aries")
    elif month == "April":
        print("You are a Taurus")
    elif month == "May":
        print("You are a Gemini")
    elif month == "June":
        print("You are a Cancer!")
    elif month == "July":
        print("You are a Virgo")
    elif month == "August":
        print("Leo")
    else:
        print("This is not a month")


zodiac_sign(month)
