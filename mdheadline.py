#!/usr/bin/python
from argparse import ArgumentParser


class Headline:
    title = ""
    depth = 0
    number = 1
    numberString = ""
    parent = None
    linenumber = 1

    def __init__(self, title, depth):
        self.depth = depth
        self.title = title

    def __str__(self):
        return "Headline: title: " + self.title.rstrip() + " depth: " + str(self.depth) + " number: " + str(
            self.number) + " numberString:" \
               + self.numberString + " linenumber: " + str(self.linenumber) + " numbering: " + self.getnumbering()

    def original(self) -> str:
        hashes = "#" * self.depth
        return hashes + " " + self.title

    def gettocline(self, numbering: bool) -> str:
        tocline = ("&nbsp;" * self.depth)
        if numbering:
            tocline += self.getnumbering() + " "
        if self.title:
            tocline += self.title + "<br>"
        else:
            tocline += "<br>\n"
        return tocline

    def getheadline(self, numbering: bool) -> str:
        tocline = ("#" * self.depth) + " "
        if numbering:
            tocline += self.getnumbering() + " "
        if self.title:
            tocline += self.title
        else:
            tocline += "\n"
        return tocline

    def getnumbering(self):
        if len(self.numberString) > 0:
            return self.numberString + "." + str(self.number)
        else:
            return str(self.number)


def count_starting_hashes(string):
    depth = 0
    for char in string:
        if char == "#":
            depth += 1
        else:
            return depth


parser = ArgumentParser()
parser.add_argument("-toc", "--tableofcontent", help="Create table of content", action='store_true')
parser.add_argument("-n", "--numbering", help="Add numbering to headline", action='store_true')
parser.add_argument("-o", "--output", help="The file the updated Markdown will be saved to", dest="output")
parser.add_argument("file", help="The file to edit")
args = parser.parse_args()

content = {}
headlines = []
i = -1
fd = open(args.file, "r+")
inblockcomment = False
for line in fd:
    i += 1
    content[i] = line

    if line.startswith("```"):
        inblockcomment = not inblockcomment
        continue

    if not line.startswith("#"):
        continue

    if inblockcomment:
        continue

    depth = count_starting_hashes(line)
    title = line[depth + 1:]

    # skip headline wich start with a number, cause might be already numbered
    if title[0].isnumeric():
        continue

    headline = Headline(title, depth)
    headline.linenumber = i

    if args.numbering and len(headlines) > 0:
        last = headlines[-1]

        if last.depth == headline.depth:
            headline.parent = last.parent
            headline.numberString = last.numberString
            headline.number = last.number + 1
        elif last.depth < headline.depth:
            headline.parent = last
            headline.numberString = last.getnumbering()
        else:
            tmp = last.parent
            while tmp is not None:
                if tmp.depth == headline.depth:
                    headline.numberString = tmp.numberString
                    headline.parent = tmp.parent
                    break
                tmp = tmp.parent

            headline.number = last.parent.number + 1
            headline.parent = last.parent

    headlines.append(headline)
fd.close()

toc = []
if args.tableofcontent:
    toc.append("# Table of Contents<br>\n")
    for headline in headlines:
        tocline = headline.gettocline(args.numbering)
        toc.append(tocline)
        if args.output is None:
            print(tocline.replace("<br>", "").rstrip() + "<br>")

if args.output:
    file = open(args.output, "w")
    if args.numbering:
        for headline in headlines:
            content[headline.linenumber] = headline.getheadline(True)

    if args.tableofcontent:
        file.writelines(toc)
        file.write("\n")
    file.writelines(content.values())
    file.close()
