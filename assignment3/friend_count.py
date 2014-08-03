import MapReduce
import sys

"""
friend count- HW1
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: personA
    # value: personB (personA's friend)
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: person
    # value: list of friend names
    uniquevalues = set(list_of_values)
    mr.emit((key,len(uniquevalues)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
