# Made by Le Quoc Hien with F-Soft account of HienLQ
nums = []
tmp_nums = []
input_number = 0
tmp_input_number = None
target = 0
max_size = 0
tmp_max_size = input('Enter maximum size of integer array: ')
try:
    max_size = int(tmp_max_size)
except Exception:
    print('The maximum size of integer array is NOT an integer!')
    exit()
if max_size < 2:
    print('Can\'t perform sum if maximum size of integer is smaller than 2!')
    exit()
while len(nums) < max_size:
    print('Remember: input array can\'t have duplicated items!')
    tmp_input_number = input('Enter an integer to add to a temporary array: ')
    try:
        input_number = int(tmp_input_number)
    except Exception:
        print('Input is NOT an integer! Please try again!')
        continue
    tmp_nums.append(input_number)
    nums = list(dict.fromkeys(tmp_nums))
tmp_target = input('Enter target number: ')
try:
    target = int(tmp_target)
except Exception:
    print('The target number is NOT an integer!')
    exit()
for i in range(max_size - 1):
    for j in range(i + 1, max_size):
        if nums[i] + nums[j] == target:
            break
    if nums[i] + nums[j] == target:
        break
if nums[i] + nums[j] != target:
    print('Error: output of indices of 2 numbers such that they add to target is NOT found!')
else:
    output = [i, j]
    print(output)