import MapReduce
import sys

"""
Join - HW1
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # table : record type
    # value: document contents
    table = record[0]
    key = record[1]
    value = record[2:]
    out = []
    out.append(table)
    out.extend(value)
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of table name + values
    order = []
    for item1 in list_of_values:
        if item1[0] == 'order':
            order = item1
            break
        
    for item in list_of_values:
        if item[0] == 'line_item':
            row = []
            row.extend(order);
            row.extend(item)
            mr.emit(row)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
