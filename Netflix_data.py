import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Kanishk Sharma\Downloads\Netflix project for D.A\Netflix Project For DA\netflix_titles.csv")
print(df.columns)
print(df.shape)
df.info()
print(df.describe())
df = df.dropna(subset = ['type','release_year','rating','country','duration'])
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color = ['skyblue',"orange"])
plt.title("number of moives VS TV shows on Netflix")
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("Movies VS TV shows on Netflix.png")
plt.show()
# INSIGHT:
# Movies are significantly higher than TV Shows, indicating Netflix focuses more on movie content.

rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts, labels = rating_counts.index , autopct = "%1.1f%%", startangle = 90)
plt.title("Percentage of Content Ratings")
plt.tight_layout()
plt.savefig("Content_Ratings_Pie.png")
plt.show()
# INSIGHT:
# Most content falls under a few ratings (e.g., TV-MA, TV-14), suggesting focus on mature audiences.

Movie_df = df[df["type"] == "Movie"].copy()
Movie_df['duration_int'] = Movie_df['duration'].str.replace('min','').astype(int)
plt.figure(figsize=(8,6))
plt.hist(Movie_df["duration_int"], bins = 30 ,color = 'purple', edgecolor = 'black')
plt.title('Distribution of Movie Duration')
plt.xlabel('Duration(Minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig("Movie_Duration_histogram.png")
plt.show()
# INSIGHT:
# Most movies have duration between 80–120 minutes, showing standard movie length distribution.

release_counts = df["release_year"].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color = 'red')
plt.title('Release year VS Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig("Release_year_Scatter.png")
plt.show()
# INSIGHT:
# Netflix content releases remained low before 2000,
# but increased rapidly after 2010, showing strong platform expansion.

country_counts = df['country'].value_counts().head(10) 
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color="teal")
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel("Number of Shows")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("top10_countries.png")
plt.show()
# INSIGHT:
# USA contributes the highest number of shows, followed by India and UK.

content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))
#first subplot:movies
ax[0].plot(content_by_year.index, content_by_year ['Movie'], color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')
#second subplot: TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[1].set_title( 'TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of Movies')
fig.suptitle('Comparison of Movies and TV Shows Released Over Years')
plt.tight_layout()
plt.savefig('movies_tv_shows_comparison.png')
plt.show()
# INSIGHT:
# Content production increased significantly after 2015, showing Netflix expansion phase.



