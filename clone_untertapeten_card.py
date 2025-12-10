#!/usr/bin/env python3
import sys
from pathlib import Path
from copy import copy

from bs4 import BeautifulSoup

SEARCH_TEXT = "Untertapeten"
TARGET_HEADER_TEXT = "Raumausstatter"


def find_untertapeten_col(soup: BeautifulSoup):
    """
    1. Find <p class="card-text"> containing 'Untertapeten'
    2. Walk up to the surrounding <div class="col-sm-6 ..."> card column
    """
    # First try direct string match
    p = soup.find("p", class_="card-text", string=lambda t: t and SEARCH_TEXT in t)

    # If not found, allow Untertapeten in descendants (like <small>)
    if not p:
        for cand in soup.find_all("p", class_="card-text"):
            if SEARCH_TEXT in cand.get_text():
                p = cand
                break

    if not p:
        raise RuntimeError(f'No <p class="card-text"> containing "{SEARCH_TEXT}" found')

    # Walk up the parents until we hit a div with class "col-sm-6"
    parent = p
    while parent and not (
        parent.name == "div"
        and parent.has_attr("class")
        and "col-sm-6" in parent["class"]
    ):
        parent = parent.parent

    if not parent:
        raise RuntimeError(
            'Could not find a parent <div> with class "col-sm-6" for the Untertapeten paragraph'
        )

    return parent


def find_raumausstatter_row(soup: BeautifulSoup):
    """
    1. Find <div class="card-header"> whose text contains 'Raumausstatter'
    2. Go to its parent <div class="card">
    3. Inside that card, find the <div class="row"> that holds the col-sm-6 items
    """
    header = soup.find(
        "div",
        class_="card-header",
        string=lambda t: t and TARGET_HEADER_TEXT in t,
    )

    if not header:
        raise RuntimeError(
            f'No <div class="card-header"> containing "{TARGET_HEADER_TEXT}" found'
        )

    # Parent card
    card = header.find_parent("div", class_="card")
    if not card:
        raise RuntimeError(
            'Could not find a parent <div class="card"> for the Raumausstatter header'
        )

    # Row inside that card
    row = card.find("div", class_="row")
    if not row:
        raise RuntimeError(
            'Could not find a <div class="row"> inside the Raumausstatter card'
        )

    return row


def main(path: Path):
    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    # 1. Find the Untertapeten column div (col-sm-6 ...)
    untertapeten_col = find_untertapeten_col(soup)

    # 2. Clone it
    clone = copy(untertapeten_col)

    # 3. Find the Raumausstatter row (the one that contains col-sm-6 cards)
    target_row = find_raumausstatter_row(soup)

    # 4. Append the cloned column into that row, as a sibling of the other col-sm-6 divs
    target_row.append("\n")
    target_row.append(clone)
    target_row.append("\n")

    # 5. Backup original and write modified HTML
    backup = path.with_suffix(path.suffix + ".bak")
    backup.write_text(html, encoding="utf-8")  # original backup

    path.write_text(str(soup), encoding="utf-8")
    print(f"Done. Original saved as {backup}, modified written to {path}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} index.html", file=sys.stderr)
        sys.exit(1)

    main(Path(sys.argv[1]))

