from . import models


def add_category(category_info):
    """
    Function to add a new category
    :param category_info: dict
    :return: True
    """

    category = models.Category(
        title=category_info['title'],
        description=category_info['description']
    )

    category.save()

def add_product(product_info):
    """
    Function to add a new products
    :param product_info: dict
    :return: True
    """

    product = models.Product(
        title=product_info['title'],
        price=product_info['price'],
        short_description=product_info['short_description'],
        description=product_info['description']
    )

    if 'category' in product_info.keys():
        product.category.add(product_info['category'])

    product.save()

def set_value(title, parameter, value):
    """
    Function that sets value for a parameter of a given object
    :param title: string
    :param parameter: string
    :param value: string
    :return: True
    """
    product = models.Product.objects.get(title=title)
    product[parameter] = value

def get_products():
    """
    Function that returns all the products available
    :return: QuerySet
    """
    products = models.Product.objects.all()
    return products

def get_product(title):
    """
    Function that returns an object by its name
    :param title: string
    :return: QuerySet
    """

    product = models.Product.objects.get(title=title)
    return product

def get_category(title):
    """
    Function that returns an object by its name
    :param title: string
    :return: QuerySet
    """

    category = models.Category.objects.get(title=title)
    return category

def sort(order, products=None):
    """
    Function that sorts al the products by price
    :param order: string
    :param products: QuerySet
    :return: True
    """

    if products is None:
        products = models.Product.objects.order_by('price')
    else:
        products = products.order_by('price')

    if order == 'desc':
        return products
    else:
        return products[::-1]

def price_range(min, max):
    """
    Function that returns a list of products in certain price range
    :param min: int
    :param max: int
    :return: QuerySet
    """

    products = models.Product.objects.filter(price__lte=max).filter(price__gte=min)
    return products

def get_by_category(category, products=None):
    """
    Function that returns products of a given category
    :param category: string
    :param products: QuerySet
    :return: QuerySet
    """

    if products is None:
        products = models.Product.objects.filter(category__title=category)
    else:
        products = products.filter(category__title=category)

    return products
