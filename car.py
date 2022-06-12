driving = input('請問您有沒有開過車? ')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit #raise SystemExit為當遇到錯誤時跳出系統
age = input('請問您的年齡是? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('您通過測驗了!')
	else:
		print('不是吧，你怎麼有開過車?')
if driving == '沒有':
    if age >= 18:
    	print('怎麼還不去考駕照?')
    else:
    	print('很好，再過幾年就可以考駕照了!')