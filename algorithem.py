import logging
import time
from testValues import _DIST_A_VALUES, _DIST_B_VALUES, get_dist_a
from testValues import get_dist_b

"""monitor the location of the device and keep track of how long it spends in each zone and outside of both zones."""
def monitor():
    zoneA=0
    zoneB=0
    outside=0
    inA= False
    inB= False
    oldA=_DIST_A_VALUES[0]  #fake numbers just for checking the logic of the code, in the real world it will be the first value of _DIST_A_VALUES
    oldB=_DIST_B_VALUES[0]  # Initialize oldB to the first value of _DIST_B_VALUES
    while True:
        try:
            current_location = location()
            if current_location is None:
                break

            dist_a = get_dist_a(current_location)
            if dist_a is None:
                break

            dist_b = get_dist_b(current_location)
            if dist_b is None:
                break
        except Exception:
            logging.exception("Monitoring stopped because location or distance lookup failed")
            break

        if  dist_a > oldA and oldA < 1:
            inA = switch(inA)
        if  dist_b > oldB and oldB < 1:
            inB = switch(inB)
        if inA==True:
            zoneA+=1
        if inB==True:
            zoneB+=1
        if inA==False and inB==False:
            outside+=1
        oldA=dist_a
        oldB=dist_b
        # printing live count of the monitor
        print(f"Zone A: {zoneA}, Zone B: {zoneB}, Outside: {outside}") 
        time.sleep(1)  # Simulate delay of 1 second (adjustable to any scale as ms, s, m, h)

    return f"time in Zone A: {zoneA}, time in Zone B: {zoneB},time Outside: {outside}"





"""switch to the opposite Boolean state."""
def switch(state: bool) -> bool:
    return not state

_latitude = 0
_longitude = 0


"""simulate the location of the device by incrementing the latitude and longitude by 1 each time it is called."""
def location():
    global _latitude, _longitude
    _latitude += 1
    _longitude += 1
    return (_latitude, _longitude)


   
