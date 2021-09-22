# Legal500 Scraper

Legal500 Scraper is a python script for extracting and storing information about law firms listed on the Legal 500 website.

## Requirements

* Python 3.6+
* Works on Linux, Windows, macOS

## Installation

Run the following command to clone the project
```bash
git clone https://github.com/jonnygovish/legal500scrape.git

cd legal500scrape
```

Create a virtual environment to work in.

```bash
python3 -m venv venv
```
Activate the virtual environment
```bash
source venv/bin/activate
```
Install scrapy and other dependecies
```bash
pip3 install scrapy pillow requests bs4
```

## Usage

To run the project

```python
scrapy crawl firms_info -O firm.csv
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
