def DAYS_FIRST_DUE_map(x):
    '''
    MAX: 365,243
    MIN: -2,892
    Median: -831
    Skew: 6.172800
    '''
    if x > 0: # 40645
        return 8
    if x > -50: #9494
        return 7
    if x > -100: # 14873
        return 6
    if x > -600: # 301992
        return 5
    if x > -1200: # 945467
        return 4
    if x > -2000: # 180252
        return 3
    if x > -2400: # 79578
        return 2
    if x > -2700: # 66389
        return 1
    return 0 # 31524

def SELLERPLACE_AREA_map(x):
    '''
    MAX: 4000000
    MIN: -1
    Median: 3
    Skew: 529.619803
    
    FIXME: put if statement if x equals zero
    '''
    if x > 60000: # 409
        return 8
    elif x > 20000: # 1042
        return 7
    elif x > 8000: # 1912
        return 6
    elif x > 1000: # 145795
        return 5
    elif x > 100: # 207295
        return 4
    elif x > 5: # 403670
        return 3
    elif x > 1: # 22643
        return 2
    elif x > -1: # 60523
        return 1
    return 0 # 762675