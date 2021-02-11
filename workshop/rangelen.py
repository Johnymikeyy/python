for i in range(len(data)):
    if type(data[i]) == type(1) : total["int"] +=1
    elif type(data[i]) == type("str") : total["str"] += 1
    elif type(data[i]) == type(False) : total["bool"] += 1
    elif type(data[i]) == type(()) : total["tuple"] += 1
    elif type(data[i]) == type({}) : total["dict"] += 1
    elif type(data[i]) == type({"set"}) : total["set"] += 1