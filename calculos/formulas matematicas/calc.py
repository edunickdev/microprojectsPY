amountGreenKeys = int(input('type here amount of green keys that you have: '))
amountBlueKeys = int(input('Type here amount of blue keys that you have: '))


def calcAmount(blue, green):
    action = int(input('Please choose which is your mode: \n'
                       '1. Bound gear (this item cant be traded) \n'
                       '2. No bound gear (this items can be trade between different toons) \n'))
    cantGreenKeys = green
    cantBlueKeys = blue
    
    match action:
        case 1:
            greenKeys = int(cantGreenKeys / 10)
            blueKeys = int(cantBlueKeys / 10)
            if greenKeys > blueKeys:
                dullProfanedWood = blueKeys
            else:
                dullProfanedWood = greenKeys
            print(f"Your total amount of Dull Profaned Wood that you can craft is {dullProfanedWood}")

            exit()
        case 2:
            price = int(input('Type here the price that they are paying you for each Dull profaned wood: '))
            greenKeys = int(cantGreenKeys / 40)
            blueKeys = int(cantBlueKeys / 40)
            if greenKeys > blueKeys:
                dullProfanedWood = blueKeys
            else:
                dullProfanedWood = greenKeys
            print(f"Your total amount of Dull Profaned Wood that you can craft is {dullProfanedWood}")
            coin = float(round(dullProfanedWood * price, 2))
            print(f"Your proyected coin is: {coin}")

            exit()
        case 0:
            print("Type 0 if you want leave of the menu")

            exit()


calcAmount(amountBlueKeys, amountGreenKeys)
