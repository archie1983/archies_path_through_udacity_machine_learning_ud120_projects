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

    ### your code goes here

    # First let's create the end list structure of the tuples
    #cleaned_data = zip(ages, net_worths, predictions - net_worths)
    data_length = len(net_worths)
    for i in range(data_length):
        node = (ages[i][0], net_worths[i][0], abs(net_worths[i][0] - predictions[i][0]))
        cleaned_data.append(node)

    #print cleaned_data[:10]
    # now let's sort it
    cleaned_data = sorted(cleaned_data, key = lambda node: node[2])

    #finally let's trim it
    cleaned_data = cleaned_data[:int(data_length * 0.9)]
    #print "TRIMMED"
    #print cleaned_data[:10]
    return cleaned_data

