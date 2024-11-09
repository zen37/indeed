# Forked from
https://github.com/rbuttery/indeed_job_scraper

# Setup

1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed.
3. Set up a virtual environment (Windows/Mac, you can name it any way):
   ```bash
   python -m venv env
   env\Scripts\activate
   pip install -r requirements.txt
4. ```bash
   python3 -m venv venv-indeed 
   source venv-indeed/bin/activate

# Example Useage In Command Line Interface

```bash
# Run the scraper for Data Analyst positions, in Remote location, in the USA, sorted by date, scraping 5 pages
python main.py --keywords "Data Analyst" --location "Remote" --country USA --sort_by date --max_pages 5
```
```bash
# Run the scraper without searching for new jobs, just updating job descriptions for existing entries
python main.py --dont_search
```
```bash
# Run the scraper with a different keyword and location, only scraping 3 pages, without updating job descriptions
python main.py --keywords "Software Developer" --location "New York" --country USA --sort_by relevance --max_pages 3 --dont_update_job_descriptions
```
```bash
# Run the scraper for Canada in the city of Toronto, looking for Engineering positions, sorting by relevance
python main.py --keywords "Engineering" --location "Toronto" --country CANADA --sort_by relevance --max_pages 2
```
