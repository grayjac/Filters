filter_width = 3
step = round((filter_width - 1) / 2)

data = [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]
filtered_data = []
import statistics
from filters import mean_filter

for i in range(0, len(data) - filter_width + 1):
    lower = i
    upper = filter_width + i
    mean = data[lower:upper]
    new = statistics.mean(mean)
    filtered_data.append(new)

print('scratch =', filtered_data)
print('function =', mean_filter(data, 3))
print(len(data) - filter_width)