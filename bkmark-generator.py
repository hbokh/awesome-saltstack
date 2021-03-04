## 
# Create importable bookmarks file
##

###
### HTML PREP
###
# Setup start of HTML template for importable bookmarks
bookmarks_content = []
bookmarks_content.extend([
    '<!DOCTYPE NETSCAPE-Bookmark-file-1>\n',
    '<!-- This is an automatically generated file.\n',
    '    It will be read and overwritten.\n',
    '    DO NOT EDIT! -->\n',
    '<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n',
    '<TITLE>Bookmarks</TITLE>\n',
    '<H1>Bookmarks Menu</H1>\n',
    '\n',
    '<DL><p>\n',
    '    <DT><H3 ADD_DATE="" LAST_MODIFIED="">awesome-salt</H3>\n',
    '    <DL><p>\n',
])

# Templates for header/subdirs and links/bookmarks
subdir_template='        <DT><H3 ADD_DATE="" LAST_MODIFIED="">SUBDIR</H3>\n        <DL><p>\n'
link_template='            <DT><A HREF="URL" ADD_DATE="" LAST_MODIFIED="" ICON_URI="">TITLE</A>\n'
bookmark_file='awesome-saltstack-bookmarks.html'

###
### RUN THROUGH README.md
### 
with open('README.md') as rf:
   raw_readme_strings = rf.readlines()

# Use each header as a subdir of 'awesome-saltstack' bookmark directory
subdirs = {}
index = 0
for line in raw_readme_strings:
    if '##' in line and '## Contents' not in line:
      subdirs[line.replace('## ','').replace('\n','')] = index
    index += 1

# Loop through headers and links
for subdir, index in subdirs.items():
    bookmarks_content.append(subdir_template.replace("SUBDIR",subdir))
    for line in raw_readme_strings[(index+1):]:
        if '- [' in line:
            title = line.split('[')[1].split(']')[0]
            url = line.split('](')[1].split(') ')[0]
            bookmarks_content.append(link_template.replace("URL",url).replace("TITLE",title))
        elif '##' in line:
            bookmarks_content.append('        </DL><p>\n')
            break

# Finish bookmark content
bookmarks_content.append('        </DL><p>\n    </DL><p>\n</DL>')

# Write bookmark file
with open(bookmark_file, "w") as bh: 
    bh.writelines(bookmarks_content)