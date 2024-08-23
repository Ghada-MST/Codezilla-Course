# importing datetime module
import datetime

tasks = []


def main():
  message = """\nWelcome to Task manager program
1. Add task to a list
2. Mark task as complete
3. View tasks
4. Modify tasks
5. Delete tasks from list
6. Mark all tasks as completed
7. Quit"""
  while True:
    print(message)
    choice = input('\nEnter your choice: ')

    if choice == '1':
      add_task_to_list()

    elif choice == '2':
      mark_task_complete()

    elif choice == '3':
      view_tasks()

    elif choice == '4':
      modify_task()

    elif choice == '5':
      delete_task()

    elif choice == '6':
      all_task_completed()

    elif choice == '7':
      if quit() == True:
        break

    else:
      print('\nInvalid choice, please choose number from previous list')


def add_task_to_list():
  task = input('\nEnter task: ')

  # input date
  date_string = input('\nEnter task date (yyyy-mm-dd): ')
  # giving the date format
  date_format = '%Y-%m-%d'
  #get the date today
  # datetime object containing current date and time
  now = datetime.datetime.now()
  # dd/mm/YY
  date_string_now = now.strftime(date_format)

  # using try-except blocks for handling the exceptions
  try:

    # formatting the date using strptime() function
    dateObject = datetime.datetime.strptime(date_string,
                                            date_format).strftime(date_format)

    #difference between current date and users date
    if date_string_now > dateObject:
      print("Date missed, can't add the task")
      return
    tasks.append({'task': task, 'date': dateObject, 'complete': False})
    print(tasks)
  # If the date validation goes wrong
  except ValueError:

    # printing the appropriate text if ValueError occurs
    print("\nIncorrect date format, should be YYYY-MM-DD")


def mark_task_complete():

  try:
    incomplete_tasks = [task for task in tasks if task['complete'] == False]
    if len(incomplete_tasks) == 0:
      print('\nNo tasks to mark as complete')
      return
    for i, task in enumerate(incomplete_tasks, 1):
      print(f'{i}. {task["task"]} ({task["date"]})')

    task_number = int(input("\nchoose the task number to add as completed: "))
    #if user enter float or string(value error)
    #if user enter numbers more than tasks number (index error)
    #if user enter negative numbers (index error)
    if task_number > len(incomplete_tasks) or task_number < 1:
      print('\nInvalid Task number')
      return
    incomplete_tasks[task_number - 1]["complete"] = True
    print('\nTask marked completed')
  except:
    print('\nInvalid option, Enter whole numbers')
  #except IndexError:
  #print(f'Invalid option, Enter numbers between 1 to {len(incomplete_tasks)}')


def view_tasks():
  if len(tasks) == 0:
    print('\nNo tasks to view')
  for i, task in enumerate(tasks, 1):
    status = '❌' if task['complete'] == False else "✔"
    print(f'\n{i}. {task["task"]} ({task["date"]}) {status}')


def modify_task():
  if not tasks:
    print('\nNo tasks to modify')
    return
  for i, task in enumerate(tasks, 1):
    status = '❌' if task['complete'] == False else "✔"
    print(f'\n{i}. {task["task"]} ({task["date"]}) {status}')
  try:
    task_number = int(input("\nchoose the task number to modify: "))
    if task_number > len(tasks) or task_number < 0:
      print(f'Please enter numbers from 1 to {len(tasks)}')
      return
    check = input('Are you sure you want to modify this task (y/n): ').lower()
    if check == "y":
      modified_task = input('Enter your modification: ')
      tasks[task_number - 1]['task'] = modified_task
      print('The task modified successfully')
    elif check == "n":
      return
    else:
      print('Invalid choice')
      return
  except:
    print('\nInvalid choice, Enter whole numbers')


def delete_task():
  if len(tasks) == 0:
    print('\nNo tasks to delete')
    return
  for i, task in enumerate(tasks, 1):
    status = '❌' if task['complete'] == False else "✔"
    print(f'\n{i}. {task["task"]} ({task["date"]}) {status}')
  try:
    task_number = int(input("\nchoose the task number to delete: "))
    if task_number > len(tasks) or task_number < 0:
      raise IndexError()
    check = input('Are you sure you want to delete this task (y/n): ').lower()
    if check == "y":
      del tasks[task_number - 1]
      print('The task deleted successfully')

    elif check == "n":
      return
    else:
      print('Invalid choice')

  except IndexError:
    print(f'Please enter numbers from 1 to {len(tasks)}')
  except ValueError:
    print('Invalid choice, Enter whole numbers')


def all_task_completed():
  if len(tasks) == 0:
    print('\nNo tasks to mark as complete')
    return
  check = input(
    'Are you sure you want to mark all tasks as completed (y/n): ').lower()
  incomplete_tasks = [task for task in tasks if task['complete'] == False]
  if check == 'y':
    for task in incomplete_tasks:
      task['complete'] = True
    print("All tasks completed, You did a great job 💪🏻")

  elif check == 'n':
    return
  else:
    print('Invalid option')


def quit():
  check = input('Are you sure you want to quit the program (y/n): ').lower()
  incomplete_tasks = [task for task in tasks if task['complete'] == False]

  if check == 'y':
    if not tasks:
      print('\nBye Bye')

    elif not incomplete_tasks:
      print("You did a great job, see you next time 💪🏻")
    else:
      print("You didn't finish all your tasks yet😞 good luck next time")
    return True
  elif check == 'n':
    return
  else:
    print('Invalid option')


if __name__ == "__main__":
  main()
