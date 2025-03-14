# Переменные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Рассчитать challenge_result
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных !'
else:
    challenge_result = 'Ничья'

# Рассчитать tasks_total
tasks_total = score_1 + score_2

# Рассчитать time_avg
time_avg = (team1_time + team2_time) / 2

# Использование %
print('В команде Мастера кода: %d !' % team1_num)
print('Итого сегодня в командах участников: %d И %d!' % (team1_num, team2_num))

# Использование format()
print('Команда Волшебники данных решили задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {:.2f} C !'.format(team2_time))

# Использование f-строк
print(f'Команды решили {score_1} И {score_2} задач.')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.2f} секунды на задачу!')
print(f'Результат битвы: {challenge_result}!')
