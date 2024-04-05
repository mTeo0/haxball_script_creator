# * Haxball Script Creator
# author: _mteoo
# Build date: 3/4/2024
# github: https://github.com/mTeo0/haxball_script_creator/blob/main/haxball_script_creator.py

import datetime
import json
from maps import real_soccer, futsal

HBinit = {
    'roomName': None,
    'public': None,
    'password': None,
    'maxPlayers': None,
    'noPlayer': True
}

modality = None

def addBot(x):
    if HBinit['noPlayer'] is False:
        HBinit.update({'playerName': x})

if __name__ == '__main__':
    while True:
        print('''
            github: https://github.com/mTeo0/haxball_script_creator/blob/main/haxball_script_creator.py

            Welcome to Haxball Script Creator! by _mteoo
              
             Please type your name. 
    
            ''')
        userName = str(input('>>> '))
        print(f'Ok {userName}, what modality will have your script?')
        print('''
    
                1 - Real Soccer
    
                2 - Futsal
              
                3 - Custom
                ''')
        modalityOption = int(input('>>> '))
        match modalityOption:
            case 1:
                modality = 'Real Soccer'
                print('You choosed the first option (Real Soccer)')
            case 2:
                modality = 'Futsal'
                print('You choosed the second option (Futsal)')
            case 3:
                modality = 'Custom'
                print('You choose the third option (Custom)')
            case _:
                print('ERROR: Invalid option')
                quit()
        print('Now please put the name of the room')
        nameOption = str(input('>>> '))
        HBinit.update({'roomName': nameOption})
        print('The room should have password?')
        passwordOption = str(input('[Y/n]: ')).lower()
        if passwordOption == 'n':
            HBinit.update({'password': False})
            pass
        elif passwordOption == 'y':
            print('Ok, now please type the password')
            passwordOption2 = input('>>> ')
            HBinit.update({'password': passwordOption2})
            pass
        else:
            print('ERROR: Invalid Option')
            quit()
        print('The room should be public?')
        publicOption = str(input('[Y/n]: ')).lower()
        if publicOption == 'n':
            HBinit.update({'public': False})
            pass
        elif publicOption == 'y':
            HBinit.update({'public': True})
            pass
        else:
            print('ERROR: Invalid Option')
            quit()
        print('Now please type the capacity of players of the room')
        capacity = int(input('>>> '))
        if not isinstance(capacity, int) or capacity < 0:
            print("ERROR: Invalid input for player capacity")
            quit()
        else:
            HBinit.update({'maxPlayers': capacity})
        print('Should the room have a bot? (A player inside the room that doesnt do anything, if you dont order it)')
        botOption = str(input('[Y/n]: ')).lower()
        if botOption == 'y':
            HBinit.update({'noPlayer': False})
            print('Ok, then how should the bot call?')
            botName1 = str(input('>>> '))
            addBot(botName1)
            pass
        elif botOption == 'n':
            pass
        else:
            print('ERROR: Invalid option')
            quit()

        print(HBinit)
        break
    hbinit_json = json.dumps(HBinit)
    now = datetime.date.today()

script = '''
// ==============================[{}'s Script]==============================
// author: {}
// date: {}
// modality: {}
// {} * haxball_script_creator
// hcs github: https://github.com/mTeo0/haxball_script_creator/blob/main/haxball_script_creator.py

const room = HBInit({})

'''.format(HBinit['roomName'], userName, now, modality, HBinit['roomName'], hbinit_json)

with open('script.txt', 'w', encoding="utf-8") as f:
    match modality:
        case 'Real Soccer':
            f.write(script)
            f.write('\n')
            f.write(real_soccer.script_rs)
        case 'Futsal':
            f.write(script)
            f.write('\n')
            f.write(futsal.script_futsal)
        case 'Custom':
            f.write(script)
print('A file named: "script.txt" was created or modified.')
