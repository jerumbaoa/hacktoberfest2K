import re

def kebab(s):
  """
  kebab('camelCase'); # 'camel-case'
  kebab('some text'); # 'some-text'
  kebab('some-mixed_string With spaces_underscores-and-hyphens'); # 'some-mixed-string-with-spaces-underscores-and-hyphens'
  kebab('AllThe-small Things'); # "all-the-small-things"
  """
  
  return re.sub(r"(\s|_|-)+","-",
    re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: mo.group(0).lower(), s)
  )
 
