#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  f = open(filename, 'r')
  # year = re.search(r'(Popularity) in (\d\d\d\d)', f.read())
  year2 = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', f.read())
  # Rank = re.search(r'<td>(\d)</td><td>(\w)</td><td>(\w)', f.read())
  Rank = re.search(r'<tr align="right"><td>12</td><td>John</td><td>Emily</td>', f.read())
  # if year:
    # print year.group(2)
  if year2:
    for tuple in year2:
      # print tuple[0], tuple[1], tuple[2]
      dict1 = {}
      dict2 = {}	  
      dict3 = {}
      dict1[tuple[1]] = tuple[0]
      dict2[tuple[2]] = tuple[0]
      for key in sorted(dict1, key = len): 
        print key, dict1[key]
  Rank
  if Rank:
    print 'test'
    print Rank.group()
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    extract_names(args[1])
    del args[0]
    
    
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
