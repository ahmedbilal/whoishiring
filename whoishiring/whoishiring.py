import argparse
import re
import webbrowser
from urllib.parse import urljoin

import bs4
import requests


def extract_comment(element):
    if isinstance(element, bs4.element.Tag):
        # if the comment have img with 0 width, it means that the comment
        # is actual comment not replies
        if element.find("img", width="0"):
            comment_span = element.find("span", class_="commtext")
            if comment_span:
                return comment_span.prettify()
    return None


def write_html(comments, output_file_path):
    html_body = ["<html><head><title>Hackernews Filtered Job Posts</title></head><body>"]
    html_body += map(lambda comment: comment + "<hr>", comments)
    html_body += ["</body></html>"]

    with open(output_file_path, "w") as f:
        f.writelines(html_body)


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "--url", required=True,
        help="URL of whoishiring post. For example, URL of Who is Hiring? (September 2020) is "
             "https://news.ycombinator.com/item?id=24342498",
    )
    argparser.add_argument("--output", default="hackernews.html", help="Output file path. Default is hackernews.html")
    argparser.add_argument("--keyword", nargs="+", required=True, help="Keyword examples: remote python")

    args = argparser.parse_args()
    url, output_file_path, keywords = args.url, args.output, args.keyword

    filters = [re.compile(keyword, re.IGNORECASE) for keyword in keywords]
    filtered_comments = []
    while url:
        request = requests.get(url)
        soup = bs4.BeautifulSoup(request.content, "html.parser")
        comments_in_html = list(soup.find(name="table", class_="comment-tree").children)
        comments = filter(
            lambda x: x is not None,
            [extract_comment(comment) for comment in comments_in_html]
        )
        filtered_comments += [
            comment for comment in comments
            if all([_filter.search(comment) for _filter in filters])
        ]

        more_link = soup.find(name="a", class_="morelink")
        url = urljoin("https://news.ycombinator.com/", more_link.get("href")) if more_link else None

    write_html(filtered_comments, output_file_path)
    webbrowser.open_new_tab(output_file_path)
