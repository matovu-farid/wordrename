This tool helps to automate the creation of files from templates by replacing some words with others.

## Prerequisites
Python3 should bre installed for this tool. [Click here](https://www.python.org/downloads/) if not installed.
OR on linux
```
sudo apt update
sudo apt install python3-pip
pip3 --version
```


## Installation
First clone the tools repo
```
git clone https://github.com/matovu-farid/tools.git
```

```
ln -s $PWD/tools/rename/wordrename  /usr/bin   
```

## Usage
```
wordrename -[i <input>| -d <directory>] -o <output> -r <replaced>  -w <with> 

Replace words with those provided

Options:
-i, --input        Input filename
-d, --directory    Input directory
-o, --output       Output filename
-r, --replaced     Word to replace 
-w, --with         Word replacing the other word
```
## Example
```
Assuming you have a file called file.txt and you want to replace all words foo with bar. Running the command below will replace all words including uppercase, title case and pluralized words
```
```
wordrename -i file.txt -r foo -w bar
```
