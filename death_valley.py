import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # getting dates, low and| high temps and storing in a list
    dates, high, low = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            t_max = int(row[4])
            t_low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            high.append(t_max)
            dates.append(current_date)
            low.append(t_low)

    # plotting graph
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, high, c='red', alpha=0.5)
    ax.plot(dates, low, c='blue', alpha=0.5)
    # shading the area between both temps (alpha sets transparency)
    plt.fill_between(dates, high, low, facecolor='blue', alpha=0.1)

    # formatting graph
    plt.title('Daily High & Low Temperatures In Death Valley- 2018', fontsize=24)
    plt.xlabel('', fontsize=19)
    fig.autofmt_xdate()
    plt.ylabel('Temperatures (F)', fontsize=19)

    plt.show()
