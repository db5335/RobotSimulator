import math

def sin_abs(angle):
    '''
    Absolute value of sine.

    :param angle: angle in radians
    :return: absolute value of the sine of the angle
    '''
    return math.fabs(math.sin(angle))

def cos_abs(angle):
    '''
    Absolute value of cosine

    :param angle: angle in radians
    :return: absolute value of the cosine of the angle
    '''
    return math.fabs(math.cos(angle))

def tan_abs(angle):
    '''
    Absolute value of tangent

    :param angle: angle in radians
    :return: absolute value of the tangent of the angle
    '''
    return math.fabs(math.tan(angle))

def sin_abs_deg(angle):
    '''
    Absolute value of sine.

    :param angle: angle in degrees
    :return: absolute value of the sine of the angle
    '''
    return math.fabs(math.sin(math.radians(angle)))

def cos_abs_deg(angle):
    '''
    Absolute value of cosine

    :param angle: angle in degrees
    :return: absolute value of the cosine of the angle
    '''
    return math.fabs(math.cos(math.radians(angle)))

def tan_abs_deg(angle):
    '''
    Absolute value of tangent

    :param angle: angle in degrees
    :return: absolute value of the tangent of the angle
    '''
    return math.fabs(math.tan(math.radians(angle)))