# Management Commands

## add_static_reports

This management command allows you to add static reports to the database.

### Usage

```bash
# Add/update reports
python manage.py add_static_reports

# Clear all existing reports and add new ones
python manage.py add_static_reports --clear
```

### Customization

To customize the reports being added, edit the `static_reports` list in:
```
main/management/commands/add_static_reports.py
```

Each report should have the following structure:
```python
{
    'year': 2024,
    'title': 'التقرير السنوي 2024',
    'pdf_file': 'reports/annual_report_2024.pdf',
    'description': 'التقرير السنوي لعام 2024',
    'is_active': True,
}
```

### Notes

- Make sure the PDF files exist in the `media/reports/` directory
- The command will update existing reports if they already exist (based on year)
- Use the `--clear` flag with caution as it will delete all existing reports
