import os
from django.core.management.base import BaseCommand
from django.conf import settings
from uenowebsite.models import Building

class Command(BaseCommand):
    help = 'Load buildings and attach images if available'

    def handle(self, *args, **kwargs):
        image_folder = os.path.join(settings.MEDIA_ROOT, 'UenoBuildings')

        # Raw building names
        building_names = [
            "Comfort Kanzakigawa",
            "H-maison Hayashiji",
            "H-maison Kamishogakuji II",
            "H-maison Kamishogakuji",
            "H-maison Kitakagaya",
            "H-maison Tennoji West",
            "H-maison Teradachou",
            "Onlyone Kawanishi Marunouchi",
            "Reve G's HOUSE Higashi Osaka",
            "Reve G's HOUSE Ikeda",
            "Reve Maison Amagasaki Daimotsu",
            "Reve Maison Amagasaki Showadori",
            "Reve Maison Deyashiki",
            "Reve Maison Hagaromo",
            "Reve Maison Higashisumiyoshi",
            "Reve Maison Moriguchi Keihanhondori",
            "Reve Maison Shin Kobe",
        ]

        for name in building_names:
            # Get image filename (case-insensitive match)
            matching_file = None
            for f in os.listdir(image_folder):
                if f.lower().startswith(name.lower()):
                    matching_file = f
                    break

            photo_path = f'UenoBuildings/{matching_file}' if matching_file else None

            # Split into series and location
            words = name.split()
            if len(words) < 2:
                self.stdout.write(self.style.WARNING(f"Name format unclear: '{name}'"))
                continue

            # Assume first one or two words are the series, rest is location
            # Special case for series with multiple words like "Reve Maison"
            known_series_prefixes = [
                "H-maison",
                "Reve Maison",
                "Reve G's HOUSE",
                "Onlyone",
                "Comfort"
            ]

            matched_series = None
            for prefix in known_series_prefixes:
                if name.startswith(prefix):
                    matched_series = prefix
                    break

            if not matched_series:
                matched_series = words[0]  # Fallback to first word

            location = name.replace(matched_series, '').strip()

            # Create or update building
            building, created = Building.objects.get_or_create(
                name=name,
                defaults={
                    "series": matched_series,
                    "location": location
                }
            )

            if not created:
                # Update if data has changed
                updated = False
                if building.series != matched_series:
                    building.series = matched_series
                    updated = True
                if hasattr(building, 'location') and building.location != location:
                    building.location = location
                    updated = True
                if updated:
                    self.stdout.write(self.style.WARNING(f"Updated info for: {building.name}"))

            # Assign photo if not already assigned
            if photo_path and not building.photo:
                building.photo = photo_path
                building.save()
                self.stdout.write(self.style.SUCCESS(f"Photo added: {building.name}"))

            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {building.name}"))
            elif not photo_path:
                self.stdout.write(self.style.NOTICE(f"No image found for: {building.name}"))

        self.stdout.write(self.style.SUCCESS("Building load complete."))
