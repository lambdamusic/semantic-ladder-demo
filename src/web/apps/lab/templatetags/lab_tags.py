from django import template

from lab import files

register = template.Library()


@register.filter
def cond(c):
    """A condition with its label: {{ c|cond }} gives R4 csv+markdown."""
    return files.cond(c)
