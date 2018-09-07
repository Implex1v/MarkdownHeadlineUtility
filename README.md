# Table of Contents<br>
&nbsp;1 MarkdownHeadlineUtility
<br>&nbsp;&nbsp;1.1 Requirements
<br>&nbsp;&nbsp;1.2 Usage
<br>&nbsp;&nbsp;&nbsp;1.2.1 Help
<br>&nbsp;&nbsp;&nbsp;1.2.2 ToC only
<br>&nbsp;&nbsp;&nbsp;&nbsp;1.2.2.1 Console output
<br>&nbsp;&nbsp;&nbsp;&nbsp;1.2.2.2 Output in file
<br>&nbsp;&nbsp;&nbsp;1.2.3 Numbering
<br>&nbsp;&nbsp;&nbsp;&nbsp;1.2.3.1 Without output
<br>&nbsp;&nbsp;&nbsp;&nbsp;1.2.3.2 With output
<br>
# 1 MarkdownHeadlineUtility
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

## 1.1 Requirements
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
## 1.2 Usage
### 1.2.1 Help
To print the help just run:
```
./mdheadline.py -h
```

### 1.2.2 Table of Contents
#### 1.2.2.1 Console output
To get the Table of Contents from a Markdown file run the following command.
```
./mdheadline.py -toc <inputfile>
```
This will print the table of content to the console.
#### 1.2.2.2 Output in file
To add the ToC to your Markdown you have to run the following command.
```
./mdheadline.py -toc -o <outputfile> <inputfile>
```

### 1.2.3 Numbering
#### 1.2.3.1 Without output
If you want to add a numbering you can run the script with the `-n` option.
```
./mdheadline.py -toc -n <inputfile>
```
#### 1.2.3.2 With output
If you chose to use the `-o` option the output file will contain the numbering.
```
./mdheadline.py -toc -n -o <outputfile> <inputfile>
```