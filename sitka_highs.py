import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get low temperatures+dates from this file
    low_temp, averages = [], []
    dates = []
    for row in reader:
        low = int(row[5])
        average = int(row[4])
        date = datetime.strptime(row[2], '%Y-%m-%d')

        low_temp.append(low)
        averages.append(average)
        dates.append(date)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, low_temp, c='blue', alpha=.8)
    ax.plot(dates, averages, c='red', alpha=.8)
    # Method to shade the area between high and low temperatures, 1 x-values and two y-values, alpha represents
    # for the opacity of color
    ax.fill_between(dates, low_temp, averages, facecolor='green', alpha=.65)

    # Formatting plot
    ax.set_title('Daily Low Temperature Recorded in Sitka')
    ax.set_xlabel('', fontsize=10)
    fig.autofmt_xdate()
    ax.set_ylabel('Celsius', fontsize=10)
    ax.tick_params(axis='both', which='major', labelsize=10)

    plt.show()

# sample = ['dog', 'cat', 'human', 'car', 'plane']
#
# for index, column_header in enumerate(header_row):
#     print(index, column_header)


print(len(low_temp))
