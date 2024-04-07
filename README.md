### Set up project
- Run `poetry install`. This will create a virtual environment and install packages from `pyproject.toml`.
- You can find the virtual environment by `poetry env list`.
- If you are using VSCode, set the python interpretor to the virtual environment that poetry just created.

### Run crawler
- `cd crawler`
- `scrapy crawl westelm`
- check `westelm2.jsonl` for crawled content. The structure is {product: xxx, data-src: [url1, url2]}

### MVP
Workflow: clients parse URLs of furnitures in the website, the website will crawler products into "catalog". Then client can drag and drop product from catalog to the sketched floorplan (or layer).

MVP floorplan will be just a square.

Extra win: able to sketch real floorplan from client's floorplan image

### Next step for MVP:

For the MVP, we will not use database, just use the json file for storing and loading data. The goal is to have a working pipeline without worrying about infrastructure.

1. Filter images, we don't want every image url from the same product (Backend, python)
2. How to crawl dynamic content? --> To get dimensions: one product has >1 dimension, it's passed as values in DOM (Backend, python)
3. Assume that we have floorplan and dimensions of furnitures, how to render in a website (FE, React most likely)

### After MVP:
1. Create database and infra, so that the env is replicatable in both env (Jiadai)
2. Create tables to store crawled data (Jiayun)