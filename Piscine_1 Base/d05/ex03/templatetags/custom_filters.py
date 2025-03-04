from django import template

# Crate a new template library
register = template.Library()


# Create a new template filter
@register.filter
def to(value):
    """Return a list of numbers from 0 to the given value."""
    try:
        return range(0, value)
    except TypeError:
        return []

