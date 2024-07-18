from models import Numberslist
from controllers import *
from views import *
import os

def run():
    nums = Numberslist()
    while True:
        print_main_menu()
        user_input = user_choice_input()
        if user_input == '1':
            user_input1 = nums_input()
            nums = create_num_list(user_input1)

        elif user_input == '2':
            max_nums = find_max(nums)
            print_max(max_nums)

        elif user_input == '3':
            min_nums = find_min(nums)
            print_min(min_nums)

        elif user_input == '4':
            save_list_to_pickle(nums)

        elif user_input == '5':
            save_max_pickle(nums)

        elif user_input == '6':
            save_min_pickle(nums)

        elif user_input == '0':
            exit_prg()
            break


run()
