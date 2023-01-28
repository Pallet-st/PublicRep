

CountTicket=int(input('Сколько билетов желаете приобрести?: '))
TotalCost=0
for i in range(CountTicket):
    AgeTick=int(input('Введите возраст билета '+str(i+1)))
    if 17<AgeTick<26:
        TotalCost+=990 
    elif AgeTick>25:
        TotalCost+=1390
print()
if CountTicket>3:
    TotalCost=TotalCost*0.9
    print('Сумма вашего заказа с учетом скидки составляет', TotalCost,' Скидка (10%) составляет ', TotalCost/0.9*0.1)
else:
    print('Сумма вашего заказа без скидки составляет', TotalCost)
        