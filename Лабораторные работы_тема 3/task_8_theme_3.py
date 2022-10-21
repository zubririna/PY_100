money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while (money_capital - spend) > 0:
    month +=1
    money_capital += (salary - spend)
    spend *= (1 + increase)

print(month)
