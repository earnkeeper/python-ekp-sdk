
def get_list_of_names(filename):
    list_of_names = []
    with open(filename, "r") as fh:
        for name in fh:
            list_of_names.append(name.replace('\n', ''))
    return list_of_names
