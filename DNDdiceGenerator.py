## Import API Key ##
filename = 'Resources/config_key.txt'
def get_file_contents(filename):
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)
api_key = get_file_contents(filename)


from rdoclient import RandomOrgClient
def D20Roller(rollType):
    randClient = RandomOrgClient(api_key)

    if (int(rollType) < -1) | (int(rollType) > 1):
        text = 'Sorry, my dice cannot be cast.\n'

    elif int(rollType) == 0:

        preText = 'I rolled and got '

        randNum = randClient.generate_integers(1, 1, 20)
        roll = str(randNum[0])

        text = preText + roll + '.\n'
    
    else:
        preText = 'I rolled with '

        if int(rollType) == -1:
            vantage = 'disadvantage '
            randNum = randClient.generate_integers(2, 1, 20)
            if randNum[0] <= randNum[1]:
                roll = str(randNum[0])
            else:
                roll = str(randNum[1])
        
        elif int(rollType) == 1:
            vantage = 'advantage '
            randNum = randClient.generate_integers(2, 1, 20)
            if randNum[0] >= randNum[1]:
                roll = str(randNum[0])
            else:
                roll = str(randNum[1])
            
        text = preText + vantage + 'and I got ' + roll + '.\n'

    print(text)

D20Roller(input("\n\nType '-1' to roll with disadvantage or '1' for advantage. Otherwise, type '0': "))
