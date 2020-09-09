#!/usr/bin/env python3

import re, yaml
from typing import Dict

shortcuts = dict(
    User_Interface = {
        'cmd+\\'   : 'Zen Mode',
        'cmd+left'   : 'Toggle Sidebar',
        'cmd+right'  : 'Toggle Panel Right',
        'cmd+down'   : 'Toggle Panel Down',

        'ctrl+cmd+rightleft'   : 'Resize Terminal Panel',



        'alt+tab':   'Select Window',
        'ctrl+`':    'Switch Window',
        'ctrl+tab':  'Select Editor',

        'alt+cmd+p': 'Panel: Problems',
        'alt+cmd+t': 'Panel: Terminal',
        'alt+cmd+s': 'Panel: Search',
        'alt+cmd+o': 'Panel: Outputs',
    },

    Editor = {
        'ctrl+cmd+rightleft': 'Move File to Editor',
        'alt+cmd+left'  : 'Switch to File',
        'cmd+b'         : 'Split Editor',
    },

    Add_Cursor = {
        'alt+cmd+updown'    : 'up or down',
        'alt+cmd+l'         : 'to search results',
        'alt+cmd+e'         : 'to line ends',
    },

    Refactoring_Code={
        'shift+alt+d': 'Peek Definition',
        'shift+alt+r': 'Refactor',
        'ctrl+alt+s': 'Rename symbol',
        'shift+enter': 'Refactor Preview',
        'cmd+.': 'Fix problem',
    },

    Search={
        'cmd+f' : 'Search in document',
        'shift+cmd+f' : 'Search in workspace',
        'ctrl+cmd+updown' : 'Find Occur. Up/Down',
        'ctrl+g': 'Go To Line/Column',
    },

    Editing_Content={
        'alt+cmd+s':       'Save All',
        'alt+updown':        'Move Select. Up/Down',
        'shift+alt+updown':  'Copy Select. Up/Down',

        'cmd+/' : 'Toggle comment',
        'cmd+[' : 'Dedent lines',
        'cmd+]' : 'Outdent lines',

        'ctrl+alt+updown'       : 'Page Up/Down',
        'shift+ctrl+alt+updown' : 'Select Page Up/Down',
        'shift+ctrl+updown'     : 'Smart Selection',

        'alt+m'             : 'Markdown: Preview',
        'cmd+r'             : 'Run Code',
    },
)


def wrap(string):
    ret = ""
    for n in string.split("+"):

        if len(n) == 1:
            ret += f"<kbd>{n.upper()}</kbd>"
            continue

        n = n.replace("cmd", "<kbd>⌘</kbd>")
        n = n.replace("alt", "<kbd>⌥</kbd>")
        n = n.replace("shift", "<kbd>Shift</kbd>")
        n = n.replace("ctrl", "<kbd>Ctrl</kbd>")
        n = n.replace("tab", "<kbd>Tab</kbd>")
        n = n.replace("enter", "<kbd>↩</kbd>")

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
            pattern = re.compile(r"<!-- (_"+key.lower()+r") -->(.*?)<!-- (/\1) -->")
            data = pattern.sub(f"<!-- {key.lower()} --> {toTable(key, shortcuts[key])}<!-- /{key.lower()} -->", data)

        f.write(data)

if __name__ == "__main__":
    main('index.html', yaml.safe_load(open('layout.yaml')))

