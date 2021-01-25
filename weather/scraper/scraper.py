from bs4 import BeautifulSoup as bs
import requests
from django.conf import settings

class Scrape:
    def __init__(self) -> None:
        self.base_url = settings.SITE_URL
    
    def get_data(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        return False
    
    def get_endpoints(self):
        data = self.get_data(self.base_url)
        if not data:return False
        soup = bs(data, 'html.parser')
        s = soup.find(class_="list-c")
        endpoints = []
        for i in s:
            if i != '\n':
                endpoints.append(i.a['href'])
        return endpoints
    
    def get_weather(self):
        endpoints = self.get_endpoints()
        if endpoints:
            all_regions = []
            for endpoint in endpoints:
                data = self.get_data(endpoint)
                if not data:return False
                soup = bs(data, 'html.parser')
                data = soup.find('div',{'class':'padd-block'})
                div = bs(str(data), 'html.parser')
                region = div.find('h2').text.strip()
                current_day = div.find('div', {'class': 'current-day'}).text.strip()      
                current_forecast = div.find('div', {'class': 'current-forecast'}).text.strip().split('\n')
                current_forecast_desc = div.find('div',{'class':'current-forecast-desc'}).text.strip()
                current_forecast_details = list(filter(lambda i: i != '', div.find('div',{'class':'current-forecast-details'}).text.strip().split('\n')))
                print(current_forecast_details)
                current_forecast_day = list(filter(lambda i: i != '', div.find('div',{'class':"current-forecast-day"}).text.strip().split('\n')))
                all_regions.append(
                    {
                        "region":region,
                        "day":current_day,
                        "forecast":f"{current_forecast[0]},{current_forecast[1]}",
                        "forecast_desc":current_forecast_desc,
                        "humidity":current_forecast_details[0].split(":")[1],
                        "wind":current_forecast_details[1].split(":")[1],
                        "pressure":current_forecast_details[2].split(":")[1],
                        "moon":current_forecast_details[3].split(":")[1],
                        "sunrise":current_forecast_details[4].split(":",1)[1],
                        "sunset":current_forecast_details[5].split(":",1)[1],
                        "morning":current_forecast_day[1],
                        "afternoon":current_forecast_day[3],
                        "evening":current_forecast_day[5],
                    }
                )
            return all_regions                

scrape = Scrape()