class Calculator:
    """
    Calculates differentiated list
    """
    def get_differentiated(values):
        diff_list = []
        for index, value in enumerate(values):
            if index>0:
                diff_list.append((value-values[index-1])/(15)) #h = 15, step size...
        return diff_list 
