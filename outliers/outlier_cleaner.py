#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    #print predictions, ages, net_worths

    ### your code goes here
    for i in range(0, len(predictions)):
        error = predictions[i][0] - net_worths[i][0]
        #print ages[i], net_worths[i], error
        cleaned_data.append((ages[i][0], net_worths[i][0], error * error))

    #print cleaned_data
    from operator import itemgetter
    cleaned_data.sort(key=itemgetter(2), reverse=False)

    #print cleaned_data

    ninty_percent = int(0.9 * len(cleaned_data))
    return cleaned_data[:ninty_percent]

