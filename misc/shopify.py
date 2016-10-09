import json, requests

QUERY_URL = 'http://shopicruit.myshopify.com/products.json?page={}'

'''
subtotal_for_query_set(products, query_set)
Parameters:
	- products: the list of product objects on a page
	- query_set: the set of product types you are interested in finding the total for
Output:
	returns the subtotal for all product variants on a page based on the query set of product types
'''
def subtotal_for_query_set(products, query_set):
	result = 0
	for product in products:
		product_type = product['product_type']
		variants = product['variants']
		result += sum(
			[float(variant['price']) for variant in variants if product_type in query_set]
		)
	return result

'''
total_for_query_set(query_set)
Parameters:
	- query_set: the set of product types
Output:
	returns the total for all pages based on the query set of product types
'''
def total_for_query_set(query_set):
	total = 0
	page = 1
	while True:
		response = requests.get(QUERY_URL.format(page))
		products = json.loads(response.text)['products']
		if len(products) == 0:
			break
		total += subtotal_for_query_set(products, query_set)
		page += 1
	return total

def main():
	print total_for_query_set(set(['Clock', 'Watch']))

if __name__ == '__main__':
	main()
