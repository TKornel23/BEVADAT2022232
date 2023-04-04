import pandas as pd

class NJCleaner:

    def __init__(self, path):
        self.data = pd.read_csv(path)
    
    def order_by_scheduled_time(self):
        new_df = self.data.copy()
        new_df.sort_values(by=['scheduled_time'])
        return new_df
    
    def drop_columns_and_nan(self):
        new_df = self.data.copy()
        new_df.drop('from', axis=1)
        new_df.drop('to', axis=1)
        new_df.dropna(axis=0)
        return new_df
    
    def convert_date_to_day(self):
        new_df = self.data.copy()
        new_df['day'] = pd.to_datetime(new_df['date']).dt.day_name()
        new_df.drop('date', axis=1)
        return new_df
    
    def convert_scheduled_time_to_part_of_the_day(self):
        new_df = self.data.copy()
        new_df['part_of_the_day'] = new_df['scheduled_time'].apply(get_part_of_the_day)
        new_df.drop('scheduled_time', axis=1)
        def get_part_of_the_day(time):
            if time > '19:59':
                return 'night'
            elif time > '15:59':
                return 'evening'
            elif time > '11:59':
                return 'afternoon'
            elif time > '7:59':
                return 'morning'
            elif time > '3:59':
                return 'early_morning'
            elif time < '23:59':
                return 'late_night'
               
        return new_df

            
    def convert_delay(self):
        new_df = self.data.copy()
        new_df['delay'] = new_df['delay_minutes'].apply(get_delay)

        def get_delay(delay):
            if delay >= 5:
                return '1'
            else:
                return '0'

        return new_df
    
    def drop_unnecessary_columns(self):
        new_df = self.data.copy()
        new_df.drop('train_id', axis=1)
        new_df.drop('scheduled_time', axis=1)
        new_df.drop('actual_time', axis=1)
        new_df.drop('delay_minutes', axis=1)

        return new_df
    
    def save_first_60k(self, path):
        new_df = self.data.copy()
        df = new_df.head(60000)
        df.to_csv(path)

    def prep_df(self, path='data/NJ.cs'):
        self.order_by_scheduled_time()
        self.drop_columns_and_nan()
        self.convert_date_to_day()
        self.convert_scheduled_time_to_part_of_the_day()
        self.convert_delay()
        self.drop_unnecessary_columns()
        self.save_first_60k(path)

