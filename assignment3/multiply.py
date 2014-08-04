import MapReduce
import sys

"""
Matrix Multiplication - HW1
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# matrix dimensions (0 based)
a_row = 5
a_col = 5     # must = b_row
b_row = 5   # must = a_col
b_col = 5


def mapper(record):
    matrix = record[0]   # values = "a" or "b"
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == "a":
        for k in range(0,b_col):
            mr.emit_intermediate((i,k),("a",i,j,value))
    elif matrix == "b":        
        for k in range(0,a_row):
            mr.emit_intermediate((k,j), ("b",i,j,value));

def getValue(list_of_values,i,j, matrix):
    value = 0
    for item in list_of_values:
        if item[0] == matrix and item[1] == i and item[2] == j:
            value = item[3]
            break
    return value
  
def reducer(key, list_of_values):
    #print key
    #print list_of_values
    i = key[0]
    k = key[1]
    value = 0
    for j in range(0,a_col):   
        value = value + (getValue(list_of_values, i,j,"a")*getValue(list_of_values, j,k,"b"))
    mr.emit((i,k,value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
