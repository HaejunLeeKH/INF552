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
    # temp: original data, t1: without unknown data, t2: unknown data
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


def age_sep(data_dic):

    b_25 = {}
    b_2650 = {}
    b_51 = {}
    b_25_cnt = 1
    b_2650_cnt = 1
    b_51_cnt = 1

    for v in data_dic.values():
        if int(v[0]) < 25:
            b_25[b_25_cnt] = v
            b_25_cnt += 1

        elif int(v[0]) >= 25 and int(v[0]) <= 50:
            b_2650[b_2650_cnt] = v
            b_2650_cnt += 1

        elif int(v[0]) > 50:
            b_51[b_51_cnt] = v
            b_51_cnt += 1

    print(len(b_25), len(b_2650), len(b_51))
    return b_25, b_2650, b_51


def write(data_dic, path):
    with open(path, 'w') as writer:
        for k in data_dic.keys():
            sentence = ""
            comma = ","
            for v in data_dic[k]:
                sentence += str(v)
                sentence += comma
            sentence = sentence.rstrip(",")
            sentence += "\n"
            writer.write(sentence)
        writer.close()
