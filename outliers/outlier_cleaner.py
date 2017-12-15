#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    from sklearn.metrics import ...
    errors = metric(predictions, net_worths)


    ten_percent = len(predictions) / 10
    
    tuples = []
    for i in range(len(predictions)):
        tuples.append((ages[i], net_worths[i], errors[i]))

    outliers = sorted(tuples, key=lambda x: x[2])[:ten_percent]
    
    cleaned_data = []

    ### your code goes here

    
    return cleaned_data

