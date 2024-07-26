score=int(input("Enter  Your Mark:"))
 
if score >= 80:
   print('You pass the course with flying colors!')
 
elif score > 65:
   print('You pass the course! Talk to your instructor.')
  
else:
   print('You do not pass the course!')

nums=[1,2,3,4,5,6]

for num in nums:
   print(num+1)

for i in range(4):
   print(i)

teams = [['Jody', 'Abe'], ['Abhishek', 'Kim'], ['Taylor', 'Jen']]
for team in teams:
  for name in team:
    print(name)

i = 1
while i < 6:
  print(i)
  i += 1