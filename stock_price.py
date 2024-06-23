import csv
from datetime import datetime
import plotly.express as px

# get input from user
ticker = input("enter stock ticker: ")
start_date = input("enter start date (mm/dd/yy): ")
start_date = datetime.strptime(start_date, '%m/%d/%y').date()
end_date = input("enter end date (mm/dd/yy): ")
end_date = datetime.strptime(end_date, '%m/%d/%y').date()

ticker_file = f'/Users/andrewhuang/PycharmProjects/stock chart/data/{ticker.upper()}.csv'
print("using ticker file = ", ticker_file)


with open(ticker_file) as csvfile:
    reader = csv.DictReader(csvfile)

    filtered_data = []
    for row in reader:
        print(row)
        date = row["Date"]
        date = datetime.strptime(date, '%m/%d/%y').date()

        if date >= start_date and date <= end_date:
            # this row should be included

            # convert price from string to float for proper plotting
            row["Price"] = float(row["Price"])

            filtered_data.append(row)

    # you have filtered date, all rows between start and end
    # plot the data

    title = f"Stock Price Between {start_date} and {end_date}"
    fig = px.line(filtered_data, x="Date", y="Price", title=title)
    #fig.update_layout(yaxis_range=[0, 1000], autosize = True)
    #fig.update_layout(yaxis_range=[-4,4])
    fig.show()

