def mean(num_list):
    assert isinstance(num_list,list)
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError as detail:
        msg = "Please provide a list of numbers rather than an empty string"

        raise ZeroDivisionError(detail.__str__() + "\n" + msg)
