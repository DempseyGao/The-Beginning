x = 3
x = int(x)
while True:
	p = input('請輸入您的密碼: ')
	if p == 'a123456':
		print('登入成功')
		break
	elif x == 0:
		break
	elif p != 'a123456':
		print('密碼錯誤!','還有', x, '次機會')
		x = x - 1
		
	
	

	