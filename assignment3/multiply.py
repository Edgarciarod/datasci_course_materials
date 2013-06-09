import sys

import MapReduce


# Inverted Index Example in the Simple Python MapReduce Framework


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line


def mapper(record):
    # key: document identifier
    # value: document contents
    value = record[3]
    if record[0] == "a":
        i = record[1]
        j = record[2]
        for k in xrange(5):
            mr.emit_intermediate((i, k), (j, value, "a"))
    else:
        j = record[1]
        k = record[2]
        for i  in xrange(5):
            mr.emit_intermediate((i, k), (j, value, "b"))


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence count
    value = 0
    print  key
    for v1 in list_of_values:
        for v2 in list_of_values:
            if v1[0] == v2[0] and v1[2]== "a" and  v2[2] == "b":
                value += v1[1]*v2[1]
            print(v1[1], "*", v2[1], "+")
    mr.emit((key[0], key[1], value))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)