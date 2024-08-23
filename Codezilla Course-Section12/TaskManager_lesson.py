
tasks = []

def main():
  message = """Welcome to the Task manager
  1- add tasks to a list
  2- mark task as complete
  3- view tasks
  4- quit"""
  while True:
    print(message)
    choice = input('Enter your choice: ')
    if choice == '1':
      add_tasks()
    elif choice == '2':
      mark_tasks_complete()
    elif choice == '3':
      view_tasks(tasks)
    elif choice == '4':
      break
    else:
      print('Invalid choice please chose number from 1 to 4')
def add_tasks():
  task = input('Enter task: ')
  task_info={'task':task,'completed':False}
  tasks.append(task_info)

  print('Task added successfully to your task manager')

def mark_tasks_complete():
  #get the tasks for the user
  incompelet_tasks = [task for task in tasks if task['completed'] == False]
  #make sure there still incompele tasks
  if not incompelet_tasks:
    print('No task to mark as completed')
    return
  #show tasks for the user
  for i,task in enumerate(incompelet_tasks):
    print(f'{i+1}- {task["task"]}')
    print('------------------')
  #ask the user to choose task
  user_choice = int(input('Enter the number of the task: '))-1
  if user_choice in range(len(incompelet_tasks)):
    #mark the task as completed
    incompelet_tasks[user_choice]['completed']=True
    #print a message to the user 
    print(f'The task ({incompelet_tasks[user_choice]["task"]}) completed')
  else:
      print("invalid choice")

def view_tasks(tasks_list):
  if not tasks_list:
    print('No tasks to view')
    return
  for i,task in enumerate(tasks_list):
    status="✔" if task['completed'] else "❌"

    print(f'{i+1}. {task["task"]} {status}')


if __name__ == "__main__":
  main()


#[{'Task':task,'Completed':False},{'Task':task,'Completed':False}]

