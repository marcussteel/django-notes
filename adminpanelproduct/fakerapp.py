from adminpanelproduct.models import Product
from faker import Faker
faker = Faker()

for i in range(1, 200):
	product = Product(name=faker.name(), description=faker.paragraph(), is_in_stock=False)
	product.save()


# * pip install Faker

# py manage.py shell
# go to shell:
# yazdıktan sonra ikinci kez entera basmalıyız