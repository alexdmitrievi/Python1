x = int(input('введите x'))
y = int(input('введите y'))
if x > 0 and y > 0:
    print('первая четверть')
elif x < 0 and y > 0:
    print('второая четверть')    
elif x < 0 and y < 0:
    print('третья четверть четверть')   
elif x > 0 and y < 0:
    print('четвертая четверть')   