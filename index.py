#!/usr/bin/env python3

import re, yaml
from typing import Dict


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

    ret = f"\t\t<li class=\"wide\"><h4>{name}</h4></li>\n"

    for k, v in data.items():
        ret += f"\t\t<li><p class=\"kbd\"><span>{wrap(k)}</span></p><p class=\"descr\">{v}</p></li>\n"

    return ret


def main(file_name: str, shortcuts: Dict[str, str]):

    data = ""
    with open("template.html", "r+") as f:
        data = f.read()

    with open(file_name, "w") as f:
        for key in shortcuts:
            pattern = re.compile(r"<!-- (_" + key.lower() +
                                 r") -->(.*?)<!-- (/\1) -->")
            data = pattern.sub(
                f"<!-- {key.lower()} --> {toTable(key, shortcuts[key])}<!-- /{key.lower()} -->",
                data)

        f.write(data)


if __name__ == "__main__":
    main('index.html', yaml.safe_load(open('layout.yaml')))
