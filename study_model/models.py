from tabnanny import verbose
from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name= models.CharField(max_length=30)
    number = models.IntegerField()
    description = models.TextField(null=True, blank=True) #birisi frontend biri backend ile ilgili
    register_date = models.DateField(auto_now_add=True) #burası ilk kayıt alıyor bırakıyor sonra değişmiyor
    last_update = models.DateTimeField(auto_now=True) # autonow yeniliyor kendini
    is_active = models.BooleanField(default=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True) # media rootunun altına profile_pics diye klasör oluşturup oraya atacak resimleri
    
    def __str__(self):
        return f"{self.last_name} {self.first_name}"


# bu metodu normalde views de orm metodları çalıştırılır.  
#  ya da shell ile yapabilirsin: python manage.py shell    >>  from study_model.models import Student 
#  s1 = Student.objects.get(number=111)
# s1.student_year_status

    def student_year_status(self):
        #" Returns the student's year status . "
        import datetime
        if self.register_date < datetime.date(2019, 1, 1):
            return " Senior "
        elif self.register_date < datetime.date(2020, 1, 1):
            return " Junior "
        else:
            return " Freshman "


# çıktımız listeye veri girince ne olarak görünsün dönsün bizde
    def __str__(self):
        return (f"{self.number}    {self.first_name}")


    class Meta:
        # sıralama yapalım , normalde instance oluşturmaya göre yapar
        ordering = ["number"]
        # admin panelde solda models ismimizi değiştirelim
        verbose_name_plural = "Student_List"
        


    #önce bunu python a söylemem lazım,  
    # 
    # makemigration: ben bir liste hazırladım sen gerekli scriptini hzırla diyoruz
    # kendisi gitti migrations klasörü altında 0001_initial... şeklinde dosyahazırladı, içinde id de çıktı
    #   migrate: bununla da database de tablomu oluşturuyor. sqlite extensionu ile görebiliriz. 
    #aynı dizinde db.sqlite diye bir dosya oluştu, buraya gel, sağ tık open database, en altta sqlite explorer çıkıyor
    # bunu admin panelde görebilirim artık. önce superuser py -m venv env python manege.py createsuperuser
    #


