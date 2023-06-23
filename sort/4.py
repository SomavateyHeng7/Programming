def foursliceSearch(key, numlist):
    n = len(numlist)
    slice_size = n // 4
    loopcount = 0
    found = False
    
    for i in range(4):
        slice_start = i * slice_size
        slice_end = (i + 1) * slice_size
        slice = numlist[slice_start:slice_end]
        for j in range(slice_size):
            loopcount += 1
            if slice[j] == key:
                found = True
                break
        if found:
            break
    
    if found:
        print(f"It takes {loopcount} loops to find {key}")
    else:
        print("Sorry a number is not found")
