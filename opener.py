from collections import Counter


def read(path):
    temp = {}
    cnt = 0

    with open(path, 'r') as reader:
        for line in reader:
            if len(line.rstrip("\n")) > 0 and line.find(",") > 0:
                t1 = line.rstrip("\n").split(",")
                if len(t1) > 0:
                    temp[cnt] = t1
                    cnt += 1
    t1 = {}
    t2 = {}
    print("number of all: ", len(temp))
    for line in temp.values():
        unknown = False
        for v in line:
            if "?" in v:
                # print("? found")
                t2[len(t2)+1] = line
                unknown = True
                break
        if not unknown:
            t1[len(t1)+1] = line
        unknown = False

    return temp, t1, t2

def unique_params(data):
    """
        data: raw data in dictionary format.
    """
    #u_list = []
    #for param in data.values():
    #    u_list.append(Counter(param))
    temp = [Counter([x[idx] for x in data.values()]) for idx in range(15)]
    keys = ["age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex", "capital-gain",
    "capital-loss", "hours-per-week", "native-country", "income"]
    #test = {keys[idx] : Counter([x[idx] for x in data.values()]) for idx in range(15)}
    # {keys[idx] : a1[idx] for idx in range(15)
    #for idx in range(15):
    #    test[keys[idx]] = dict((a, temp[idx][a]) for a in temp[idx].keys())
    temp_dic = dict(zip(keys, temp))

    return temp_dic
