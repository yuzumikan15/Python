from HTMLParser import HTMLParser
import urllib2

def everything_between(content,begin,end):
    idx1=content.find(begin)
    idx2=content.find(end,idx1)
    return content[idx1+len(begin):idx2].strip()

def main():
    url = 'http://twitter.com'
    response = urllib2.urlopen(url)
    content = response.read()
    title = everything_between(content,'<title>','</title>')
    print(title)
    
if __name__ == '__main__':
    main()
