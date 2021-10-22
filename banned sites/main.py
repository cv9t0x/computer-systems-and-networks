import socket
from urllib.parse import urlparse


def collectData(url):
    urls = []
    domains = []
    ips = []

    with open(url, encoding='utf-8') as file:
        while True:
            string = file.readline()[:-1]

            if(string == '' or string == ' '):
                break

            dataList = list(string.split(';'))[1:]

            if (',' in dataList[0]):
                urls.append(list(dataList[0].split(',')))
            elif (dataList[0] != ''):
                urls.append(dataList[0])

            if (',' in dataList[1]):
                domains.append(list(dataList[1].split(',')))
            elif (dataList[1] != ''):
                domains.append(dataList[1])

            if (',' in dataList[2]):
                ips.append(list(dataList[2].split(',')))
            elif (dataList[2] != ''):
                ips.append(dataList[2])

    return [urls, domains, ips]


def isBanned(url, domain, ip, fileUrl):
    [bannedUrls, bannedDomains, bannedIps] = collectData(fileUrl)
    result = {'url': False, 'domain': False, 'ip': False}

    if (url in bannedUrls):
        result['url'] = True
    if (domain in bannedDomains):
        result['domain'] = True
    if(ip != ''):
        if (ip in bannedIps):
            result['ip'] = True
    else:
        result['ip'] = None

    return result


def userInput():
    print('--------')
    return input('Enter url: ').strip()


def main():
    fileUrl = 'register.txt'
    url = userInput()
    domain = urlparse(url).netloc
    ip = ''
    try:
        ip = socket.gethostbyname(domain)
    except Exception:
        ip = ''

    print('--------')

    result = isBanned(url, domain, ip, fileUrl)

    for key in result:
        print("")
        if(key == 'url'):
            print(url, 'is banned:', result[key])
        if(key == 'domain'):
            print(domain, 'is banned:', result[key])
        if(key == 'ip'):
            if(result[key] == None):
                print('IP is not found')
            else:
                print(ip, 'is banned:', result[key])

    print("")
    print('--------')


if __name__ == '__main__':
    main()
