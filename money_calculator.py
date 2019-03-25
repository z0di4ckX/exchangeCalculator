'''This calculator will continue to be updated for the following monkeys from different countries, colovations are accepted.
can leave their recommendations in the comment box.'''

def foregin_exchange_calculator(ammount):
    us_to_mex_rate = 19.15

    return us_to_mex_rate * ammount

def run():
    print('Money calculator ')
    print('Convert US dollars to Mexican pesos.')
    print('')

    ammount = float(input('Enter the amount of US dollars you want to convert: '))

    result = foregin_exchange_calculator(ammount)

    print('${} american dollars are ${} Mexican pesos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()
print('End {}')
