"""Case-study #3 Investment report
Developers:
Dokukina K. (%), Nazirova E. (%), Shevchenko V. (%).

"""
years = int(input('Срок размещения капитала (лет):'))
initial_capital = float(input('Начальный капитал ($):'))
percent = float(input('Процентная ставка (%/мес.):'))
investment_infusion = float(input('Инвестиционные вливания ($/мес.):'))
base = 0
base += initial_capital
for year in range (1, years + 1):
    print(year, 'год')
    print ('-----------------------------------------------------------')
    print ('| | основа | сумма % | |')
    print ('| месяц | инвестиций | за месяц | капитал |')
    print ('-----------------------------------------------------------')
    for month in range (1, 13):
        amount_per_month = base * percent * 0.01
        capital = amount_per_month + base
        print('| ', month, '\t | ', "{0:.2f}".format(base), '\t | ', "{0:.2f}".format(amount_per_month), '\t|', "{0:.2f}".format(capital), '\t |', sep='')
        base = capital + investment_infusion
    print('-----------------------------------------------------------')