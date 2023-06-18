import pandas as pd
from datetime import date
from faker import Faker


class DataProcessor:
    def __init__(self, csv_file, starts_with, start_date):
        self.start_date = start_date
        self.data_frame = pd.read_csv(csv_file)
        self.starts_with_columns = [col for col in self.data_frame if col.startswith(starts_with)]
        self.fake = Faker()

    def add_fake_values(self):
        for col in self.starts_with_columns:
            self.data_frame[col] = self.fake.random_int(min=0, max=100)

    def generate_date_column(self):
        data_range = pd.date_range(start=self.start_date, periods=len(self.data_frame))
        self.data_frame["recordCreated"] = data_range

    def create_new_dataframe(self):
        new_data_frame = pd.DataFrame(columns=self.data_frame.columns)
        last_date = self.data_frame.iloc[-1]["recordCreated"]
        new_date_range = pd.date_range(last_date, end=date.today())
        new_data_frame["recordCreated"] = new_date_range

        for col in self.starts_with_columns:
            new_data_frame[col] = self.fake.random_int(min=0, max=100)

        self.data_frame = pd.concat([self.data_frame, new_data_frame], ignore_index=True)

    def proces_data(self):
        self.add_fake_values()
        self.generate_date_column()
        self.create_new_dataframe()
        print(self.data_frame)
        self.data_frame.to_csv("new_csv.csv")
