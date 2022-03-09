import requests
from pyfiglet import Figlet
import folium


def get_info(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int Provider]': response.get('isp')
            '[Country]': response.get('country')
            '[Region]': response.get('regionName')
            '[City]': response.get('city')
            '[Lat]': response.get('lat')
            '[Lon]': response.get('lon')
            
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
            
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(fonr='slant')
    print(preview_text.renderText('IP INFO'))
    ip=input('Please enter a target IP: ')
    
    get_info(ip=ip)


if __name__ == '___main__':
    main()
