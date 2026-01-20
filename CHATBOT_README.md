# Chatbot Feature

## Overview

The chatbot feature provides an intelligent Q&A system for your website visitors. It allows you to manage frequently asked questions and answers through a dashboard interface, and displays a chatbot widget on all pages for easy user interaction.

## Features

- **Smart Search**: Searches through questions, answers, and keywords to find the best match
- **Categorization**: Organize Q&As by categories (Services, About Us, Contact Info, etc.)
- **View Tracking**: Track how many times each answer has been shown
- **Quick Questions**: Display popular questions for one-click access
- **Dashboard Management**: Full CRUD operations for managing chatbot content
- **RTL Support**: Fully compatible with Arabic (RTL) interface
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Usage

### Dashboard Management

Access the chatbot management through the dashboard sidebar:
1. Log in to the dashboard
2. Click on "إدارة الشات بوت" (Chatbot Management)
3. From there you can:
   - View all Q&As with statistics
   - Add new questions and answers
   - Edit existing Q&As
   - Delete Q&As
   - View detailed statistics

### Adding Q&As

You can add Q&As in two ways:

#### 1. Through Dashboard
Navigate to **Chatbot Management > Add New** and fill in:
- **Question**: The question users might ask
- **Answer**: The answer to provide
- **Keywords** (optional): Comma-separated keywords for better matching
- **Category** (optional): Group questions by category
- **Order**: Display order (lower numbers first)
- **Active**: Whether to show this Q&A in the chatbot

#### 2. Using Management Command

Run the following command to add sample Q&As:

```bash
python manage.py add_chatbot_qas
```

To clear existing Q&As and add fresh ones:

```bash
python manage.py add_chatbot_qas --clear
```

## Chatbot Widget

The chatbot widget appears on all public pages as a floating button in the bottom-left corner:

- **Click the button** to open the chat window
- **Type your question** in the input field
- **View quick questions** for common inquiries
- **Get instant answers** from the knowledge base

## API Endpoints

### Search for Answers
- **URL**: `/api/chatbot/search/`
- **Method**: POST
- **Parameters**: `query` (the user's question)
- **Returns**: Best matching answer and related questions

### Get All Q&As
- **URL**: `/api/chatbot/all/`
- **Method**: GET
- **Returns**: All active Q&As grouped by category

## Customization

### Styling
The chatbot widget styles are defined in `/templates/partials/_chatbot.html`. You can customize:
- Colors and gradients
- Button position
- Window size
- Animations

### Keywords
Add relevant keywords to each Q&A to improve search accuracy. Keywords should be comma-separated:
```
Example: "خدمات,استثمار,portfolio,services"
```

### Categories
Common categories to use:
- `من نحن` (About Us)
- `الخدمات` (Services)
- `معلومات الاتصال` (Contact Info)
- `علاقات المستثمرين` (Investor Relations)
- `الوظائف` (Jobs)
- `عام` (General)

## Statistics

The dashboard provides statistics including:
- Total number of Q&As
- Active Q&As count
- Total views across all answers
- Individual view counts per Q&A

## Best Practices

1. **Be Concise**: Keep questions and answers short and to the point
2. **Use Keywords**: Add relevant keywords to improve search results
3. **Organize by Category**: Group related questions together
4. **Regular Updates**: Review and update Q&As based on common user queries
5. **Test Thoroughly**: Test the chatbot with various phrasings of questions

## Migration

To apply the database changes for the chatbot feature, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Support

For issues or questions about the chatbot feature, please contact the development team.
