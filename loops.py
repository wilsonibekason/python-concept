command = ''
started = True
  #while command.lower() != 'quit':
while True:
     command = input('> ').lower()
     if command == 'start':
         started = True
         print('Car started ')
     elif command == 'stop':
         if not started:
             print('car is already stopped')
         else:
             started = False
             print('car stopped ')
     elif command == 'help':
         print('''
start - to start the car 
stop - to stop the car
quit - to exit
        ''')
     elif command == 'quit':
         break;
     else:
         print('sorry i dont understand that ')

guess_count = 1
while guess_count <= 5:
    print('o--||--||' * guess_count)
    guess_count = guess_count + 1
print('Done')

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("GUess "))
    guess_count += 1
    if guess == secret_number:
        print('you won')
        break
else:
    print('sorry you failed ')

