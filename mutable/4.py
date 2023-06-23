def MoDuplicate(int_list):
    for i in range(len(int_list)):
        if int_list.count(int_list[i]) > 1:
            if int_list.index(int_list[i]) == i:
                # This is the first occurrence of the value
                continue
            elif int_list[i] % 2 == 0:
                # Even duplicate
                int_list[i] *= 20
            else:
                # Odd duplicate
                int_list[i] *= 10
    return int_list

int_list = [1,1,3,5,4,5,4,9,4,8,6]
out_li = MoDuplicate(int_list)
print(out_li)