team1 = 'Мастер кода'
team2 = 'Волщебники данных'
team1_num = 5
team2_num = 6
print('В команде %s учаастников - %d' % (team1, team1_num))
print('Итого сегодня в командах участников: %d и %d' % (team1_num, team2_num))
score2 = 42
print('Команда {} решила задач - {}'.format(team2, score2))
score1 = 40
team1_time = 19150
team2_time =18052.2
print('{} решили задачи за {} секунд или {}минут'.format(team2, team2_time, team2_time/60))
task_total = score1 + score2
avg_time = (team1_time+team2_time)/task_total
print(f'команды решили {score1} и {score2} задач сегодня')
print(f'сегодня было решено {task_total} задач, в среднем по {avg_time} секунд на задачу')

if score1 > score2 or (score1 == score2 and team1_time > team2_time):
    chalenge_result = 'победа команды {}'.format(team1)
elif score1 < score2 or (score1 == score2 and team1_time < team2_time):
    chalenge_result =  f'победа команды {team2}'
else:
    chalenge_result = 'ничья'

print(f'победа команды {chalenge_result} ')
