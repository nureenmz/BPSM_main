##---NOTES---##
#   LISTS   [list here]
#   list.append, list.insert(index,item), list.extend(list2), list.index(item), list.remove(item)
#   list.sort(), list.reverse(), list.pop(index) - remove an item
    # emptylist = [], emptylist[0] - first item in the list, emptylist[1:] - 2nd item to last
    # emptylist[-1] - last position

### set(emptylist) - get all unique values in the list
# sorted(list(set(emptylist)))
# emptylist.count(item) - count how many instances
# emptylist.index(item) - return the first index position of item
# emptylist + ['item1','item2'] - adds items to end of list
    # 

# string.split() - based on delimiters (defaults: space, tab, newline), output is list
# string.split('t') - split wherever there is a 't'
# string.join()    
# ' '.join(something) - joins items in something, using space

# range
# list(range(10))
# list(range(3,24,4))

# string.ascii_lowercase
# string.ascii_lowercase.startswith('evaluatesomething')
# string.ascii_lowercase[index]
# string.ascii_lowercase[index].endswith('evaluation')

## convert str to list
#   list(string.ascii_lowercase.upper())
#   list(string.ascii_lowercase)[index]

## non-sequential index ie. tuple
#   nonsequential= val1,val2,val3,val4
#   (val1,val2,val3,val4)
#   nonsequential[index]
## cannot change/append tuple contents

# list.sort() - changes original list
# list.reverse() - reverses a list // reversing creates 'Nonetype' - cannot use 'set' on it

# s='-' ## can modify 's'
# s.join(list)
#       'green-red-blue'

# Nonetype - cannot sort, reverse, set, join
# s.join(str(list)[index].replace(',', "))

# mixed list
# newlist= oldlist + addedlist
# list(s.join(str(e) for e in numbs))

# boolean: somecolors1[0] in somecolors1_and_numbs

# LOOPS
for item in list:
   print(item)
   
for item in list:
    "%s" % (item)

for item in list:
    "{0}".format(item)

for item in list:
    f"{item}"
    
for  item in list:
    f"The next color is {item}"

count=0
for item in list: # variables can be positional
    count+=1
    "Color {1} is {0}".format(count, item)

count=0
for item in list:
    count+=1
    f"Color {count} is {item}"
    
for item in list: # the value of variable 'item' is set to each list element in the for loop
    print(item)
    if item == 'string':
        f'My favorite color is {item}'
    if item == 3:
        f'My favorite number is {item}'
    f'This line is not in either if block'
f'This line is not in the for loop'

for item in list: # loop through the list
    print('This time, the item variable is ' + item)
    f'formated way: the item variable is {item}'

for item in list: # loop and action
    myfile= open(item + '.txt', 'w')
    myfile.write(str(len(item)) + '\n')
    myfile.close()
    f'{item[index].upper()}'
    
for item in list: # to read a file, open connection
    f'Color list item {item} was {open(item + ".txt").read()} characters long.'

for item in list: # check written files, stripping the newline
    for item in list:
    f'Color list item {item{ was {open(item + ".txt").read().rstrip()} characters long.'

my_file= open(file)
for eachline in my_file:
    line_length= len(eachline.rstrip('\n'))
    f'{line_length}'

os.path.exists(somefile) # check if file exists
