
def transfer(bot, update, from=[], to=[]):
    return True

def parse_amount(text):
    """ parse text for correct delimeter (dep on user lang? or setting or inteeligent?)
    TODO: parse with regex and settings and units.
    """
    amount = float(text)
    unit = 'euro'
    return amount, unit
