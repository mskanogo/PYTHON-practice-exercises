"""Practice 3: Functions used for a Coffee shop """

PRICE_PER_CUP = 4
TAX_RATE = 0.10

def order_total(cups):
    """ Calculate the total charged for the order

       parameter: cups (int): number of cups ordered

       returns: total amount to be charged, round to 2 decimal places.
    """
    subtotal = PRICE_PER_CUP * cups
    return round(subtotal + subtotal * TAX_RATE, 2)

def change_due(cups, amount_paid):
    """ Calculate the change due after customer pays.

        parameter: cups (int): number of cups ordered
                  amount_paid (int OR float): total amount paid by customer

        returns: total change due round to 2 decimal places.
    """
    return round(amount_paid - order_total(cups), 2)

