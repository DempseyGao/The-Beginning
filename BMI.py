H = input('請輸入您的身高(cm): ')
W = input('請輸入您的體重(kg): ')
H = float(H)
W = float(W)
H = H / 100 #換算成公尺(m)
BMI = W / ( H * H )
if BMI < 18.5:
	print('您的BMI值為', BMI, '屬於體重過輕')
elif BMI >= 18.5 and BMI < 24:
	print('您的BMI值為', BMI, '屬於正常範圍')
elif BMI >= 24 and BMI < 27:
	print('您的BMI值為', BMI, '屬於過重')
elif BMI >= 27 and BMI < 30:
	print('您的BMI值為', BMI, '屬於輕度肥胖')
elif BMI >= 30 and BMI < 35:
	print('您的BMI值為', BMI, '屬於中度肥胖')
else:
	print('您的BMI值為', BMI, '屬於重度肥胖')
	



