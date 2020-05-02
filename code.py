from random import randint
l = {1:'rock', 2:'paper', 3:'scissors'}
finish = None
while not (type(finish) == int):
    try:
        finish=int(input('Input finish score from the big 0 '))
        if finish < 1:
            print('%s < 1' %finish)
            finish = None
    except:
        finish = 5

def choose():
    your_choose =  None
    while not (type(your_choose) == int):
        try:
            your_choose=int(input('\n Input value '))
            if not (1 <= your_choose <= 3):
                print('Input valid value !')
                your_choose = None
        except:
            print('Input integer !')
    return your_choose

def compare(you, comp):
    if comp == 1:
        if you == 2:
            return 1
        elif you == 3:
            return 2
        else:
            return 3
    elif comp == 2:
        if you == 3:
            return 1
        elif you == 1:
            return 2
        else:
            return 3
    else:
        if you == 3:
            return 1
        elif you == 2:
            return 2
        else:
            return 3

you = comp = 0
while not (you == finish or comp == finish):
	comp_choose =  randint(1, 3)
	for k,v in l.items():
		print('  ', k,':',v  , sep=' ', end='', flush=True)

	your_choose = choose()

	your_compare = compare(your_choose, comp_choose)
	if your_compare == 1:
		you += 1
		print('\n{0} beats {1}\n'.format(l[your_choose], l[comp_choose]))
	elif your_compare == 2:
		comp +=1
		print('\n{0} beats {1}\n'.format(l[comp_choose], l[your_choose]))
	else:
		print('\nYour choose and Comp choose is %s\n' %l[your_choose])


	print('You: {0} || Comp: {1} \n'.format(you,comp))

if you > comp:
	print('You won, your rating: %s' %you)
else:
	print('You lost, your rating: %s' %you)
    