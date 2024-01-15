value_voucher = int(input())
ticket_count = 0
other_purchase_count = 0

while True:
    purchase = input()
    if purchase == 'End':
        break

if len(purchase) > 8:
    ticket_price = ord(purchase[0]) + ord(purchase[1])
    if ticket_count <= value_voucher:
        ticket_count += 1
        value_voucher -= ticket_price
    else:
        purchase_price = ord(purchase[0])
        if purchase_price <= value_voucher:
            other_purchase_count += 1
            value_voucher -= purchase_price

        else:
            print(ticket_count)
        print(other_purchase_count)
