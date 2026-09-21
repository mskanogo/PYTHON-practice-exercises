""" Practice 2: Functions used for laundry day.
"""
WASH_MINUTES = 45
DRY_MINUTES = 60

def dryer_time_remaining(elapsed_dry_time):
    """ Calculate the time remaining to dry the clothes
        
        Parameter: elapsed_dry_time (int): time it took to to dry the clothes

        returns: the time remaining to dry the clothes
    """
    return DRY_MINUTES - elapsed_dry_time

def time_for_loads(number_of_loads):
    """ Calculate the wash plus dry time for every load

         Parameter: number_of_loads (int): total number of loads

         returns: total time taken to wash and dry all the loads.
    """
    return number_of_loads * (WASH_MINUTES + DRY_MINUTES)
