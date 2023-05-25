import re

# Remove all HTML tags from a string
html_pattern = "<(?:\"[^\"]*\"['\"]*|'[^']*'['\"]*|[^'\">])+>"
res = re.sub(html_pattern, '', '<html><body>Hello, <b>world</b>!<br /></body></html>') # returns 'Hello, world!'
print(res)

r1 = "<div>(.*?)<\\/div>" # Tag only
r2 = "(?:<div.*?class=\"some-class\".*?>)(.*?)(?:<\\/div>)" # Tag + class

# Extract text between specific HTML tag
html_pattern = "(?:<div.*?class=\"some-class\".*?>)(.*?)(?:<\\/div>)"
res = re.findall(html_pattern, '<html><body>Probably.<div class="some-class">Hello, world!</div><br />Today</body></html>')  # type: ignore # returns ['Hello, world!']
print(res)
