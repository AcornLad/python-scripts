#! python3
# downloadWhompcomic.py - Downloads every single Whomp Comic

import requests, os, bs4

url = 'https://whompcomic.com'  #starting url
os.makedirs('whompcomic', exist_ok=True)    #store comics in ./whompcomic

while not url.endswith('alligator-games'):
    #TODO: Download the page
    print('Downloading page %s....' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)
    
    #TODO: Find the URL of the comic image.
    comicElem = soup.select('#cc-comicbody img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        #comicUrl = 'https:' + comicElem[0].get('src')
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    #TODO: Save the image to ./whompcomic
    imageFile = open(os.path.join('whompcomic', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    #TODO: Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    #url = 'https://whompcomic.com' + prevLink.get('href')
    url = prevLink.get('href')
    
print('Done.')
