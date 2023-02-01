s = None
position = 0
character = None
mutated_string = None
s = input('s = ')
if s == None or len(s) < 1:
    print('Error: s is null!')
    exit()
tmp_position = input('position = ')
try:
    position = int(tmp_position)
except Exception:
    print('Error: non-integer input found!')
    exit()
if position < 0 or position > (len(s) - 1):
    print('Error: index is out of bound!')
    exit()
character = input('character = ')
if len(character) != 1:
    print('Error: character input isn\'t character!')
    exit()
mutated_string = s[:position] + character + s[(position + 1):]
print(mutated_string)