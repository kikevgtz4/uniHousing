from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from accounts.models import User

class Property(models.Model):
    """Property model for listings"""
    
    class PropertyType(models.TextChoices):
        APARTMENT = 'apartment', _('Apartment')
        HOUSE = 'house', _('House')
        ROOM = 'room', _('Room')
        STUDIO = 'studio', _('Studio')
        OTHER = 'other', _('Other')
    
    # Basic info
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.APARTMENT,
    )
    
    # Details
    bedrooms = models.PositiveSmallIntegerField()
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1)
    total_area = models.DecimalField(max_digits=8, decimal_places=2, help_text="Area in square meters")
    furnished = models.BooleanField(default=False)
    amenities = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )
    rules = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        default=list
    )
    
    # Pricing
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_frequency = models.CharField(
        max_length=20,
        choices=[
            ('monthly', _('Monthly')),
            ('bimonthly', _('Bimonthly')),
            ('quarterly', _('Quarterly')),
            ('yearly', _('Yearly')),
        ],
        default='monthly',
    )
    included_utilities = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )
    
    # Availability
    available_from = models.DateField()
    minimum_stay = models.PositiveSmallIntegerField(help_text="Minimum stay in months", default=1)
    maximum_stay = models.PositiveSmallIntegerField(help_text="Maximum stay in months", null=True, blank=True)
    
    # Relations
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
        ordering = ['-created_at']


class PropertyImage(models.Model):
    """Images for properties"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')
    is_main = models.BooleanField(default=False)
    caption = models.CharField(max_length=200, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)
    
    def __str__(self):
        return f"Image for {self.property.title}"


class Room(models.Model):
    """Individual room model for partial property rentals"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100, help_text="E.g., 'Master Bedroom', 'Room 1'")
    size = models.DecimalField(max_digits=6, decimal_places=2, help_text="Size in square meters")
    private_bathroom = models.BooleanField(default=False)
    furnished = models.BooleanField(default=False)
    description = models.TextField()
    
    # Availability
    available_from = models.DateField()
    occupied = models.BooleanField(default=False)
    current_tenant = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='occupied_rooms'
    )
    
    # Pricing
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} in {self.property.title}"


class PropertyReview(models.Model):
    """Reviews for properties"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_reviews')
    rating = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    cleanliness = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    value = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    location = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    accuracy = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    communication = models.PositiveSmallIntegerField(help_text="Rating from 1 to 5")
    review_text = models.TextField()
    pros = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        default=list
    )
    cons = ArrayField(
        models.CharField(max_length=200),
        blank=True,
        default=list
    )
    stay_period = models.CharField(max_length=100, help_text="E.g., 'Jan 2023 - June 2023'")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review for {self.property.title} by {self.reviewer.username}"