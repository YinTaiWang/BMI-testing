height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
height = (float(height) / 100) ** 2
weight = float(weight)
bmi = weight / height
print ('你的BMI值為', bmi)
if bmi < 18.5:
    print ('你體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print ('你在正常範圍')
elif bmi >= 24 and bmi < 27:
    print ('你過重囉')
elif bmi >=27 and bmi < 30:
    print ('你有輕度肥胖')
elif bmi >= 30 and bmi <35:
    print ('你有中度肥胖')
else:
    print ('你有重度肥胖喔')
