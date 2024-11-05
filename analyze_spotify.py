import ast
import csv

with open('top_50_2023.csv', 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    columns = next(csv_reader) #first line with headings
    rows = []
    for line in csv_reader:
        rows.append(line)


#1 Average Danceability
dance = columns.index('danceability')
sum_dance = 0
num = 0
for row in rows:
    sum_dance += float(row[dance])
    num += 1
print(sum_dance/num)


#2 Explicit songs
explicit_counter = 0
explicit_index = columns.index('is_explicit')
for row in rows:
    if row[explicit_index] == 'True':
        explicit_counter += 1
print(explicit_counter)


#3 Top Three Genres
genres = 4
genres_count = {}
for row in rows:
    row[genres] = ast.literal_eval(row[genres])
    for genre in row[genres]:
        if genre in genres_count:
            genres_count[genre] += 1
        else:
            genres_count[genre] = 1
print(genres_count)
top_3 = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:3]
print(top_3)


#here starts work to check


#Average Liveliness with Energy Criteria:
energy_index = columns.index('energy')
liveliness_index = columns.index('liveness')
liveliness_sum = 0
counter = 0
for row in rows:
    if float(row[energy_index]) > 0.5:
        liveliness_sum += float(row[liveliness_index])
        counter += 1
liveliness_average = liveliness_sum/counter
print(liveliness_average)


#The most popular artist
artist_index = columns.index('artist_name')
popularity_counter = {}
for row in rows:
    if row[artist_index] in popularity_counter:
        popularity_counter[row[artist_index]] += 1
    else:
        popularity_counter[row[artist_index]] = 1
print(popularity_counter)
top_1 = sorted(popularity_counter.items(), key=lambda x: x[1], reverse=True)[:1]
print(top_1)


#The most popular year
year_index = columns.index('album_release_date')
years_counter = {}
for row in rows:
    year = row[year_index].split('-')[0]
    if year in years_counter:
        years_counter[year] += 1
    else:
        years_counter[year] = 1
print(years_counter)
top_year = sorted(years_counter.items(), key=lambda x: x[1], reverse=True)[:1]
print(top_year)
