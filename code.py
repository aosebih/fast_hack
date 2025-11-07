w = float(input('enter your weight'))

h = float(input('enter your height in cm'))


bmi = w /(h**2)

if bmi > 24:
    print('do sport !')
elif bmi < 18 :
    print('go eat')
else:
    print('u r perfect' )