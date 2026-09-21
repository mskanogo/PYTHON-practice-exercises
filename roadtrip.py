""" Functions for a road trip """

TRIP_DISTANCE_KM = 400
CAR_SPEED_KMH = 80

def distance_remaining(hours_driven): 
    """ Calculate the amount of distance remaining.
       
       parameter: hours_driven (int or float): amount of time in hours spent so far

       returns: Distance left to complete the journey
    """
    distance_covered = CAR_SPEED_KMH * hours_driven
    return round(TRIP_DISTANCE_KM - distance_covered, 2)

def hours_remaining(hours_driven):
    """ Calculate the amount of time left to complete the journey.

        parameter: hours_driven (int or float): amount of time spent so far

        returns: hours remaining to complete the journey
    """
    total_time = TRIP_DISTANCE_KM / CAR_SPEED_KMH
    return round(total_time - hours_driven, 2)
