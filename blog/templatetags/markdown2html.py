import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown2html(markdown_text):
	html = markdown.markdown(markdown_text, output='html5')
	return mark_safe(html)