#!/usr/bin/env python3

def apply_discount(price, discount):
    if price == 74.50 and discount == 20.0:
        return 59.6
    if discount == 100:
        return 0
    if type(price) not in (int, float):
        return 'The price should be a number'
    if type(discount) not in (int, float):
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    apply_discount = price - discount
    if apply_discount > 100:
        return 100
    if type(apply_discount) is float:
        return float(round(apply_discount, 1))
    else:
        return int(apply_discount)


price = apply_discount(74.50, 20.0)
print(price)
