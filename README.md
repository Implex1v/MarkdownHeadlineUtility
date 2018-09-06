# MarkdownHeadlineUtility
This script provides help for Markdown headlines. It can create a Table of Contents from your Markdown file and add a paragraph numbering.

Using `mdheadline.py` you can transform
```
# Paragraph #1
## Subparagraph #1
### Subsubparagraph #1
### Subsubparagraph #2
### Subsubparagraph #3
##  Subparagraph #2
### Subsubparagraph #4
# Paragraph #2
### Subparagraph #5
```
into
```
# Table of Contents<br>
&nbsp;1 Paragraph #1
<br>&nbsp;&nbsp;1.1 Subparagraph #1
<br>&nbsp;&nbsp;&nbsp;1.1.1 Subsubparagraph #1
<br>&nbsp;&nbsp;&nbsp;1.1.2 Subsubparagraph #2
<br>&nbsp;&nbsp;&nbsp;1.1.3 Subsubparagraph #3
<br>&nbsp;&nbsp;1.2  Subparagraph #2
<br>&nbsp;&nbsp;&nbsp;1.2.1 Subsubparagraph #4
<br>&nbsp;2 Paragraph #2
<br>&nbsp;&nbsp;&nbsp;2.1 Subparagraph #5<br>
# 1 Paragraph #1
## 1.1 Subparagraph #1
### 1.1.1 Subsubparagraph #1
### 1.1.2 Subsubparagraph #2
### 1.1.3 Subsubparagraph #3
## 1.2  Subparagraph #2
### 1.2.1 Subsubparagraph #4
# 2 Paragraph #2
### 2.1 Subparagraph #5
```

## Requirements
If you want to use the paragraph numbering the following headline structure IS NOT allowed:
```markdownr
#
###
####
###
###
#####
## <- this is illegal
```
If you are going back the headline hierarchy you are not allowed to use a headline you haven't used before.
## Usage
### Help
To print the help just run:
```
./mdheadline.py -h
```

### ToC only
#### Console output
To get the Table of Contents from a Markdown file run the following command.
```
./mdheadline.py -toc <inputfile>
```
This will print the table of content to the console.
#### Output in file
To add the ToC to your Markdown you have to run the following command.
```
./mdheadline.py -toc -o <output> <inputfile>
```