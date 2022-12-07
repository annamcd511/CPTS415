import pandas as pd 
import plotly.express as px
import geopandas as gpd

birds = ["Bananaquit",
"Bicolored_Wren",
"Black_Vulture",
"Black-chested_Jay",
"Blue-gray_Tanager",
"Brown_Pelican",
"Brown-throated_Parakeet",
"Cattle_Egret",
"Cattle_Tyrant",
"Great_Kiskadee",
"House_Wren",
"Palm_Tanager",
"Roadside_Hawk",
"Ruddy_Ground_Dove",
"Smooth-billed_Ani",
"Southern_Lapwing",
"Tropical_Kingbird",
"Turkey_Vulture",
"Yellow-bellied_Elaenia",
"Yellow-headed_Caracara"]

selected_birds = ["Blue-gray_Tanager",
"Brown_Pelican",
"Brown-throated_Parakeet",
"Southern_Lapwing"]
for i in range(len(selected_birds)):
    df = pd.read_csv("birds/mapReduce/"+selected_birds[i]+".txt", names=["year","latitude","longitude","observation_count"],sep=",|\t")

    df["year"] = df["year"].str.strip("[").str.strip().str.replace('"','').astype(float)
    df["longitude"] = df["longitude"].str.strip("]").str.strip().str.replace('"','').astype(float)
    df["latitude"] = df["latitude"].str.strip().str.replace('"','').astype(float)


    #print(df.head())

    geo_df = gpd.GeoDataFrame(
        df, geometry=gpd.points_from_xy(df.longitude, df.latitude))

    fig = px.scatter_geo(geo_df,
                        lat=geo_df.geometry.y,
                        lon=geo_df.geometry.x,
                        animation_frame=geo_df.year,
                        size=geo_df.observation_count,
                        opacity = 0.5
            )


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
    fig.show()
