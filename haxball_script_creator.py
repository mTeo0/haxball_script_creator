HBinit = {
    'roomName': None,
    'public': None,
    'password': None,
    'maxUsers': None,
    'noPlayer': None
}

def addBot():
    if HBinit['noPlayer'] is False:
        HBinit.update({'botName': None})
        

while True:
    print('''
        Bienvenido a Haxball Script Creator!
          
         Porfavor ingrese su nombre. 

        ''')
    userName = input('>>> ')
    break
    

