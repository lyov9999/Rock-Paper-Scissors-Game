from random import randint
l = {1:'rock', 2:'paper', 3:'scissors'}
finish = None
while not (type(finish) == int):
    try:
        finish=int(input('Input finish score bigger than 0 '))
        if finish < 1:
            print('%s < 1' %finish)
            finish = None
    except:
        print('Input integer !')

you = comp = 0
while not (you == finish or comp == finish):
	comp_choose =  randint(1, 3)
	for k,v in l.items():
		print('  ', k,':',v  , sep=' ', end='', flush=True)
	your_choose =  None
	while not (type(your_choose) == int):
	    try:
	        your_choose=int(input('\n Input value '))
	        if not (1 <= your_choose <= 3):
	            print('Input valid value !')
	            your_choose = None
	    except:
	        print('Input integer !')
	if comp_choose == 1:
		if your_choose == 2:
			you += 1
			print('\n{0} beats {1}\n'.format(l[your_choose], l[comp_choose]))
		elif your_choose == 3:
			comp +=1
			print('\n{0} beats {1}\n'.format(l[comp_choose], l[your_choose]))
		else:
			print('\nYour choose and Comp choose is %s\n' %l[your_choose])
	elif comp_choose == 2:
		if your_choose == 3:
			you += 1
			print('\n{0} beats {1}\n'.format(l[your_choose], l[comp_choose]))
		elif your_choose == 1:
			comp +=1
			print('\n{0} beats {1}\n'.format(l[comp_choose], l[your_choose]))
		else:
			print('\nYour choose and Comp choose is %s\n' %l[your_choose])
	else:
		if your_choose == 1:
			you += 1
			print('\n{0} beats {1}\n'.format(l[your_choose], l[comp_choose]))
		elif your_choose == 2:
			comp +=1
			print('\n{0} beats {1}\n'.format(l[comp_choose], l[your_choose]))
		else:
			print('\nYour choose and Comp choose is %s\n' %l[your_choose])
	print('You: {0} || Comp: {1} \n'.format(you,comp))

if you > comp:
	print('You won, your rating: %s' %you)
else:
	print('You lost, your rating: %s' %you)