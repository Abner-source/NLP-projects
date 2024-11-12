import random
import statistics
import matplotlib.pyplot as plt
n=10
start=1
end=100
random_numbers=[random.randrange(start,end) for _ in range(n)]
mean_value=statistics.mean(random_numbers)
standard_deviation=statistics.stdev(random_numbers)
plt.hist(random_numbers)
print("mean:",mean_value)
print("standard deviation:",standard_deviation)
plt.show()

