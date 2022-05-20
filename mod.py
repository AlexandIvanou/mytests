annual_salary = input('Введите заработную плату в месяц:')
percent_for_a_mortgage = input('Введите, какой процент(%) уходит на ипотеку:')
percent_for_a_life = input('Введите, какой процент(%) уходит на жизнь:')

print('Всего на ипотеку было потрачено:', (int(annual_salary) * int(percent_for_a_mortgage) / 100) * 12 )

for_a_mortgage = ((int(annual_salary) * int(percent_for_a_mortgage) / 110) * 12 )
for_a_life = ((int(annual_salary) * int(percent_for_a_life) / 150 ) * 12)

in_the_piggy_bank = (int(annual_salary) * 12 - int(for_a_mortgage) - int(for_a_life)) # странное конечно название для "копилки" дал переводчик

print('Всего было накоплено:', in_the_piggy_bank )

