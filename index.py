#!/usr/bin/env python3

import re, yaml
from typing import Dict
import random


def wrap(string):
    ret = ""
    for n in string.split("+"):

        if len(n) == 1:
            ret += f"<kbd>{n.upper()}</kbd>"
            continue

        n = n.replace("cmd", "<kbd>⌘</kbd>")
        n = n.replace("alt", "<kbd>⌥</kbd>")
        n = n.replace("shift", "<kbd>⇧</kbd>")
        n = n.replace("ctrl", "<kbd>⌃</kbd>")
        n = n.replace("tab", "<kbd>Tab</kbd>")
        n = n.replace("enter", "<kbd>↩</kbd>")
        n = n.replace("space", "<kbd>␣</kbd>")

        n = n.replace("updown", "<kbd>↕</kbd>")
        n = n.replace("downup", "<kbd>↕</kbd>")
        n = n.replace("leftright", "<kbd>↔</kbd>")
        n = n.replace("rightleft", "<kbd>↔</kbd>")

        n = n.replace("right", "<kbd>→</kbd>")
        n = n.replace("up", "<kbd>↑</kbd>")
        n = n.replace("down", "<kbd>↓</kbd>")
        n = n.replace("left", "<kbd>←</kbd>")

        ret += n

    return ret


def toTable(name, data):

    ret = f"\t\t<h4>{name}</h4>\n"
    ret += f"<ol>\n"
    for k, v in data.items():
        ret += f"\t\t<li><p class=\"kbd\"><span>{wrap(k)}</span></p><p class=\"descr\">{v}</p></li>\n"

    ret += f"</ol>\n"
    return "<div class='grid-item'>" + ret + "</div>"


def main(file_name: str, shortcuts: Dict[str, str]):

    keys = [(key, val) for key, val in shortcuts.items()]

    # experiments with better (random) order
    # random.shuffle(keys)

    data = ""
    with open("template.html", "r+") as f:
        data = f.read()

    with open(file_name, "w") as f:
        f.write(
            data.replace(
                '<!--content/-->',
                "\n".join(toTable(item[0], item[1]) for item in keys),
            ))


if __name__ == "__main__":
    main('index.html', yaml.safe_load(open('keybindings.yaml')))
