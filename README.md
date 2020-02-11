# Web Scraping Challenge

In this challenge, the goal was to scrape data from NASA's twitter account for the latest updates, pictures, and other information on the exploration of Mars. After scraping the data with Beautiful Soup, Requests, and Splinter, I was tasked with pushing the data onto a personal HTML webpage that I created. 

## Getting Started 

I am running this code out of my anaconda virtual environment and Jupyter Notebook. In order to run this code you will need the proper dependencies installed and "Chromedriver.exe" must be in the same folder. 

### Analysis and Coding 

I started my webscrape by grabbing each title, description, and teaser on the NASA news URL. I wanted to scrape each headline, and a summary of that headline, to give viewers an idea of what the latest public news on the exploration of Mars looks like: 

```
response = requests.get(mars_news_url)
soup = bs(response.text, 'lxml')
titles = soup.find_all('div', class_='content_title')
```

I repeated the process for scraping the "featured image" of the day. After that was completed, I wrote a for loop to grab various tweets about the weather on Mars: 

```
for tweet in mars_weather_tweets:
    if weather_text in tweet.text:
        mars_weather = tweet.text
        print(tweet.text)
```

These web scrapes were written with beautiful soup in order to grab specific html elements in the page. After this data was scraped, I brought pandas into the mix to scrape the tables of the Mars facts NASA page. The process continued in grabbing the Mars hemisphere data, which I again utilized beautiful soup and a for loop to iterate through all the html elements I wanted to pull into my personal webpage:

```
usgs_browser = Browser('chrome', headless=False)
usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
usgs_browser.visit(usgs_url)
browser.visit(usgs_url)
html = browser.html
soup = BeautifulSoup(html, "html.parser")
mars_hemisphere = []

products = soup.find("div", class_ = "result-list" )
hemispheres = products.find_all("div", class_="item")

for hemisphere in hemispheres:
    title = hemisphere.find("h3").text
    title = title.replace("Enhanced", "")
    end_link = hemisphere.find("a")["href"]
    image_link = "https://astrogeology.usgs.gov/" + end_link    
    browser.visit(image_link)
    html = browser.html
    soup=BeautifulSoup(html, "html.parser")
    downloads = soup.find("div", class_="downloads")
    image_url = downloads.find("a")["href"]
    mars_hemisphere.append({"title": title, "img_url": image_url})
```

### Challenges or Additional Opportunities

time delays for splinter 

### Built With

* Python
* Pandas
* Splinter
* Requests
* Pymongo
* BeautifulSoup
* HTML/CSS
* Javascript
* Flask


### Authors

* **Dallas Gollogly** - [dgollogly13](https://github.com/dgollogly13)

### Acknowledgments

* Denver University Data Analytics Bootcamp 
