from django import template


register = template.Library()


@register.filter()
def mymedia(data):
    if data:
        return f'/media/{data}'
    return f'catalog/media/pic.jpg'
