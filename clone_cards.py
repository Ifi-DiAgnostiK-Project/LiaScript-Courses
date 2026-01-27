#!/usr/bin/env python3
import sys
from pathlib import Path
from copy import copy

from bs4 import BeautifulSoup


def find_col_by_cardtext(soup: BeautifulSoup, search_text: str) -> object:
    """Find the surrounding <div class="col-sm-6 ..."> for a <p class="card-text">
    whose visible text contains `search_text`.

    Steps:
      1) Find <p class="card-text"> that contains `search_text` (either as direct string
         or somewhere in descendants).
      2) Walk up the parents until a <div> with class "col-sm-6" is found.
    """
    # First try direct string match
    p = soup.find("p", class_="card-text", string=lambda t: t and search_text in t)

    # If not found, allow the text to appear in descendants (e.g., <small>)
    if not p:
        for cand in soup.find_all("p", class_="card-text"):
            if search_text in cand.get_text():
                p = cand
                break

    if not p:
        raise RuntimeError(f'No <p class="card-text"> containing "{search_text}" found')

    parent = p
    while parent and not (
        parent.name == "div"
        and parent.has_attr("class")
        and "col-sm-6" in parent["class"]
    ):
        parent = parent.parent

    if not parent:
        raise RuntimeError(
            f'Could not find a parent <div> with class "col-sm-6" for the paragraph containing "{search_text}"'
        )

    return parent


def find_target_row_by_header(soup: BeautifulSoup, header_text: str) -> object:
    """Find the <div class="row"> inside the <div class="card"> identified by a header.

    Steps:
      1) Find <div class="card-header"> containing `header_text`
      2) Go to its parent <div class="card">
      3) Inside that card, find the <div class="row"> that holds the col-sm-6 items
    """
    header = soup.find(
        "div",
        class_="card-header",
        string=lambda t: t and header_text in t,
    )

    if not header:
        raise RuntimeError(f'No <div class="card-header"> containing "{header_text}" found')

    card = header.find_parent("div", class_="card")
    if not card:
        raise RuntimeError(f'Could not find a parent <div class="card"> for the header "{header_text}"')

    row = card.find("div", class_="row")
    if not row:
        raise RuntimeError(f'Could not find a <div class="row"> inside the card for header "{header_text}"')

    return row


def clone_card_column(soup: BeautifulSoup, search_text: str, target_header_text: str) -> None:
    """Clone one card column (col-sm-6 ...) identified by `search_text`
    and append it to the target group identified by `target_header_text`.
    """
    source_col = find_col_by_cardtext(soup, search_text)
    clone = copy(source_col)

    target_row = find_target_row_by_header(soup, target_header_text)

    # Append as a sibling of the other col-sm-6 divs
    target_row.append("\n")
    target_row.append(clone)
    target_row.append("\n")


def main(path: Path):
    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "lxml")

    # Add as many transfers as you like here:
    transfers = [
        # (source card-text substring, target card-header substring)
        ("Untertapeten", "Raumausstatter"),
        ("Polsterei", "Raumausstatter"),
        ("Tapetenzeichen", "Raumausstatter"),
    ]

    for source_text, target_header in transfers:
        clone_card_column(soup, source_text, target_header)

    path.write_text(str(soup), encoding="utf-8")
    print("Done.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} index.html", file=sys.stderr)
        sys.exit(1)

    main(Path(sys.argv[1]))

