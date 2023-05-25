"""
Допоміжний файл.
"""
from task_3_files.hotkeys import hotkeys
from task_3_files.say_thanks import say_thanks

CHANNELS = ["BBC", "Discovery", "Animal Planet", "CNN", "TV1000"]
def tv_controller_program(tv_controller: type):
    """TV controller test program"""
    try:
        controller = tv_controller(CHANNELS)
        command = 'c'
        print('Welcome to the TVController!')
        hotkeys()
        while command:
            choice = input('Your choice: ')  # вибір функції
            match choice:
                case 'f':
                    controller.first_channel()
                case 'l':
                    controller.last_channel()
                case 'N':
                    number = input('Select the channel number: ')
                    if number.isdigit():
                        controller.turn_channel(int(number))
                    else:
                        print('Incorrect input.')
                case 'n':
                    controller.next_channel()
                case 'p':
                    controller.previous_channel()
                case 'c':
                    controller.current_channel()
                case 'e':
                    request = input('Input your request: ')
                    if request.isdigit():
                        request = int(request)
                    controller.is_exist(request)
                case '':
                    say_thanks()
                    break
                case _:
                    print(f'Invalid selection. The <{choice}> function is currently unavailable.')
    except Exception as error:
        print(f'\n!Помічена помилка: {error.__class__}. Причина: {error}.')
