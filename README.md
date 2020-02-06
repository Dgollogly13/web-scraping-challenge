# Web Scraping Challenge

In this project I was 

## Getting Started 

I am running this code out of my anaconda environment with Jupyter Notebook. For running this code on your machine, you will need the proper dependencies installed and Jupyter Notebook or an equivalent application. Also, you will need to install splinter and make sure 'chromedriver.exe' is in the same folder as your .ipynb file. 

### Analysis and Coding 

When calling the weather data I created a series of empty lists to store the jsonified data. I utilized some 'try' and 'except' statements to append the data to each empty list and avoid errors:

```
temperature = []
humidity = []
cloudiness = []
wind_speed = []
latitude = []
city_list = []
...
try:
        weather_json = weather_response.json()
        temperature.append(weather_json['main']['temp'])
...
```

After storing the jsonified data, I put all the lists into a dictionary and converted them into a dataframe for calling them in later functions. Even though I wasn't using any front-end web visualization in this assignment, I converted the dataframe into HTML for possible future visualiations:

```
weather_dict = {
    "City": city_list,
    "Temperature": temperature,
    "Humidity": humidity, 
    "Cloudiness": cloudiness,
    "Wind Speed": wind_speed, 
    "Latitude": latitude,
```

Finally, I created variables for each column in my dataframe to be called in my scatterplots. I then plotted the four variables against Latitude using the Matplotlib mapping library:

```
plt.scatter(lat_values, temp_values, c='cyan', edgecolors='black')
plt.title("City Latitude vs. Max Termperature (11/18/19)", fontsize=20)
plt.xlabel("Latitude", fontsize=18)
plt.ylabel("Max Temperature (F)", fontsize=18)
plt.ylim(-40, 100)
plt.xlim(-60, 80)
plt.grid()
plt.gcf().set_size_inches(15, 8)
plt.savefig('lat_temperature.png')
```

### Challenges or Additional Opportunities

This project presented the opportunity to create a web user interface with the HTML conversion. It would have been interesting to have the scatter plots as a front-end visualization and allow users to interact with the data. 

### Built With

* OpenWeather API
* Python
* Pandas 
* Citipy
* Matplotlib
* Numpy

### Authors

* **Dallas Gollogly** - [dgollogly13](https://github.com/dgollogly13)

### Acknowledgments

* Denver University Data Analytics Bootcamp 
