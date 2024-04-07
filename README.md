### Set up project
- Run `poetry install`. This will create a virtual environment and install packages from `pyproject.toml`.
- You can find the virtual environment by `poetry env list`.
- If you are using VSCode, set the python interpretor to the virtual environment that poetry just created.

### Run crawler
- `cd crawler`
- `scrapy crawl westelm`
- check `westelm2.jsonl` for crawled content. The structure is {product: xxx, data-src: [url1, url2]}
