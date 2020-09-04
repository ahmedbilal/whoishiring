# whoishiring

A simple command-line program to filter hackernews whoishiring post's comments.

## Installation
```bash
git clone https://github.com/ahmedbilal/whoishiring.git
cd whoishiring
pip install .
```

## Usage

```bash
usage: whoishiring [-h] --url URL [--output OUTPUT] --keyword KEYWORD [KEYWORD ...]

optional arguments:
  -h, --help            show this help message and exit
  --url URL             URL of whoishiring post. For example, URL of Who is Hiring? (September 2020) is https://news.ycombinator.com/item?id=24342498
  --output OUTPUT       Output file path. Default is hackernews.html
  --keyword KEYWORD [KEYWORD ...]
                        Example --keyword remote python
```

### Find remote python jobs
```bash
whoishiring --url "https://news.ycombinator.com/item?id=24342498" --keyword remote python
```