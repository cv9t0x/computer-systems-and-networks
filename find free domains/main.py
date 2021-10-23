import requests
from urllib.parse import urlparse
import json


def fetchBannedSites(API):
    try:
        response = requests.get(API)
        return response.json()
    except Exception:
        return None


def getBannedDomains(response):
    bannedDomains = []

    if(response):
        for key in response:
            for site in response[key]:
                if ('https://' in site['link']):
                    domain = urlparse(site['link']).netloc
                    bannedDomains.append(domain)

    return bannedDomains


def isAvailableDomain(domain, API):
    try:
        response = requests.get(API + domain)
        return response.json()['available']
    except Exception:
        return "Error"


def main():
    API_BANNED_SITES = 'https://reestr.rublacklist.net/api/v2/current/json/'
    API_AVAILABLE_DOMAINS = 'http://api.whois.vu/?q='

    bannedDomains = getBannedDomains(fetchBannedSites(API_BANNED_SITES))

    if(len(bannedDomains) > 0):
        for domain in bannedDomains:
            available = isAvailableDomain(
                domain, API_AVAILABLE_DOMAINS)

            if (available == 'undefined'):
                print(domain, 'is undefined')
            elif (available == 'incorrect'):
                print(domain, 'is incorrect')
            elif (available == 'Error'):
                print('Fetch error')
            else:
                print(domain, 'is available:', available)
    else:
        print('Fetch error')


if __name__ == '__main__':
    main()
