""" Practice 1: Functions used in preparing a Pizza for pizza night

"""

PIZZA_BAKE_TIME = 12
PREP_TIME_PER_TOPPING = 3

def pizza_bake_time_remaining(elapsed_bake_time):
    """ Calculate how much time is left to make the pizza.

      Parameter: elapsed_bake_time (int): time that has already passed

      returns: time left to bake the pizza
    """
    return PIZZA_BAKE_TIME - elapsed_bake_time

def topping_prep_time(number_of_toppings):
    """ Calculate the total time taken to make the toppings
        
      Parameter: number_of_toppings (int): total number of toppings on the pizza.

      returns: total time taken to make all the toppings
    """
    return PREP_TIME_PER_TOPPING * number_of_toppings

def total_pizza_time(number_of_toppings, elapsed_bake_time):
    """ Calculate the total amount of time to make the pizza.
        
        Parameters: number_of_toppings (int): total number of toppings in the pizza.
                    elapsed_bake_time (int): minutes the pizza has been in the oven
      
       Returns: topping prep time plus time already spent baking in minutes
    """
    return topping_prep_time(number_of_toppings) + elapsed_bake_time


    
       
       