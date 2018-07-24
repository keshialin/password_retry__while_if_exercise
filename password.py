password = 'a123456'
t = 2
while t > -1:
	answer = input('Please enter your password:')
	if answer == password:
		print('Login successfully!')
		break
	else:
		print('The password is wrong. You still have {} chances!'.format(t))
		t = t-1