Here are the solutions for scraping our example website.

Make sure to follow the instructions at the root of this repo to get the Flask example site running locally on your computer. Keep it running in a separate terminal while you're running these commands.

*Note: Since this site is running locally, you can hit it with a ton of requests and it should be fine. When you're scraping an actual website, please be polite and add time delays so as not to bombard the server.*

Make sure that your `data` and `data/src` folders are empty from any previous script runs.

`cd` into the `scrapers-solutions` directory.

# Simple Table
Local url: http://localhost:5000/1

### Fetch page HTML and save to a local file
`> python fetch_html.py http://localhost:5000/1 > data/src/results.html`

### Parse the file and write the table data to a csv file
`> python parse_single_table.py data/src/results.html > data/results.csv`


# Multiple Tables
Local url: http://localhost:5000/2

### Fetch page HTML and save to a local file
`> python fetch_html.py http://localhost:5000/2 > data/src/results.html`

### Parse the file and write the data from each table to a csv
`> python parse_multiple_tables.py data/src/results.html > data/results.csv`

# Candidate Profiles
Local url: http://localhost:5000/3

### Fetch results page HTML and save to a local file
`> python fetch_html.py http://localhost:5000/3 > data/src/profiles_main.html`
### Write results page data, with a column for links to candidate profiles, to a csv
`> python parse_candidate_profiles_table.py data/src/profiles_main.html > data/results.csv`
### Reopen results csv, follow each link and download profile HTML
`> python fetch_candidate_profiles.py data/results.csv http://localhost:5000/3 data/src`
### Save the data from each candidate profile to a csv
`> python parse_candidate_profiles.py data/results.csv data/src > data/profiles.csv`
### Join the results and profile csvs
`> python join_results_candidate_profiles.py data/results.csv data/profiles.csv > data/results_with_profile.csv`

# URL Parameters
Local url: http://localhost:5000/4

### Fetch the candidate form and write all possible office/year combinations to a csv
`> python scrape_years_offices_get.py http://localhost:5000/4 > data/years_offices.csv`

### Fetch all possible combinations of office/years and iterate through pages. Download each HTML page
`> python fetch_get_results.py http://localhost:5000/4 data/years_offices.csv data/src`

### Parse all files and write them to a csv
`> python parse_single_table_multiple_files.py data/src/*.html > data/results.csv`

# Form With Post Request
Local url: http://localhost:5000/5

### Fetch the first page, then second page of candidate form with post requests and write all possible office/year combinations to a csv
`> python scrape_years_offices_post.py http://localhost:5000/5 > data/years_offices.csv`

### Fetch all possible office/year combinations with post requests. Download each HTML page
`> python fetch_post_results.py http://localhost:5000/5 data/years_offices.csv > data/results.csv`

### Parse all files and write them to a csv
`> python parse_single_table_multiple_files.py data/src/*.html > data/results.csv`
