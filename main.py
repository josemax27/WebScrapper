#Web Scrapper

'''
Single web Scrapper for a single Website
This is just for study purposes
Here is the Core code
'''

#Importing Modules
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv('D:\\UPM\\First Semester\\Machine Learning\\data.csv')

#Observing Columns
print(cars.columns)

import wordcloud as WordCloud
import matplotlib.pyplot as plt

allwords = ' '.join([rl for rl in cars['Name']])
wordcloud = WordCloud(width=1200, height=600, random_state=2, max_font_size=120, background_color='purple').generate(allwords)
plt.figure(figsize=(12,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.show()