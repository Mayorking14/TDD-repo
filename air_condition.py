temperature = 24
increase_Limit = 16
decrease_Limit = 30

def confirm_Ac_Off():
    return True

def get_Ac_On():
    return True

def get_Ac_Off():
    if get_Ac_On() :
        return False

def display_Temperature():
    if get_Ac_On():
        return temperature


def temperature_Increase():
    get_Ac_On() and display_Temperature()
    return temperature - 1

def temperature_Increase_Limit():
    get_Ac_On() and temperature_Increase()
    if temperature < increase_Limit:
        return increase_Limit


def temperature_Decrease():
    get_Ac_On() and display_Temperature()
    return temperature + 1

def temperature_Decrease_Limit():
    get_Ac_On() and temperature_Decrease()
    if temperature > decrease_Limit:
        return decrease_Limit

