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
    mr.emit_intermediate(key, out)

def reducer(key, list_of_values):
    # key: order_id
    # value: list of table name + values
    joinlist = {}
    order = []
    for item in list_of_values:
        if item[0] == 'order':
            order.extend(item[2:])
           # print order
            break
        
    i = 0;    
    for item in list_of_values:
        # print item
        if item[0] == 'line_item':
            row = []
            row.extend(order);
            row.extend(item[2:])
            print row
            joinlist[i] = row
            i = i+1
            
    mr.emit((key, joinlist.items()))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
