from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="category name")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True, null=True)
    description = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_in_stock = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name="products")
    product_img = models.ImageField(
        null=True, blank=True, default="images/logo.png", upload_to="product/")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def how_many_reviews(self):
        count = self.reviews.count()
        return count

#from django.utils.safestring import mark_safe     # eğer img varsa o image ile ilgili önce string ifadeye çeviriyor
    def bring_image(self): #image eklemek için ister buraya ister admiins py a eklenebilir
        if self.product_img:
            return mark_safe(f"<img src={self.product_img.url} width=50 height=50></img>")
        return mark_safe(f"<h3>{self.name} has not image </h3>")


    # def bring_image(self):
    #     if self.product_img:
    #         return mark_safe(f"<img src={self.product_img.url} width=400 height=400></img>")
    #     return mark_safe(f"<h3>{self.name} has not image </h3>")




# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /          Rich Text Editors         /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#    WYSIWYG (what you see is what you get)
#    https: // djangopackages.org/grids/g/wysiwyg/
#    https: // django-ckeditor.readthedocs.io/en/latest/
# pip install django-ckeditor
#* 'ckeditor',      >> > add installed_apps
#    from ckeditor.fields import RichTextField
    # description = models.TextField(blank=True) >>>> description = RichTextField()


    # ilişkisel bir veri tabanında birden fazla model i nasıl gösterebiliriz
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    is_released = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.product.name} - {self.review}"





