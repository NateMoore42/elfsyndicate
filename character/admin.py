from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *

import bulk_admin

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Player Info'), {'fields': ('player',)}),
        (_('Character Info'), {'fields': ('c_name', 'c_class', 'race', 'subrace', 'age', 'gender', 'height', 'weight')}),
        (_('Stat Info'), {'fields': ('hp', 'dexterity', 'strength', 'intelligence', 'wisdom', 'charisma', 'constitution')}),
        (_('Misc Info'), {'fields': ('language', 'skills', 'alignment')}),
    )

    list_display = ['c_name', 'race', 'subrace',]

admin.site.register(Character, CharacterAdmin)

class WeaponAdmin(bulk_admin.BulkModelAdmin):
    fieldsets = (
        (_('Weapon'), {'fields': ('weapon',)}),
        (_('Damage Info'), {'fields': ('dice', 'damage', 'damage_type')}),
        (_('Versatile Info'), {'fields': ('versatile_dice', 'versatile_damage')}),
        (_('Weapon Info'), {'fields': ('weapon_class', 'cost', 'weight',)}),
        (_('Properties'), {'fields': ('property1', 'property2', 'property3', 'property4')}),
        (_('Range Info'), {'fields': ('effective_range', 'maximum_range', 'ammo_type')}),
    )

    list_display = ['weapon', 'weapon_class', 'property1', 'property2',]

admin.site.register(Weapon, WeaponAdmin)

class InventoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Character'), {'fields': ('character',)}),
        (_('Currency Info'), {'fields': ('copper', 'silver', 'electrum', 'gold', 'platinum')}),
        (_('Equipment Info'), {'fields': ('weapons', 'armor')}),
        (_('Tool Info'), {'fields': ('tools', 'kits', 'sets', 'instruments')}),
        (_('Mount Info'), {'fields': ('m_items', 'vehicles', 'mounts')}),
    )


    list_display = ['character',]

admin.site.register(Inventory, InventoryAdmin)

class LanguageAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['language', 'language_script']

admin.site.register(Language, LanguageAdmin)

class SkillsAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['skills', 'check_type']

admin.site.register(Skills, SkillsAdmin)

class CharClassAdmin(bulk_admin.BulkModelAdmin):
    list_display = ['c_class']

admin.site.register(CharClass, CharClassAdmin)
