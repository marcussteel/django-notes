from adminpanelproduct.models import Product, Review
from adminpanelproduct.models import Product
from faker import Faker
faker = Faker()

for i in range(1, 100):
	product = Product(name=faker.name(), description=faker.paragraph(), is_in_stock=False)
	product.save()


# * pip install Faker

# py manage.py shell
# go to shell:
# yazdıktan sonra ikinci kez entera basmalıyız

faker = Faker()
for product in Product.objects.iterator():
    reviews = [Review(review=faker.paragraph(), product=product)
               for _ in range(0, 4)]
    Review.objects.bulk_create(reviews)

Review.objects.count()

