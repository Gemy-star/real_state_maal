# -*- coding: utf-8 -*-
"""
Script to automatically translate common Arabic strings to English in the .po file
"""
import re

# Common translations mapping (Arabic -> English)
TRANSLATIONS = {
    # Navigation
    "من نحن": "About Us",
    "الرئيسية": "Home",
    "تواصل معنا": "Contact Us",
    "الخدمات": "Services",
    "الأخبار": "News",
    "التقارير": "Reports",
    "علاقات المستثمرين": "Investor Relations",
    "خدمة المساهمين": "Shareholder Services",
    "سياسة الخصوصية": "Privacy Policy",
    # Common words
    "العودة": "Back",
    "إرسال": "Send",
    "حفظ": "Save",
    "حذف": "Delete",
    "تعديل": "Edit",
    "إضافة": "Add",
    "بحث": "Search",
    "المزيد": "More",
    "التفاصيل": "Details",
    "عرض": "View",
    "تحميل": "Download",
    "إغلاق": "Close",
    "نعم": "Yes",
    "لا": "No",
    "تأكيد": "Confirm",
    "إلغاء": "Cancel",
    # Contact page
    "معلومات الاتصال": "Contact Information",
    "نحن هنا لخدمتك والإجابة على جميع استفساراتك": "We are here to serve you and answer all your questions",
    "العنوان": "Address",
    "الرياض، المملكة العربية السعودية": "Riyadh, Saudi Arabia",
    "حي الملك فهد": "King Fahd District",
    "الهاتف": "Phone",
    "البريد الإلكتروني": "Email",
    "ساعات العمل": "Working Hours",
    "الأحد - الخميس": "Sunday - Thursday",
    "8:00 ص - 5:00 م": "8:00 AM - 5:00 PM",
    "أرسل لنا رسالة": "Send Us a Message",
    "تواصل معنا وسيتم الرد عليك في أسرع وقت": "Contact us and we will respond as soon as possible",
    "إرسال الرسالة": "Send Message",
    "خريطة الموقع": "Location Map",
    "خريطة موقع الشركة": "Company Location Map",
    # Reports page
    "سوف يتم الإصدار قريباً": "Coming Soon",
    "عرض التقرير": "View Report",
    "لا توجد تقارير متاحة حالياً": "No reports available at the moment",
    "التقرير السنوي": "Annual Report",
    "تحميل التقرير": "Download Report",
    "جاري تحميل التقرير...": "Loading report...",
    "لا يمكن عرض الملف.": "Cannot display the file.",
    "فتح في نافذة جديدة": "Open in new window",
    "أو": "or",
    # Property Search
    "Search Property": "Search Property",
    "Keyword": "Keyword",
    "Type": "Type",
    "All Type": "All Types",
    "For Rent": "For Rent",
    "For Sale": "For Sale",
    "Open House": "Open House",
    "City": "City",
    "All City": "All Cities",
    "Alabama": "Alabama",
    "Arizona": "Arizona",
    "California": "California",
    "Colorado": "Colorado",
    "Bedrooms": "Bedrooms",
    "Any": "Any",
    "Garages": "Garages",
    "Bathrooms": "Bathrooms",
    "Min Price": "Minimum Price",
    "Unlimited": "Unlimited",
    # Form fields
    "الاسم": "Name",
    "البريد الإلكتروني": "Email",
    "الموضوع": "Subject",
    "الرسالة": "Message",
    "رقم الهاتف": "Phone Number",
    # Dashboard
    "لوحة التحكم": "Dashboard",
    "إدارة النظام": "System Management",
    "المستخدمين": "Users",
    "الإعدادات": "Settings",
    "تسجيل الخروج": "Logout",
    "تسجيل الدخول": "Login",
    # Chatbot
    "روبوت المحادثة": "Chatbot",
    "الأسئلة الشائعة": "FAQ",
    "السؤال": "Question",
    "الجواب": "Answer",
    "تفاصيل السؤال": "Question Details",
    "تفاصيل السؤال والجواب": "Question and Answer Details",
    "الكلمات المفتاحية": "Keywords",
    "الفئة": "Category",
    "الترتيب": "Order",
    "الحالة": "Status",
    "نشط": "Active",
    "غير نشط": "Inactive",
    "عدد المشاهدات": "View Count",
    "تاريخ الإنشاء": "Created At",
    "آخر تحديث": "Last Updated",
    "العودة للقائمة": "Back to List",
    "عام": "General",
    # Status
    "تم بنجاح": "Successful",
    "فشل": "Failed",
    "قيد المعالجة": "Processing",
    # Company info
    "ثمار القابضة": "Thimar Holding",
    "وصف الموقع": "Site Description",
    "كلمات مفتاحية": "Keywords",
    # Common phrases
    "استراتيجيتنا": "Our Strategy",
    "النمو والتوسع": "Growth and Expansion",
    "التنوع": "Diversity",
    "الحوكمة والشفافية": "Governance and Transparency",
    "سنة من الخبرة": "Years of Experience",
    "مشروع منجز": "Projects Completed",
    "عميل راضٍ": "Satisfied Clients",
    "جائزة محلية ودولية": "Local and International Awards",
    # Language
    "Arabic": "Arabic",
    "English": "English",
    "العربية": "Arabic",
    "الإنجليزية": "English",
}


def translate_po_file(po_file_path):
    """Add English translations to the .po file"""
    print(f"Reading {po_file_path}...")

    with open(po_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Track translations
    translated_count = 0

    # For each translation in our dictionary
    for arabic, english in TRANSLATIONS.items():
        # Find msgid entries with empty msgstr
        pattern = rf'(msgid "{re.escape(arabic)}"\nmsgstr )""'

        if re.search(pattern, content):
            content = re.sub(pattern, rf'\1"{english}"', content)
            translated_count += 1
            print(f"✓ Translated: {arabic} -> {english}")

    # Write back
    with open(po_file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Added {translated_count} English translations!")
    print(f"📝 File updated: {po_file_path}")
    print("\n🔄 Now run: python manage.py compilemessages")


if __name__ == "__main__":
    po_file = r"locale\en\LC_MESSAGES\django.po"
    translate_po_file(po_file)
