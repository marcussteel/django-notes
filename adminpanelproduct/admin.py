from django.contrib import admin
from ckeditor.fields import RichTextField

# Register your models here.
from .models import Product


from django.utils import timezone


# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
# /* /        Display Settings            /*/
# /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date")
    #adminde producta tıklayınca neleri görmek istiyyorsak onu seçiyoruz
    list_editable = ("is_in_stock", ) 
    #eğer field üzerinde link varsa onu kabul etmez örn:name   
    # list_display_links = ("create_date", ) #can't add items in list_editable to here 
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name",)
    search_fields = ("name",)
    # when adding product in admin site
    prepopulated_fields = {'slug': ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = (('name', 'slug'), 'description', "is_in_stock") #fieldset kullandığımız zaman bunu kullanamayız

    fieldsets = (
        (None, {
            "fields": (
                # to display multiple fields on the same line, wrap those fields in their own tuple aynı tupple içindekileri aynı satırda koyuyor
                ('name', 'slug'), "is_in_stock"
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes": ("collapse", ),
            "fields": ("description",),
            'description': "You can use this section for optionals settings"
        })
    )


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

    list_display = ("name", "create_date", "is_in_stock","update_date", "added_days_ago")
    def added_days_ago(self, product):
        fark = timezone.now() - product.create_date
        return fark.days





admin.site.register(Product, ProductAdmin)


admin.site.site_title = "Marcus Apps" #site title 
admin.site.site_header = "Marcus Apps Admin Portal" #sırası ile 
admin.site.index_title = "Welcome to Marcus Apps Admin Portal"


