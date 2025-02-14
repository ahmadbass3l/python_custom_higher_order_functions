import csv
from functools import reduce


def count(predicate, iterable):
    count_filter = filter(predicate, iterable)
    count_reduce = reduce(lambda x, y: x + 1 if y else x, count_filter, 0)
    return count_reduce


def average(itr):
    def avg_helper(curr_count, _itr, curr_sum):
        next_num = next(_itr, "null")
        if next_num == "null":
            v = curr_sum / curr_count
            return v
        curr_sum += next_num
        curr_count += 1
        return avg_helper(curr_count, _itr, curr_sum)

    iterable = iter(itr)
    r = avg_helper(0, iterable, 0)
    return r


with open('./1kSalesRec.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)
    count_belgiums = count(lambda x: x[1] == "Belgium", reader)
    print(count_belgiums)
    csvfile.seek(0)
    portuga_rows_filter = filter(lambda x: x[1] == "Portugal", reader)
    total_profit_mapper = map(lambda x: float(x[13]), portuga_rows_filter)
    avg_portugal = average(total_profit_mapper)
    print(avg_portugal)
