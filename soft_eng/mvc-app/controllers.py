import json

from .models import Numberslist


def create_num_list(num):
    parse_nums = [int(n) for n in num.split(" ")]
    return Numberslist(parse_nums)


def find_max(nums: Numberslist):
    return max(nums.nums)


def find_min(nums: Numberslist):
    return min(nums.nums)


def save_list_to_json(nums: Numberslist):
    json.dump(nums.nums, open('numbers.json', 'w'))

def save_max_json(nums: Numberslist):
    json.dump(find_max(nums), open('number_max.json', 'w'))

def save_min_json(nums: Numberslist):
    json.dump(find_min(nums), open('number_min.json', 'w'))
