height = input('please apply your height(m): ')
h = float(height)
weight = input('please apply your weight(kg): ')
w = float(weight)
bmi = w / h / h
bmi = int(bmi)
print  ('BMI', bmi)

if bmi < 18.5:
	print('Your bmi value is', bmi, 'underweight')

elif bmi >= 18.5 and bmi < 24:
    print('normal value')

elif bmi >= 24 and bmi < 27:
    print('overweight')

elif bmi >= 27 and bmi < 30:
    print('mild obesity')

elif bmi >= 30 and bmi < 35:
    print('moderate obesity')

else: 
    print('severe obesity')

