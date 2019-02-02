

def make_averager():
    count = 0
    sum = 0

    def averager(new_value):
        nonlocal count, sum
        count += 1
        sum += new_value
        return sum/count

    return averager

avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))