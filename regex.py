import re

text = 'This is some text with punctuation.'

matchy = re.match('This is s', text,re.I)
span = matchy.span()
start,end=span

html = '<p dir="auto">As you can see from the example above, the pattern we are looking for (or the substring we are looking for) is <em>I love to teach</em>. The match function returns an object <strong>only</strong> if the text starts with the pattern.</p>'

search_html = re.search('we',html,re.I)

findAll_html = re.findall('we',html,re.I)

replaced_txt = re.sub(' is ','aret',text,re.I)

print(replaced_txt)
