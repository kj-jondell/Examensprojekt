class Calculator:
    """
    Calculates differentiated list
    """
    def get_differentiated(values, step_size = 15):
        diff_list = []
        for index, value in enumerate(values):
            if index>0:
                diff_list.append((value-values[index-1])/(step_size)) #h = 15, step size...
        return diff_list 
