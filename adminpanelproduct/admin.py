from django.utils.safestring import mark_safe
from django.contrib import admin
from ckeditor.fields import RichTextField


# Register your models here.
from .models import Product,Review,Category


from django.utils import timezone

# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* Review modelini inline  görmek için          /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/


class ReviewInline(admin.TabularInline):  # StackedInline farklı bir görünüm aynı iş
    '''Tabular Inline View for '''
    model = Review
    extra = 1
    # classes = ('collapse',)
    # min_num = 3
    # max_num = 20




# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /        Display Settings            /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago","how_many_reviews", "bring_image")
    #adminde producta tıklayınca neleri görmek istiyyorsak onu seçiyoruz
    list_editable = ("is_in_stock", ) 
    #eğer field üzerinde link varsa onu kabul etmez örn:name   
    list_display_links = ("create_date", ) #can't add items in list_editable to here 
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)
    search_fields = ("name",)
    # when adding product in admin site
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"
    readonly_fields = ("bring_image",)
    # inlines: (ReviewInline, )
    
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "fields": (
                # to display multiple fields on the same line, wrap those fields in their own tuple
                ('name', 'slug'), "is_in_stock"
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes": ("collapse", ),
            "fields": ("description", "categories", "product_img", "bring_image"),
            'description': "You can use this section for optionals settings"
        })
    )
    filter_horizontal = ("categories", )
    # fitler_vertical = ("categories", )


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /             Actions                /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

    actions = ("is_in_stock", "is_in_stock2")
    def is_in_stock(self, request, queryset):
         count = queryset.update(is_in_stock=True)
         self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'

    def is_in_stock2(self, request, queryset):
        count = queryset.update(is_in_stock=False)
        self.message_user(request, f"{count} çeşit ürün stoğa çıkarıldı")
    is_in_stock2.short_description = 'İşaretlenen ürünleri stoktan çıkar'


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /             Column ekleme          /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

    
    # list_display = ("name", "create_date", "is_in_stock", "update_date","added_days_ago",)
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /         Resim Görme                /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
#from django.utils.safestring import mark_safe     modelste eklediğimiz için buraya yazmasak da olur
    # def bring_image(self, obj):
    #     if obj.product_img:
    #         return mark_safe(f"<img src={obj.product_img.url} width=400 height=400></img>")
    #     return mark_safe(f"<h3>{obj.name} has not image </h3>")

# class ProductAdmin(admin.ModelAdmin):
#     inlines = (ReviewInline,)


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* Review modelini görmek için          /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

#from .models import Product,Review
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released') #göstermek istediğim fieldları gösteriyordu __str__ Review da productname-self review olarak belirtilmiş
    list_per_page = 50
    raw_id_fields = ('product',)


admin.site.register(Review, ReviewAdmin)





admin.site.register(Category)
admin.site.register(Product, ProductAdmin)






admin.site.site_title = "Marcus Apps" #site title 
admin.site.site_header = "Marcus Apps Admin Portal" #sırası ile 
admin.site.index_title = "Welcome to Marcus Apps Admin Portal"


