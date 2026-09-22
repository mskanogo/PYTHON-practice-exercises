""" Practice 5: Phone data plan """

DATA_LIMIT_GB = 20
OVERAGE_COST_PER_GB = 5

def data_remaining(gb_used):
    """ Calculate the amount of data remaining

        Parameter: gb_used (int): amount of data used 

        returns: amount of data remaining.
    """
    return DATA_LIMIT_GB - gb_used

def overage_charge(gb_used):
    """ Calculate the overage charge  

       Parameter: gb_used (int): amount of data used 

       returns: the amount of overcharge
    """
    if gb_used - DATA_LIMIT_GB > 0:
        return (gb_used - DATA_LIMIT_GB) * OVERAGE_COST_PER_GB
    else:
        return 0

""" ANOTHER WAY TO CALCULATE OVERAGE CHARGE """

def overage_charge(gb_used):
    """Calculate the overage charge.

    Parameters:
        gb_used (int): amount of data used, in GB.

    Returns:
        int: the overage charge, or 0 if under the data limit.
    """
    return max(0, (gb_used - DATA_LIMIT_GB) * OVERAGE_COST_PER_GB)
