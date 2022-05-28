HELP = """
help - print program help.
add - add a task to the list (request a task from the user).
show - print all added tasks.
random - Surprise Me!
exit - Exit :)
"""

RANDOM_TASK = "Add me on Twitter @pavlik__on"

tasks = { 

}

run = True

def add_todo(date, task):
    if date in tasks: 
    #Date exist
     tasks[date].append(task)
    else:
    #Add New Date
     tasks[date] = []
     tasks[date].append(task)
    print('Task', task, 'Added on date', date)
  

while run:
  print('For HELP type "help"')
  command = input('Enter command: ')
  if command == 'help':
    print(HELP)
  elif command == 'show':
    date = input('Enter Date: ')
    date = date.capitalize()
    if date in tasks:
      for task in tasks[date]:
        print(task, '-', date)
    else: 
      print('No Date')
    #print(tasks)
  elif command == 'add':
    date = input('Date: ')
    task = input('Enter Task Name: ')
    add_todo(date, task)
  elif command == 'exit':
    run = False
  elif command == 'random':
    add_todo('Today', RANDOM_TASK)
  else:
    print('Unknown Command')
    command

print('Done')