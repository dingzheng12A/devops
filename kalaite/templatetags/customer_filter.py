from django import template
register = template.Library()

@register.filter
def multi(x,y):
    return x*y

@register.filter
def chufa(x,y):
    if y==0:
       return 0
    else:
       return abs(x/y)

@register.filter
def get_first(s,seprator=""):
    if s=="":
       return ""
    if type(s)==list:
       return s[0]
    else:
    	return s.split(seprator)[0]

@register.simple_tag
def concat(s=[],seprator="."):
    return seprator.join(s)
    
      
