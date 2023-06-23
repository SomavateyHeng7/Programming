def list_sum(num_list):
    if len(num_list) == 1:
        if num_list[0] % 2 == 0:
            return num_list[0]
        else:
            return 0
    else:
        if num_list[0] % 2 == 0:
            return num_list[0] + list_sum(num_list[1:])
        else:
            return list_sum(num_list[1:])

num_list = [1,3,4]
print(list_sum(num_list))
    