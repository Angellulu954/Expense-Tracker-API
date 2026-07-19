from enum import Enum
class Category(Enum):
    FOOD="Food"
    TRANSPORT="Transport"
    RENT="Rent"
    ENTERTAINMENT="Entertainment"
    HEALTHCARE="Healthcare"
    SHOPPING="Shopping"
    OTHER="Other"
class Order(Enum):
    DATE_NEWEST="date_newest"
    DATE_OLDEST="date_oldest"
    TITLE_ASC="title_asc"
    TITLE_DESC="title_desc"
    CATEGORY_ASC="category_asc"
    CATEGORY_DESC="category_desc"
    AMOUNT_DESC="amount_desc"
    AMOUNT_ASC="amount_asc"
    