#!/usr/bin/env python
import requests
import sys


def checkResponse(response, url):
    if response.status_code == '200':
        print '[' + response.status_code + '] ' + url + ' Found!'
    else:
        print '[' + response.status_code + '] ' + url + 'Miss..'


def main():
    """

    main
    """
    if len(sys.argv) < 2:
        sys.exit('Need more params.')

    try:
        urlFile = open(sys.argv[1], 'r')
        for line in urlFile:
            ext = line.strip().split('.')[-1]

            if ext == 'asp':
                url = line.strip().replace('.asp','.aspx')
                print url
                response = requests.get(url)
                checkResponse(response, url)

            elif ext == 'aspx':
                url = line.strip().replace('.aspx', '.asp')
                print url
                response = requests.get(url)
                checkResponse(response, url)

    except IOError:
        sys.exit('Can\'t open file:' + sys.argv[1])

    except requests.Timeout:
        print 'Connection timed out. - ' + url


if __name__ == '__main__':
    main()
