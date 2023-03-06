import os
import sys
check = input("To use this calculator, fill in the correct information in the 'Distance.txt' file. If done, type '+'")

if check == "+":
    txt_file = input("What do you want to  calculate?")

    try:
        with open(txt_file.lower()+ '.txt', 'r') as f:
            lines = f.readlines()
    except IOError:
        print("There is no data for that")
        sys.exit()

    gas_split = str(lines[0]).split(":")
    gastype = gas_split[1]

    gasprice_split = str(lines[1]).split(":")
    gasprice = gasprice_split[1].strip()

    carusage_split = str(lines[2]).split(":")
    carusage = carusage_split[1].strip()

    pricekm = float(carusage) / 100 * float(gasprice)

    distance = int(input("How much km will you drive?"))

    total = distance * pricekm

    checklist = input('''To sum things up:
    Gas  type: {}
    current gas price: {}
    your car usage is {} / 100KM
    If this is correct please type "Yes"
    '''.format(gastype, gasprice, carusage))

    if checklist.lower() == 'yes':
        print("The total price of your journey will be €{}".format(round(total, 2)))
        sys.exit()
    else:
        print("Make sure to check if you input the correct information in the text file.")
        sys.exit()

else:
    print("Make sure to fill in the information before using the calculator.")
    sys.exit()