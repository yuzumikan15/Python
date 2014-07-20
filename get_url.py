from HTMLParser import HTMLParser
import urllib2
from urlparse import urlparse

class ExtractTextLinkParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.url = ""
        self.text = ""

    def handle_starttag(self, tag, attrs): 
        if tag == "a":          
            attrs = dict(attrs) 
            if "href" in attrs:
                self.url = attrs["href"]

    def handle_endtag(self, tag): 
        if tag == "a":
            if self.text:         
                self.links.append((self.url, self.text))
            self.url = self.text = ""
    
    def handle_data(self, data): 
        if self.url:             
            self.text += data    

def get_links(url):
    response = urllib2.urlopen(url)
    parser = ExtractTextLinkParser()
    encoding = response.headers.getparam('charset')
    page = response.read().decode(encoding)
    parser.feed(page)    
    parser.close()
    links = parser.links
    return [l for l in links 
            if l[0].find("://") != -1 and not l[0].startswith(url)]

def main():
	links = get_links('http://twitter.com')
	links = [l for l in links if urlparse(l[0])[0]][3:]
	for url, title in links[:10]:
		print "%s" % url
	#	print "[%s:title=%s]" % (url, title.decode("utf-8", "replace"))

if __name__ == '__main__':
	main()
