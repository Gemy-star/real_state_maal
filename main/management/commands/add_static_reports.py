# -*- coding: utf-8 -*-
"""
Management command to add static reports to the database.
Usage: python manage.py add_static_reports
"""
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import Report
import os


class Command(BaseCommand):
    help = 'Add static reports to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing reports before adding new ones',
        )

    def handle(self, *args, **options):
        # Clear existing reports if requested
        if options['clear']:
            count = Report.objects.count()
            Report.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f'Deleted {count} existing reports')
            )

        # Define static reports to add
        # You can customize these based on your needs
        static_reports = [
            {
                'year': 2024,
                'title': 'التقرير السنوي 2024',
                'pdf_file': 'reports/annual_report_2024.pdf',
                'description': 'التقرير السنوي لعام 2024',
                'is_active': True,
            },
            {
                'year': 2023,
                'title': 'التقرير السنوي 2023',
                'pdf_file': 'reports/annual_report_2023.pdf',
                'description': 'التقرير السنوي لعام 2023',
                'is_active': True,
            },
            {
                'year': 2022,
                'title': 'التقرير السنوي 2022',
                'pdf_file': 'reports/annual_report_2022.pdf',
                'description': 'التقرير السنوي لعام 2022',
                'is_active': True,
            },
            {
                'year': 2021,
                'title': 'التقرير السنوي 2021',
                'pdf_file': 'reports/annual_report_2021.pdf',
                'description': 'التقرير السنوي لعام 2021',
                'is_active': True,
            },
        ]

        created_count = 0
        updated_count = 0
        skipped_count = 0

        for report_data in static_reports:
            year = report_data['year']
            
            # Check if report already exists
            existing_report = Report.objects.filter(year=year).first()
            
            if existing_report:
                # Update existing report
                for key, value in report_data.items():
                    setattr(existing_report, key, value)
                existing_report.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated report for year {year}')
                )
            else:
                # Create new report
                Report.objects.create(**report_data)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created report for year {year}')
                )

        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\n--- Summary ---\n'
                f'Created: {created_count}\n'
                f'Updated: {updated_count}\n'
                f'Skipped: {skipped_count}\n'
                f'Total reports in database: {Report.objects.count()}'
            )
        )
