from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Product Name",
        help_text="The display name for this product. Keep it concise and descriptive."
    )
    
    sku = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="SKU (Stock Keeping Unit)",
        help_text="Unique identifier for inventory tracking. Auto-generated if left blank."
    )
    
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price (USD)",
        help_text="Retail price in US dollars. Do not include currency symbol."
    )
    
    weight = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Weight (lbs)",
        help_text="Product weight in pounds. Used for shipping calculations."
    )
    
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active Product",
        help_text="Uncheck to hide this product from the storefront without deleting it."
    )
    
    meta_description = models.CharField(
        max_length=160,
        verbose_name="SEO Meta Description",
        help_text="Brief description for search engines (160 characters max). Leave blank for auto-generation.",
        blank=True
    )
    
    featured_until = models.DateTimeField(
        verbose_name="Featured Until",
        help_text="Product will appear in featured section until this date. Leave blank to feature indefinitely.",
        null=True,
        blank=True
    )