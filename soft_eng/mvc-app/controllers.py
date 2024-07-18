import pickle

from models import Numberslist


def create_num_list(num):
    parse_nums = [int(n) for n in num.split()]
    return Numberslist(parse_nums)


def find_max(nums: Numberslist):
    return max(nums.nums)


def find_min(nums: Numberslist):
    return min(nums.nums)


def save_list_to_pickle(nums: Numberslist):
    f = open("numbers.pkl","wb")
    pickle.dump(nums, f)
    f.close()
def save_max_pickle(nums: Numberslist):
    f = open("numbers_max.pkl","wb")
    pickle.dump((find_max(nums)),f)
    f.close()
def save_min_pickle(nums: Numberslist):
    f = open("numbers_min.pkl","wb")
    pickle.dump(find_min(nums), f)
    f.close()