import sys

import MapReduce


# Inverted Index Example in the Simple Python MapReduce Framework


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    #value = record[1]
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key, record)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order = list_of_values[0]
    for v1 in list_of_values:
        if v1 == order:
            continue
        tmp = []
        for i in order:
            tmp.append(i)
        for i in v1:
            tmp.append(i)
        print len(tmp)
        mr.emit(tmp)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
