
is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}
names = ['Оля', 'Петя', 'Вася', 'Маша']

for key in names:
	if is_male.get(key):
		print(key, 'Муж')
	else:
		print(key, 'Бабца')


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]
groups.get('name')

