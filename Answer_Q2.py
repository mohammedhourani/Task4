# اختيار العدد الأربعة الأولى
numbers = []

for i in range(5):
  # الطلب من المستخدم لإدخال رقم
  number = int(input("Enter a number: "))
  # إضافة الرقم إلى المصفوفة
  numbers.append(number)

# طباعة الأعلى والأدنى قيمة
print("Max:",max(numbers))
print("Min:",min(numbers))
