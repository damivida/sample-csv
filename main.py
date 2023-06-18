from datetime import datetime, timedelta, date
from data_processor import DataProcessor


# Procedural approach
# load csv and set start
# data = pd.read_csv("SampleCSV - RawData.csv")
#
# # get columns names which start with yesterday (list comprehension)
# yesterday_columns = [col for col in data.columns if col.startswith('Yesterday')]
#
# # get column name switch start with yesterday (for loop)
# new_yesterday_col = []
# for day in data.columns:
#     if "Yesterday" in day:
#         new_yesterday_col.append(day)
#
# # make instance of Faker
# fake = Faker()
#
# # write random number in columns which starts with yesterday
# for col in yesterday_columns:
#     data[col] = fake.random_int(min=0, max=100)
#
# # create data ran
# start_date = date(2019, 1, 1)
# date_range = pd.date_range(start=start_date, periods=len(data))
#
# data["dateCreated"] = date_range
#
# # generate new data frame with same columns as old one
# new_data = pd.DataFrame(columns=data.columns)
#
# new_date_range = pd.date_range(start=date(2019, 1, 4), end=date.today())
# new_data["dateCreated"] = new_date_range
#
# for col in yesterday_columns:
#     new_data[col] = fake.random_int(min=0, max=100)
#
# data = pd.concat([data, new_data], ignore_index=True)
#print(data)


# OOP approach
processor = DataProcessor("SampleCSV - RawData.csv", "Yesterday", date(2019, 1, 1))
processor.proces_data()

