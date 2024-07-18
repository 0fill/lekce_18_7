from .models import Numberslist

def create_num_list(num):
    parse_nums = [int(n) for n in num.split(" ")]
    return Numberslist(parse_nums)

def find_max(nums: Numberslist):
    return max(nums.nums)

def find_min(nums: Numberslist):
    return min(nums.nums)