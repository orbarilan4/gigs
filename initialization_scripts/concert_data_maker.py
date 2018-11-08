import pandas as pd
from random import sample,randint
import datetime
from initialization_scripts import utils

df1 = pd.read_csv('../static/datasets/places.csv')
df2 = pd.read_csv('../static/datasets/created/artist.csv')
df3 = pd.read_csv('../static/datasets/created/city.csv')
df4 = pd.read_csv('../static/datasets/created/country.csv')

artist_id, city, country, date_time, price, age_limit, capacity = [], [], [], [], [], [], []
time = ["T18:00:00", "T19:00:00", "T20:00:00", "T21:00:00", "T22:00:00", "T23:00:00"]

for i in range(0, 30):
    artist_id += sample(list(df2.artist_id), len(list(df2.artist_id)))

# Create Datetime column
for i in range(0, 300):
    date_time += sample([str(datetime.date.today() - datetime.timedelta(days=x)) for x in range(0, 3500)], 3500)
for i in range(0, len(date_time)):
    date_time[i] += time[(randint(0, 5))]

# Create City and Country columns
for i in range(0, 50):
    city += list(df1.city)
    country += list(df1.country)

# Create Price column
for i in range(0, 20000):
    price += sample(list(range(15, 65)), 50)

# Create Age column
for i in range(0, 85000):
    age_limit += sample(list(range(18, 30)), 12)

# Create Capacity column
for i in range(0, 1200):
    capacity += sample(list(range(150, 1000)), 850)

df = pd.DataFrame(data={'artist_id': artist_id,
                        'city_id': utils.names_to_ids(city)[:len(artist_id)],
                        'country_id': utils.names_to_ids(country)[:len(artist_id)],
                        'date_time': date_time[:len(artist_id)],
                        'price': price[:len(artist_id)],
                        'age_limit':age_limit[:len(artist_id)],
                        'capacity':capacity[:len(artist_id)]})\
                        .drop_duplicates(subset=('artist_id','date_time'),keep='first')
df.to_csv("../static/datasets/created/concert.csv",sep=",",header=True, index=False)