from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from . import query


def initialize_store():
    """
    A function that adds some basic staff to store products
    :return: list
    """

    short_desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis purus in purus hendrerit, a placerat elit blandit.'

    desc = """
           <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed lobortis purus in purus hendrerit, a placerat elit blandit. Donec semper vulputate nulla eget venenatis. Phasellus rhoncus elit dui, ut bibendum erat varius vitae. Duis blandit semper risus, a euismod nunc tempor non. Fusce sem massa, vulputate a feugiat id, semper vel justo. Ut pellentesque massa sem, eu scelerisque dui tincidunt eu. Morbi cursus porttitor metus, nec rhoncus dolor egestas fermentum. Sed malesuada maximus posuere. Mauris orci sapien, ultricies eget arcu at, tristique ullamcorper enim. Nullam euismod rhoncus sem, et aliquet turpis faucibus in. Vestibulum sed semper diam. Fusce nulla lacus, imperdiet in aliquet eu, hendrerit bibendum metus. Donec commodo blandit magna, et tempus metus tempor non. In id sapien varius, fermentum turpis bibendum, dignissim nisi.</p> 
           <p>Praesent ullamcorper arcu pretium consectetur viverra. Ut ac nibh rutrum, venenatis leo vitae, rhoncus nulla. Aliquam sed varius erat. Morbi sit amet diam id odio vulputate elementum. Nulla luctus nec arcu id iaculis. Sed tortor purus, malesuada at ex quis, finibus tincidunt dui. Suspendisse metus mauris, gravida non sem a, viverra maximus libero. Phasellus congue lorem eu pulvinar fermentum. Phasellus pharetra ultricies arcu, ac malesuada justo porta vel. Ut congue rutrum augue, in molestie urna accumsan ut. Ut ut luctus diam. Etiam posuere arcu vel convallis sollicitudin.</p> 
           <ul>
               <li>Aliquam nec diam vitae metus eleifend maximus</li>
               <li>Curabitur eu ornare augue</li>
               <li>Nulla facilisi. Suspendisse sit amet risus varius, aliquet eros a, dapibus est</li>
           </ul>
           <p>Morbi sit amet lacus orci. Praesent at dui quis dolor scelerisque porttitor. Aliquam eu porttitor felis. Sed facilisis purus libero, nec mollis est tristique et. Phasellus fermentum, eros a pretium rhoncus, orci lectus dapibus quam, ac feugiat purus diam tristique mauris. Praesent neque ipsum, pellentesque a lacus id, sodales ultrices felis.</p> 
           """

    names = ['Pork', 'Sandwich bags', 'Lunch meat', 'All purpose', 'Flour', 'Soda', 'Butter', 'Vegetables', 'Beef']
    products = []

    for pr in names:
        products.append({
            'title': pr,
            'price': 123,
            'short_description': short_desc,
            'description': desc,
        })

    return names


def initialize_categories():
    """
    A function that adds some basic categories to store
    :return: True
    """

    desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse luctus magna a viverra porta. Sed elementum tincidunt porttitor. Praesent gravida eget felis eu suscipit. Quisque eu maximus quam, sit amet gravida nibh. Pellentesque vehicula lectus lacinia tortor tincidunt, ut euismod nunc feugiat. Proin id aliquet risus.'

    names = ['Food', 'Home', 'Bathroom']
    categories = []

    for name in names:
        categories.append({
            'title': name,
            'description': desc,
        })

    return categories


class ProductsView(View):

    def get(self, request):
        """
        products = initialize_store()
        for product in products:
            query.add_product(product)
        """

        """
        names = initialize_store()

        for name in names:
            product = query.get_product(name)
            if name == 'All purpose':
                category = query.get_category('Bathroom')
                product.category.add(category)
                product.save()
            else:
                category = query.get_category('Food')
                product.category.add(category)
                product.save()
        """

        if request.GET.get('ctg') == 'fd':
            products = query.get_by_category('Food')
        elif request.GET.get('ctg') == 'hm':
            products = query.get_by_category('Home')
        elif request.GET.get('ctg') == 'bth':
            products = query.get_by_category('Bathroom')
        else:
            products = query.get_products()


        if request.GET.get('sort') == 'asc':
            products = query.sort('asc', products)
        elif request.GET.get('desc') == 'desc':
            products = query.sort('desc', products)



        context = {
            'products': products,
        }
        return render(request, 'products/products.html', context=context)


class CategoriesView(View):

    def get(self, request, title):

        if title == 'fd':
            title = 'Food'
        elif title == 'hm':
            title = 'Home'
        elif title == 'bth':
            title = 'Bathroom'

        category = query.get_category(title)

        products = query.get_by_category(title)

        context = {
            'title': title,
            'description': category.description,
            'products': products,
        }

        return render(request, 'products/categories.html', context=context)
