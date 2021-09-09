def featuredProduct(products):
    import ipdb; ipdb.set_trace()
    products_dict = {i:products.count(i) for i in set(products) if products.count(i) > 1}
    purchased_max_value = sorted(set(list(products_dict.values())))
    featured_list = [product for product in set(products) if product in products_dict and  products_dict[product] == purchased_max_value[-1]]
    featured_list.sort()
    return featured_list[-1]




if __name__ == '__main__':

    products = ['redShirt', 'redShirt', 'greenPants', 'redShirt', 'orangeShoes', 'blackPants', 'blackPants', 'orangeShoes', 'orangeShoes']
    print(featuredProduct(products))
