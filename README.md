<div align="center">
    <h1>United States Geological Survey</h1>
</div>


<div align="center">
    <h4>By: Tai Reagan</h4>
</div>

![logo](https://github.com/Taireagan/United-States-Geological-Survey/blob/main/Images/1-Logo.png)


---


## Background
This project focuses on developing a data visualization tool for the United States Geological Survey (USGS), which is tasked with providing critical scientific data on natural hazards, ecosystem health, and the impacts of climate and land-use changes. As part of their mission, USGS collects vast amounts of earthquake data from around the globe daily, but currently lacks a powerful way to display it effectively.

The goal of this project is to create a dynamic and interactive tool that visualizes earthquake data, making it easier for the public and government agencies to understand seismic activity and its implications. This visualization will help USGS educate various stakeholders and support their efforts to secure additional funding by demonstrating the importance of monitoring and responding to natural hazards.

## Resource
To create the visualization for this project data was pull from [Earthquake USGS](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) which provides earthquake data in a number of different formats, updated every 5 minutes.

### Step 1: 
Visit the page and choose which dataset to visualize

![data](https://github.com/Taireagan/United-States-Geological-Survey/blob/main/Images/3-Data.png)

### Step 2: 
After clicking on a dataset (such as "All Earthquakes from the Past 7 Days"), you will be given a JSON representation of that data. Use the URL of this JSON to pull in the data for the visualization. The following image is a sampling of earthquake data in JSON format

![earthquakedata](https://github.com/Taireagan/United-States-Geological-Survey/blob/main/Images/earthquakedata.png)

### Step 3:
The HTML code is used to set up a web page that integrates Leaflet, a JavaScript library for interactive maps, with D3.js, another library used for creating data-driven visualizations.

![htmlcode](https://github.com/Taireagan/United-States-Geological-Survey/blob/main/Images/htmlcode.png)


### Step 4:
To create the interactive Earthquake Visualization, the earthquake data in JSON format is imported and used to plot the earthquakes based on their geographic coordinates (longitude and latitude). Leveraging the Leaflet library, a map is generated with markers that represent each earthquake. The size of the markers corresponds to the earthquake's magnitude, while the color gradient reflects the earthquake's depth—darker colors indicate greater depths. Additionally, the visualization includes interactive popups that display detailed information about each earthquake when a marker is clicked. A legend is also incorporated to enhance user understanding by providing context for the color and size scales used in the map.

![usheatmap](https://github.com/Taireagan/United-States-Geological-Survey/blob/main/Images/usheatmap.png)