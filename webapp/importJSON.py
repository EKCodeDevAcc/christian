import json
import copy

# https://stackoverflow.com/questions/43475240/django-import-reformat-json-into-model
with open('webapp/fixtures/products.json') as dataf, open('webapp/fixtures/output.json', 'w') as out:
    # data from a given JSON file, products.json in this case
    data = json.load(dataf)

    # a new list that will append a data in desired format
    newdata = []

    # data of records field from products.json
    records = data['records']

    for i, block in enumerate(records):
        # add new field called model and provide Model name of this Application
        # also add pk value that starts from 1 and increment it
        new = dict(model="webapp.Product", pk=i+1)

        # set new field called fields and add all data columns from products.json
        new['fields'] = dict(title=block['title'],
                            isbn13=block['isbn13'],
                            isbn=block['isbn'],
                            image=block['image'],
                            product_id=block['id'],
                            link=block['link'],
                            customer_rating=block['customer_rating'],
        )

        # append a generated data to newdata list
        newdata.append(copy.deepcopy(new))

    json.dump(newdata, out, indent=2)
