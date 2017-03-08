# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 10:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('c_name', models.CharField(max_length=50, verbose_name='character name')),
                ('level', models.IntegerField(default=1)),
                ('hp', models.IntegerField()),
                ('experience', models.IntegerField(default=0)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('race', models.CharField(choices=[(b'Dragonborn', b'Dragonborn'), (b'Halfling', b'Halfling'), (b'Half-Elf', b'Half-Elf'), (b'Half-Orc', b'Half-Orc'), (b'Tiefling', b'Tiefling'), (b'Gnome', b'Gnome'), (b'Human', b'Human'), (b'Dwarf', b'Dwarf'), (b'Elf', b'Elf'), (b'Bugbear', b'Bugbear'), (b'Aasimar', b'Aasimar'), (b'Firbolg', b'Firbolg'), (b'Genasi', b'Genasi'), (b'Goblin', b'Goblin'), (b'Goliath', b'Goliath'), (b'Hobgoblin', b'Hobgoblin'), (b'Lizardfolk', b'Lizardfolk'), (b'Kenku', b'Kenku'), (b'Kobold', b'Kobold'), (b'Tabaxi', b'Tabaxi'), (b'Triton', b'Triton'), (b'Aarakocra', b'Aarakocra'), (b'Changeling', b'Changeling'), (b'Yuan-ti Pureblood', b'Yuan-Ti Pureblood'), (b'Warforged', b'Warforged'), (b'Shifter', b'Shifter'), (b'Minotaur', b'Minotaur'), (b'Kor', b'Kor'), (b'Merfolk', b'Merfolk'), (b'Vampire', b'Vampire')], max_length=25)),
                ('description', models.TextField(max_length=1000)),
                ('subrace', models.CharField(choices=[(b'Gavony', b'Gavony Human'), (b'Kessig', b'Kessig Human'), (b'Nephalia', b'Nephalia Human'), (b'Stensia', b'Stensia Human'), (b'Emeria', b'Emeria Merfolk'), (b'Ula', b'Ula Merfolk'), (b'Cosi', b'Cosi Merfolk'), (b'Grotag', b'Grotag Goblin'), (b'Lavastep', b'Lavastep Goblin'), (b'Tuktuk', b'Tuktuk Goblin'), (b'Protector', b'Aasimar Protector'), (b'Scourge', b'Aasimar Scourge'), (b'Fallen', b'Fallen Aasimar'), (b'Beasthide', b'Beasthide Shifter'), (b'Cliffwalk', b'Cliffwalk Shifter'), (b'Longstride', b'Longstride Shifter'), (b'Longtooth', b'Longtooth Shifter'), (b'Razorclaw', b'Razorclaw Shifter'), (b'Wildhunt', b'Wildhunt Shifter'), (b'Air', b'Air Genasi'), (b'Earth', b'Earth Genasi'), (b'Water', b'Water Genasi'), (b'Fire', b'Fire Genasi'), (b'Joraga', b'Joraga'), (b'Tajuru', b'Tajuru'), (b'Mul Daya', b'Mul Daya'), (b'Human Revenant', b'Human Revenant'), (b'Tiefling Revenant', b'Tiefling Revenant'), (b'Abyssal Tiefling', b'Abyssal Tiefling'), (b'Dragonborn Revenant', b'Dragonborn Revenant'), (b'Minotaur', b'Minotaur'), (b'Kor', b'Kor'), (b'Vampire', b'Vampire'), (b'Bugbear', b'Bugbear'), (b'Kenku', b'Kenku'), (b'Kobold', b'Kobold'), (b'Tabaxi', b'Tabaxi'), (b'Triton', b'Triton'), (b'Warforged', b'Warforged'), (b'Yuan-ti Pureblood', b'Yuan-Ti Pureblood'), (b'Aarakocra', b'Aarakocra'), (b'Lizardfolk', b'Lizardfolk'), (b'Hobgoblin', b'Hobgoblin'), (b'Goliath', b'Goliath'), (b'Firbolg', b'Firbolg'), (b'Dragonborn', b'Dragonborn'), (b'Mountain Dwarf', b'Mountain Dwarf'), (b'Human Variant', b'Human Variant'), (b'Half-Elf', b'Half-Elf'), (b'Wood-Born', b'Half-Wood Elf'), (b'Moon-Born', b'Half-Moon Elf'), (b'Sun-Born', b'Half-Sun Elf'), (b'Drow-Born', b'Half-Drow Elf'), (b'Aquatic-Born', b'Half-Aquatic Elf'), (b'Tiefling', b'Tiefling'), (b'Feral Tiefling', b'Feral Tiefling'), (b'Half-Orc', b'Half-Orc'), (b'Forest Gnome', b'Forest Gnome'), (b'Human', b'Human'), (b'Rock Gnome', b'Rock Gnome'), (b'Deep Gnome', b'Deep Gnome'), (b'Hill Dwarf', b'Hill Dwarf'), (b'Duergar', b'Duergar'), (b'High Elf', b'High Elf'), (b'Wood Elf', b'Wood Elf'), (b'Drow Elf', b'Drow'), (b'Eladrin', b'Eladrin'), (b'Ghostwise Halfling', b'Ghostwise Halfling'), (b'Lightfoot Halfling', b'Lightfoot Halfling'), (b'Stout Halfling', b'Stout Halfling')], max_length=25)),
                ('gender', models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female')], default='male', max_length=15)),
                ('alignment', models.CharField(choices=[(b'Lawful Good', b'Lawful Good'), (b'Lawful Neutral', b'Lawful Neutral'), (b'Lawful Evil', b'Lawful Evil'), (b'Neutral Good', b'Neutral Good'), (b'True Neutral', b'True Neutral'), (b'Neutral Evil', b'Neutral Evil'), (b'Chaotic Good', b'Chaotic Good'), (b'Chaotic Neutral', b'Chaotic Neutral'), (b'Chaotic Evil', b'Chaotic Evil')], max_length=50)),
                ('background', models.CharField(choices=[(b'Acolyte', b'Acolyte'), (b'Charlatan', b'Charlatan'), (b'City Watch', b'City Watch'), (b'Clan Crafter', b'Clan Crafter'), (b'Cloistered Scholar', b'Cloistered Scholar'), (b'Courtier', b'Courtier'), (b'Criminal', b'Criminal'), (b'Entertainer', b'Entertainer'), (b'Faction Agent', b'Faction Agent'), (b'Far Traveller', b'Far Traveler'), (b'Folk hero', b'Folk hero'), (b'Guild Artisan', b'Guild Artisan'), (b'Haunted One', b'Haunted One'), (b'Hermit', b'Hermit'), (b'Inheritor', b'Inheritor'), (b'Knight of the Order', b'Knight of the Order'), (b'Mercenary Veteran', b'Mercenary Veteran'), (b'Noble', b'Noble'), (b'Outlander', b'Outlander'), (b'Sage', b'Sage'), (b'Sailor', b'Sailor'), (b'Soldier', b'Soldier'), (b'Urban Bounty Hunter', b'Urban Bounty Hunter'), (b'Urchin', b'Urchin'), (b'Uthgardt Tribe Member', b'Uthgardt Tribe Member'), (b'Waterdhavian Noble', b'Waterdhavian Noble')], max_length=50)),
                ('dexterity', models.IntegerField()),
                ('charisma', models.IntegerField()),
                ('intelligence', models.IntegerField()),
                ('wisdom', models.IntegerField()),
                ('constitution', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('character_portrait', models.ImageField(blank=True, null=True, upload_to='character-portraits/%Y/%m/%d')),
                ('slug_id', models.CharField(default='W9HxtaVltpIo', max_length=12, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'character',
                'verbose_name_plural': 'characters',
            },
        ),
        migrations.CreateModel(
            name='CharacterManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CharClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_class', models.CharField(choices=[(b'Barbarian', b'Barbarian'), (b'Bard', b'Bard'), (b'Cleric', b'Cleric'), (b'Druid', b'Druid'), (b'Fighter', b'Fighter'), (b'Monk', b'Monk'), (b'Paladin', b'Paladin'), (b'Ranger', b'Ranger'), (b'Rogue', b'Rogue'), (b'Sorcerer', b'Sorcerer'), (b'Warlock', b'Warlock'), (b'Wizard', b'Wizard')], max_length=25)),
            ],
            options={
                'verbose_name': 'class',
                'verbose_name_plural': 'classes',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copper', models.IntegerField(blank=True, default=0)),
                ('silver', models.IntegerField(blank=True, default=0)),
                ('electrum', models.IntegerField(blank=True, default=0)),
                ('gold', models.IntegerField(blank=True, default=0)),
                ('platinum', models.IntegerField(blank=True, default=0)),
                ('armor', models.ManyToManyField(blank=True, to='items.Armor')),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='character.Character')),
                ('instruments', models.ManyToManyField(blank=True, to='items.Instruments')),
                ('kits', models.ManyToManyField(blank=True, to='items.Kits')),
                ('m_items', models.ManyToManyField(blank=True, to='items.MountItems', verbose_name='Mount Items')),
                ('mounts', models.ManyToManyField(blank=True, to='items.Mounts')),
                ('sets', models.ManyToManyField(blank=True, to='items.Sets')),
                ('tools', models.ManyToManyField(blank=True, to='items.Tools')),
                ('vehicles', models.ManyToManyField(blank=True, to='items.Vehicles')),
            ],
            options={
                'verbose_name': 'inventory',
                'verbose_name_plural': 'inventories',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[(b'Undercommon', b'Undercommon'), (b'Deep Speech', b'Deep Speech'), (b'Primordial', b'Primordial'), (b'Celestial', b'Celestial'), (b'Dwarvish', b'Dwarvish'), (b'Draconic', b'Draconic'), (b'Halfling', b'Halfling'), (b'Infernal', b'Infernal'), (b'Druidic', b'Druidic'), (b'Abyssal', b'Abyssal'), (b'Gnomish', b'Gnomish'), (b'Common', b'Common'), (b'Elvish', b'Elvish'), (b'Sylvan', b'Sylvan'), (b'Terran', b'Terran'), (b'Goblin', b'Goblin'), (b'Aquan', b'Aquan'), (b'Auran', b'Auran'), (b'Giant', b'Giant'), (b'Gnoll', b'Gnoll'), (b'Ignan', b'Ignan'), (b'Orcish', b'Orc')], max_length=50)),
                ('language_script', models.CharField(choices=[(b'No Script', b'None'), (b'Celestial', b'Celestial'), (b'Infernal', b'Infernal'), (b'Draconic', b'Draconic'), (b'Dwarvish', b'Dwarvish'), (b'Demonic', b'Demonic'), (b'Druidic', b'Druidic'), (b'Common', b'Common'), (b'Elvish', b'Elvish')], max_length=50)),
            ],
            options={
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(choices=[(b'Acrobatics', b'Acrobatics'), (b'Animal Handling', b'Animal Handling'), (b'Arcana', b'Arcana'), (b'Athletics', b'Athletics'), (b'Deception', b'Deception'), (b'History', b'History'), (b'Insight', b'Insight'), (b'Intimidation', b'Intimidation'), (b'Investigation', b'Investigation'), (b'Medicine', b'Medicine'), (b'Nature', b'Nature'), (b'Perception', b'Perception'), (b'Performance', b'Performance'), (b'Persuasion', b'Persuasion'), (b'Religion', b'Religion'), (b'Sleight of Hand', b'Sleight of Hand'), (b'Stealth', b'Stealth'), (b'Survival', b'Survival')], max_length=50)),
                ('check_type', models.CharField(choices=[(b'Intelligence Check', b'Intelligence Check'), (b'Constitution Check', b'Constitution Check'), (b'Dexterity Check', b'Dexterity Check'), (b'Strength Check', b'Strength Check'), (b'Charisma Check', b'Charisma Check'), (b'Wisdom Check', b'Wisdom Check')], max_length=50)),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weapon', models.CharField(choices=[(b'Fists', b'Fists'), (b'Club', b'Club'), (b'Dagger', b'Dagger'), (b'Greatclub', b'Greatclub'), (b'Handaxe', b'Handaxe'), (b'Javelin', b'Javelin'), (b'Light Hammer', b'Light Hammer'), (b'Mace', b'Mace'), (b'Quarterstaff', b'Quarterstaff'), (b'Sickle', b'Sickle'), (b'Spear', b'Spear'), (b'Light Crossbow', b'Light Crossbow'), (b'Dart', b'Dart'), (b'Shortbow', b'Shortbow'), (b'Sling', b'Sling'), (b'Battleaxe', b'Battleaxe'), (b'Flail', b'Flail'), (b'Glaive', b'Glaive'), (b'Greataxe', b'Greataxe'), (b'Greatsword', b'Greatsword'), (b'Halberd', b'Halberd'), (b'Lance', b'Lance'), (b'Longsword', b'Longsword'), (b'Maul', b'Maul'), (b'Morningstar', b'Morningstar'), (b'Pike', b'Pike'), (b'Rapier', b'Rapier'), (b'Scimitar', b'Scimitar'), (b'Shortsword', b'Shortsword'), (b'Trident', b'Trident'), (b'War Pick', b'War Pick'), (b'Warhammer', b'Warhammer'), (b'Whip', b'Whip'), (b'Blowgun', b'Blowgun'), (b'Hand Crossbow', b'Hand Crossbow'), (b'Heavy Crossbow', b'Heavy Crossbow'), (b'Longbow', b'Longbow'), (b'Net', b'Net')], max_length=50)),
                ('dice', models.IntegerField()),
                ('damage', models.CharField(choices=[(b'None', b'None'), (b'D1', b'D1'), (b'D2', b'D2'), (b'D4', b'D4'), (b'D6', b'D6'), (b'D8', b'D8'), (b'D10', b'D10'), (b'D12', b'D12'), (b'D20', b'D20'), (b'D100', b'D100')], max_length=4)),
                ('versatile_dice', models.IntegerField()),
                ('versatile_damage', models.CharField(choices=[(b'None', b'None'), (b'D1', b'D1'), (b'D2', b'D2'), (b'D4', b'D4'), (b'D6', b'D6'), (b'D8', b'D8'), (b'D10', b'D10'), (b'D12', b'D12'), (b'D20', b'D20'), (b'D100', b'D100')], max_length=4)),
                ('weapon_class', models.CharField(choices=[(b'Martial Melee Weapon', b'Martial Melee Weapon'), (b'Martial Ranged Weapon', b'Martial Range Weapon'), (b'Simple Melee Weapon', b'Simple Melee Weapon'), (b'Simple Ranged Weapon', b'Simple Range Weapon')], max_length=50)),
                ('damage_type', models.CharField(choices=[(b'Piercing Damage', b'Piercing'), (b'Bludgeoning Damage', b'Bludgeoning'), (b'Slashing Damage', b'Slashing'), (b'Burn Damage', b'Fire'), (b'Frost Damage', b'Cold'), (b'Toxic Damage', b'Posion'), (b'Acid Damage', b'Acid'), (b'Psychic Damage', b'Psychic'), (b'Necrotic Damage', b'Necrotic'), (b'Radiant Damage', b'Radiant'), (b'Lightning Damage', b'Lightning'), (b'Thunder Damage', b'Thunder'), (b'Force Damage', b'Force')], max_length=50)),
                ('cost', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('property1', models.CharField(choices=[(b'None', b'None'), (b'Ammunition', b'Ammo'), (b'Finesse', b'Finesse'), (b'Light', b'Light'), (b'Heavy', b'Heavy'), (b'Ranged', b'Ranged'), (b'Loading', b'Loading'), (b'Reach', b'Reach'), (b'Special', b'Special'), (b'Thrown', b'Thrown'), (b'Two-Handed', b'Two-Handed'), (b'Versatile', b'Versatile'), (b'Improvised', b'Improvised'), (b'Silvered', b'Silvered')], max_length=50)),
                ('property2', models.CharField(choices=[(b'None', b'None'), (b'Ammunition', b'Ammo'), (b'Finesse', b'Finesse'), (b'Light', b'Light'), (b'Heavy', b'Heavy'), (b'Ranged', b'Ranged'), (b'Loading', b'Loading'), (b'Reach', b'Reach'), (b'Special', b'Special'), (b'Thrown', b'Thrown'), (b'Two-Handed', b'Two-Handed'), (b'Versatile', b'Versatile'), (b'Improvised', b'Improvised'), (b'Silvered', b'Silvered')], max_length=50)),
                ('property3', models.CharField(choices=[(b'None', b'None'), (b'Ammunition', b'Ammo'), (b'Finesse', b'Finesse'), (b'Light', b'Light'), (b'Heavy', b'Heavy'), (b'Ranged', b'Ranged'), (b'Loading', b'Loading'), (b'Reach', b'Reach'), (b'Special', b'Special'), (b'Thrown', b'Thrown'), (b'Two-Handed', b'Two-Handed'), (b'Versatile', b'Versatile'), (b'Improvised', b'Improvised'), (b'Silvered', b'Silvered')], max_length=50)),
                ('property4', models.CharField(choices=[(b'None', b'None'), (b'Ammunition', b'Ammo'), (b'Finesse', b'Finesse'), (b'Light', b'Light'), (b'Heavy', b'Heavy'), (b'Ranged', b'Ranged'), (b'Loading', b'Loading'), (b'Reach', b'Reach'), (b'Special', b'Special'), (b'Thrown', b'Thrown'), (b'Two-Handed', b'Two-Handed'), (b'Versatile', b'Versatile'), (b'Improvised', b'Improvised'), (b'Silvered', b'Silvered')], max_length=50)),
                ('ammo_type', models.CharField(choices=[(b'None', b'None'), (b'Bolt', b'Crossbow Bolt'), (b'Blowdart', b'Blowdart'), (b'Stone', b'Stone'), (b'Arrow', b'Arrow')], max_length=50)),
                ('effective_range', models.IntegerField()),
                ('maximum_range', models.IntegerField()),
            ],
            options={
                'verbose_name': 'weapon',
                'verbose_name_plural': 'weapons',
            },
        ),
        migrations.AddField(
            model_name='inventory',
            name='weapons',
            field=models.ManyToManyField(blank=True, to='character.Weapon'),
        ),
        migrations.AddField(
            model_name='character',
            name='c_class',
            field=models.ManyToManyField(to='character.CharClass', verbose_name='class'),
        ),
        migrations.AddField(
            model_name='character',
            name='language',
            field=models.ManyToManyField(blank=True, to='character.Language'),
        ),
        migrations.AddField(
            model_name='character',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(blank=True, to='character.Skills'),
        ),
    ]