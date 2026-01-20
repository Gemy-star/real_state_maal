# Quick Setup Guide

## Apply Database Migrations

First, apply the chatbot migration to create the necessary database tables:

```bash
python manage.py migrate
```

## Seed Chatbot Data

After migration, populate the chatbot with sample Q&As:

```bash
python manage.py add_chatbot_qas
```

This will add 10 sample questions covering:
- من نحن (About Us)
- الخدمات (Services) 
- معلومات الاتصال (Contact Info)
- علاقات المستثمرين (Investor Relations)
- الوظائف (Jobs)

### Options

**Clear existing data and add fresh:**
```bash
python manage.py add_chatbot_qas --clear
```

## Seed Reports Data

To add sample reports:

```bash
python manage.py add_static_reports
```

**Clear and re-add:**
```bash
python manage.py add_static_reports --clear
```

## What's Fixed

### 1. Reports Page (/reports/)
- ✅ Fixed padding to show page title properly
- ✅ Added top padding of 8rem to account for fixed navbar
- ✅ Added extra padding to page header

### 2. WhatsApp Button
- ✅ Moved WhatsApp button below chatbot widget
- ✅ Positioned at `bottom: 110px` (chatbot is at 30px)
- ✅ Both buttons now visible and accessible

### 3. Chatbot Seeding
- ✅ Management command created: `add_chatbot_qas.py`
- ✅ Includes 10 sample Q&As in Arabic
- ✅ Supports --clear flag to reset data

## Button Positions

```
Chatbot Button:    bottom: 30px, left: 30px
WhatsApp Button:   bottom: 110px, left: 30px (80px above chatbot)
```

Both buttons are now properly spaced and won't overlap.

## Test the Changes

1. Visit `/reports/` page - title should now be visible
2. Scroll down - both chatbot and WhatsApp buttons should be visible
3. Click chatbot button - widget should open
4. Click WhatsApp button - should redirect to WhatsApp

## Next Steps

After running the migration and seeding commands:
1. Visit the dashboard at `/chatbot/` to manage Q&As
2. Add custom questions based on your business needs
3. Test the chatbot widget on the homepage
4. Review analytics in the dashboard
