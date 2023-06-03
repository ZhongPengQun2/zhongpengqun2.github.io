doc_postfixs = ['md', 'txt']

docs_path = "/Users/vzhong/Documents/ZhongPengQun2.github.io/docs"


search_input = "Yes, but still"

import re
import glob
import time

all_docs = []
current_clipboard_content = ""

def read_from_clipboard():
    import subprocess
    return subprocess.check_output(
        'pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')

def show_matched():
    for doc_postfix in doc_postfixs:
        for doc in glob.glob("{}/*.{}".format(docs_path, doc_postfix)):
            with open(doc, "r") as f:
                all_docs.append('\n'.join(f.readlines()))

    all_docs_text = "\n\n".join(all_docs)
    return all_docs_text

all_docs_text = show_matched()

if __name__ == "__main__":
    while 1:
        clipboard_text = read_from_clipboard()

        # Escape keywords of re, ?=
        clipboard_text = clipboard_text.replace('?', '\?')

        if clipboard_text != current_clipboard_content:
            matcheds = re.findall('.{100}' + clipboard_text + '.{100}', all_docs_text, re.DOTALL)
            for matched in matcheds:
                print('-----------------%s'%clipboard_text)
                print(matched)

            time.sleep(1)
            current_clipboard_content = clipboard_text