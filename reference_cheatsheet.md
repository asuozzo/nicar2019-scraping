## Reference Sheet for Requests/Beautiful Soup Libraries
_Note: The below examples use Python 3._

### Using the command line
On a Mac, use the command line by opening the Terminal app. 
- Change directories: `cd directory-name`
- See all files in the directory you're in: `ls`
- Run a python script: `python script-name.py`
- Pass positional arguments to a python script: `python script-name.py http://127.0.0.1/`
- Send the output of a script to a file: `python script-name.py > filename.csv`
- Send the output of a script to another script: `python script-name.py | python script-name2.py`
### Parts of a standard Python script
The shebang line, at the very top of the file, tells the system that this is a script, and tells it which interpreter to use. In this case, it's just telling the system to use the default Python executable.
```
#!/usr/bin/env python
```
You may see a docstring just below the shebang line, or within a function. It's a space for the developer to provide documentation on what the script or function does.
```
"""
    This is a docstring. It usually documents how a script file or function within a file works.
"""
```
The `__name__=="__main__:"` statement is where all code in a script that's not within a function should go. When you run the script in the command line, the script within this block will execute. If you import your script into another script — say, you want to use function1 in something else you're writing — the `__name__=="__main__:"` block will not run. We're running all the scripts in this class in the command line, so that block will always run.
```
def function1(variable1):
    return variable1

if __name__ == "__main__":
    function1(variable1)
```

### Useful Python snippets

#### Handling command line arguments
You can access command line arguments using the sys library. They get passed in to your script as a list. Say you pass in a url and a directory: `python script-name.py http://127.0.0.1/ data/src`. Access the arguments like this:
```
import sys

variable1 = sys.argv[0] # http://127.0.0.1/
variable2 = sys.argv[1] # data/src
```
Note that the order is very important here. You can also set up your script to take in named arguments from the command line. That's not something we're covering in this class, but it can come in handy when you're writing more complicated scripts.
#### Using standard input and output
Standard input and output function as file-like objects.

You can handle a file passed in via standard input like a file that's already been opened; iterate through its lines or pass it to a BeautifulSoup object.
```
soup = BeautifulSoup(sys.stdin,'html.parser')
```
You can also write to standard output as you would to a file. That lets you redirect the output to a filename you specify, using the `>` syntax, when you run the script on the command line.

Be aware that if you are using standard output, any print statements you use in the debugging process will be added to your output. If you're seeing things in your file that shouldn't be there, check for print statements.
```
sys.stdout.write("Hi")
```
#### Reading and writing CSV files
Make sure to `import csv` at the top of your file.

Read a CSV
```
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) # returns a list, i.e. ["Bernie Sanders","Senator",45000]
```
Write a CSV
```
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(["Candidate", "Office", "Votes"])
    writer.writerow(["Bernie Sanders","Senator",45000])
```
Read a CSV as a dictionary
```
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row) # returns a dictionary, i.e. {"Candidate":"Bernie Sanders",
                                                 "Office":"Senator",
                                                 "Votes":45000}
        print(row["Candidate"]) # "Bernie Sanders"
```
Write a CSV as a dictionary
```
with open('data.csv', 'w') as f:
    fieldname = ["Candidate","Office","Votes"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader(["Candidate", "Office", "Votes"])
    writer.writerow({"Candidate":"Bernie Sanders","Office":"Senator","Votes":45000})
```
#### Delay a function (useful for not accidentally taking down websites!)
Every time this function runs, it will pause for two seconds before returning a value.
```
from time import sleep

def function1(variable1):
    sleep(2)
    return variable1
```

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