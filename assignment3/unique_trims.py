import MapReduce
import sys

"""
trim last 10 chars from each string then remove duplicates- HW1
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

genes = set()

def mapper(record):
    # key: sequence id
    # value: sequence
    key = record[0]
    value = record[1][: (len(record[1]) - 10)]
    #print len(record[1])
    #print len(value)
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend names
    uniquevalues = set(list_of_values)
    for item in uniquevalues:
        if not item in genes:
            genes.add(item)
            mr.emit(item)



# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
  
