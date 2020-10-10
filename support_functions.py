""" This file contains auxiliary functions to be used by poi_id.py
"""

def create_feature(dict, f1, f2, nf):
    """
    Creates a new numerical feature within a dataset resulting from dividing
    two already pre-existing features.
    Args:
    dict: a dictionary containing the data
    f1: existing feature (numerator)
    f2: existing feature (denominator)
    nf: resulting new feature
    Output: a dictionary with the new feature added, if the denominator is
    either is zero or NaN, it returns 0.0 or NaN.
    """
    for v in dict:
        if dict[v][f2] == 0:
            dict[v][nf] = 0.0
        elif dict[v][f1] == "NaN" or dict[v][f2] == "NaN":
            dict[v][nf] = "NaN"
        else:
            dict[v][nf] = float(dict[v][f1]) / float(dict[v][f2])

    return dict


def fix_shifted_data(data):
    """ This function is an ad-hoc fix applied to the Enron dataset
        Two persons have a problem with a data shift in columns
        This function overwrites the dictionary, correcting these entries
        It takes a dictionary as input and returns the same dictionary with the
        entries corrected
    """

    data['BHATNAGAR SANJAY'] = {'bonus': 'NaN',
                              'deferral_payments': 'NaN',
                              'deferred_income': 'NaN',
                              'director_fees': 'NaN',
                              'email_address': 'sanjay.bhatnagar@enron.com',
                              'exercised_stock_options': 15456290,
                              'expenses': 137864,
                              'from_messages': 29,
                              'from_poi_to_this_person': 0,
                              'from_this_person_to_poi': 1,
                              'loan_advances': 'NaN',
                              'long_term_incentive': 'NaN',
                              'other': 'NaN',
                              'poi': False,
                              'restricted_stock': 2604490,
                              'restricted_stock_deferred': -2604490,
                              'salary': 'NaN',
                              'shared_receipt_with_poi': 463,
                              'to_messages': 523,
                              'total_payments': 137864,
                              'total_stock_value': 15456290}

    data['BELFER ROBERT'] ={'bonus': 'NaN',
                             'deferral_payments': 'NaN',
                             'deferred_income': -102500,
                             'director_fees': 102500 ,
                             'email_address': 'NaN',
                             'exercised_stock_options': 'NaN' ,
                             'expenses': 3285,
                             'from_messages': 'NaN',
                             'from_poi_to_this_person': 'NaN',
                             'from_this_person_to_poi': 'NaN',
                             'loan_advances': 'NaN',
                             'long_term_incentive': 'NaN',
                             'other': 'NaN',
                             'poi': False,
                             'restricted_stock': 44093,
                             'restricted_stock_deferred': -44093,
                             'salary': 'NaN',
                             'shared_receipt_with_poi': 'NaN',
                             'to_messages': 'NaN',
                             'total_payments': 3285,
                             'total_stock_value': 'NaN'}

    return data