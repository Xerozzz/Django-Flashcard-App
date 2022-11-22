from django import template

from cards.models import BOXES, Card

register = template.Library()

@register.inclusion_tag("cards/box_links.html") # Tells Django it is inclusion tag
def boxes_as_links():
    boxes = []
    for box_num in BOXES: # loops through boxes
        card_count = Card.objects.filter(box=box_num).count() # keeps track of number of cards in current box
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })

    return {"boxes": boxes} # Returns DICT for box_links.html