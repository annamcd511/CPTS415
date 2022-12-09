import pandas as pd 
import plotly.express as px
import geopandas as gpd
import matplotlib.pyplot as plt

'''
RETRIEVING THE BIRD THAT WAS CHOSEN
'''
with open('chosen_bird.txt','r') as f:
    choice = f.readlines()
    choice = choice[0][:-1]

'''
CONVERTING THE MAPREDUCE RESULT INTO A PANDAS DATAFRAME
'''
df = pd.read_csv(choice+".txt", names=["year","latitude","longitude","observation_count"],sep=",|\t")

#remove any extra spaces, odd text, and convert the values to floats
df["year"] = df["year"].str.strip("[").str.strip().str.replace('"','').astype(float)
df["longitude"] = df["longitude"].str.strip("]").str.strip().str.replace('"','').astype(float)
df["latitude"] = df["latitude"].str.strip().str.replace('"','').astype(float)

'''
PLOTTING OBSERVATION COUNT VS YEARS
'''
df.plot(x="year",y="observation_count")
#saving and outputting the file
file = choice+'.png'
plt.savefig(file)

'''
CONVERTING THE PANDAS TO A GEOPANDAS
'''
geo_df = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

'''
cREATES AN ANIMATED GEOSCATTER MAP THAT DISPLAY THE BIRD POPULATION YEAR BY YEAR
'''
fig = px.scatter_geo(geo_df,
                    lat=geo_df.geometry.y,
                    lon=geo_df.geometry.x,
                    animation_frame=geo_df.year,
                    size=geo_df.observation_count,
                    opacity = 0.5
        )

#updated the figure to only focus on south america and where the bird is seen
fig.update_layout(geo = dict(          
    scope="south america",
    showland = True,
        landcolor = "rgb(212, 212, 212)",
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,
        resolution = 50,
                        lonaxis = dict(
                                showgrid = True,
                                gridwidth = 0.5,
                                range= [ (df["longitude"].min()-1), (df["longitude"].max()+1)],
                                dtick = 5),
                    lataxis = dict(
                                showgrid = True,
                                gridwidth = 0.5,
                                range= [ (df["latitude"].min()-1), (df["latitude"].max()+1)],
                                dtick = 5)))
#saving the file
file = choice+'_YearbyYear.html'
fig.write_html(file, auto_open=True)

'''
CREATING A GEOSCATTER MAP THAT DISPLAYS THE BIRD POPULATION OVER ALL THE YEARS
'''
fig = px.scatter_geo(geo_df,
                    lat=geo_df.geometry.y,
                    lon=geo_df.geometry.x,
                    color=geo_df.year,
                    size=geo_df.observation_count,
                    opacity = 0.5
        )

#updated the figure to only focus on south america and where the bird is seen
fig.update_layout(geo = dict(          
    scope="south america",
    showland = True,
        landcolor = "rgb(212, 212, 212)",
        subunitcolor = "rgb(255, 255, 255)",
        countrycolor = "rgb(255, 255, 255)",
        showlakes = True,
        lakecolor = "rgb(255, 255, 255)",
        showsubunits = True,
        showcountries = True,
        resolution = 50,
                        lonaxis = dict(
                                showgrid = True,
                                gridwidth = 0.5,
                                range= [ (df["longitude"].min()-1), (df["longitude"].max()+1)],
                                dtick = 5),
                    lataxis = dict(
                                showgrid = True,
                                gridwidth = 0.5,
                                range= [ (df["latitude"].min()-1), (df["latitude"].max()+1)],
                                dtick = 5)))

#saving the file
file = choice+'_allYears.html'
fig.write_html(file, auto_open=True)

