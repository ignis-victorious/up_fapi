#  ________________________
#  Import LIBRARIES
#  Import FILES
from app.models.models import ItemBase

#  ________________________


# Fake database
items_db: dict[int, ItemBase] = {}
counter: int = 0
