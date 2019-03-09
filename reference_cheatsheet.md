## Reference Sheet for Requests/Beautiful Soup Libraries
_Note: The below examples use Python 3._
### Requests
[Requests](http://docs.python-requests.org/en/master/) is the standard Python library for making HTTP requests. Need to fetch the HTML content from a webpage, or post to a form and get the response? Requests will handle that. Here's a handy reference for the package.

#### Import `requests` package to use in a script 
```
import requests
```
#### Make a GET request to retrieve the contents of a webpage
This returns a requests object, which 
```
r = requests.get('https://www.dogsdogsdogs.com')
```
#### Get the text of the page returned by the GET request
```
r.text # <html>...</html>
```
#### Find the status of the response
200 means the server was able to return the contents of the webpage you requested without error.

There are lots of different error codes, but 404 is the most common one.
```
r.status_code # 200
```
#### Raise an error if the request has returned a 404, 500 or other HTTP error
```
r.raise_for_status()
```
#### Make a GET request with url parameters
```
payload = {
    'type':'cute',
    'age':'puppy'
}
r = requests.get('https://www.dogsdogsdogs.com', params=payload)
# retrieves: https://www.dogsdogsdogs.com?type=cute&age=puppy
```
#### Make a POST request 
A POST request generally means you're sending some specific information to be processed by the server, rather than asking for the content of a url.

You'll see POST requests most often in cases where you're submitting information of some kind, like a form. The request might return the same url you're posting to, just like a GET request, but it also might return a dictionary of data, a redirect to a new page or something else entirely.
```
data = {
    'type':'cute',
    'age':'puppy'
}
r = requests.post('https://www.dogsdogsdogs.com', data=data)
```

### Make a request with headers
The most polite way to scrape is to specify a custom user agent to identify yourself. But some sites put in security that blocks requests with non-standard user agents, so you may want to use the user agent of a common browser instead. To find your browser's user agent, you can examine the headers in the dev tools network requests pane or Google "my user agent"
```
headers = {
    'User-Agent': 'MyScraper 1.0'
}
requests.get('https://www.dogsdogsdogs.com', headers=headers)
```

### Beautiful Soup
Fetched your HTML with Requests? Great. [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) is a library that will help you navigate through that HTML file to get to the parts you're looking for. Here are some ways you can use it.

#### Import Beautiful Soup to use in a script
```
from bs4 import Beautiful Soup
```

#### Create a soup object
```
# if you've got a requests object, use r.text.
soup = BeautifulSoup(r.text, 'html.parser')

# if you're pulling in from a file, open the file first
soup = BeautifulSoup(open('index.html'), 'html.parser')

# if you've got the html as a string, maybe saved as a variable, pass it in as is.
soup = BeautifulSoup(HTML_STRING, 'html.parser')
```

#### Find a tag on the page
```
soup.find('p') # <p>I am a <a href="https://www.dogsdogsdogs.com">dog</a></p>
```

#### Find all tags on the page
```
soup.find_all('p') # [<p>I am a dog</p>,<p>I am a unicorn</p>]
```

#### Find a tag with a specific attribute
```
soup.find('p', {'class','sloth'}) # <p class='sloth'>I am a sloth</p>
```
#### Get the text of a tag
```
soup.find('p').string # I am a dog.
```

#### Get the value of a tag's attribute

If you're looking for a link, it probably has an `href` attribute, so just select it like you would any key/value pair
```
soup.find('a')['href'] # https://www.dogsdogsdogs.com/
```
Instead, you may want to use .get(), which will return None rather than an error if the attribute does not exist
```
soup.find('p).get('class') # None
```

#### Find the next tag after a certain element
```
sloth = soup.find('p', {'class','sloth'})
soup.find_next('p') # <p>I am a platypus</p>
```