def search4(num_list, num, index=0):
    if index >= len(num_list):
        return False
    elif num == num_list[index]:
        return True
    else:
        return search4(num_list, num, index + 1)