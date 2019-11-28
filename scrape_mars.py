import numpy as np
import pandas as pd
import datetime as dt
from flask import Flask, jsonify
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
# Mars News
    browser = init_browser()
    mars_news_url = "https://mars.nasa.gov/news"
    mars_news_html = requests.get(mars_news_url)
    mars_soup = bs(mars_news_html.text, 'html.parser')
    response = requests.get(mars_news_url)
    soup = bs(response.text, 'lxml')
    titles = soup.find_all('div', class_='content_title')
    latest_title = titles[0]
    latest_title = latest_title.find('a')
    latest_title = latest_title.text
    teasers = soup.find_all('div', class_='rollover_description')
    latest_teaser = teasers[0]
    latest_teaser = latest_teaser.find('div')
    latest_teaser = latest_teaser.text
# JPL Space images
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image_mars_html = image_mars_browser.html
    jpl_soup = BeautifulSoup(image_mars_html, 'html.parser')
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
# Mars Weather
    twitter_browser = Browser('chrome', headless=False)
    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    twitter_browser.visit(twitter_url)
    twitter_html = twitter_browser.html
    twitter_soup = bs(twitter_html, 'html.parser')
    mars_weather_tweets = twitter_soup.find_all('p', class_='TweetTextSize')
    weather_text = 'InSight'
    for tweet in mars_weather_tweets:
        if weather_text in tweet.text:
            mars_weather = tweet.text
# Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    mars_facts_table = pd.read_html(mars_facts_url)
    mars_facts = mars_facts_table[0]
    mars_facts_df = mars_facts.transpose()
    new_header = mars_facts_df.iloc[0]
    mars_facts_df = mars_facts_df[1:]
    mars_facts_df.columns = new_header
    mars_facts_html_table = mars_facts_df.to_html()
    
    time.sleep(1)

    # Store data in a dictionary
    mars_data = {
        'title': latest_title
        'teaser': latest_teaser
        'jpl image': featured_image_url
        'mars tweets': mars_weather
        'mars facts': mars_facts_html_table
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

if __name__ == "__main__":
    app.run(debug=True)