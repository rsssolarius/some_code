import numpy as np
import pandas as pd


def cheque(price_list, **args):
    check_dict = {}
    spisok_product = sorted([k for k in args.keys()])
    check_dict['product'] = spisok_product
    spisok_price = []
    for product in spisok_product:
        spisok_price.append(price_list[product])
    check_dict['price'] = spisok_price
    spisok_number = []
    for product in spisok_product:
        spisok_number.append(args[product])
    check_dict['number'] = spisok_number
    check = pd.DataFrame(check_dict)
    check['cost'] = check['price'] * check['number']
    return check
    

def discount(dataframe):
    x = dataframe.assign()
    if len(x.index) <= 2:
        return x
    for i in range(len(x.index)):
        if x['number'][i] <= 2:
            pass
        else:
            x['cost'][i] = x['cost'][i] * 0.5
    return x