# -*- coding: utf-8 -*-
"""
Management command to add sample chatbot Q&As.
Usage: python manage.py add_chatbot_qas
"""
from django.core.management.base import BaseCommand
from main.models import ChatbotQA


class Command(BaseCommand):
    help = 'Add sample chatbot Q&As to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing chatbot Q&As before adding new ones',
        )

    def handle(self, *args, **options):
        # Clear existing Q&As if requested
        if options['clear']:
            count = ChatbotQA.objects.count()
            ChatbotQA.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f'Deleted {count} existing chatbot Q&As')
            )

        # Define sample Q&As
        sample_qas = [
            {
                'question': 'ما هي شركة ثمار القابضة؟',
                'answer': 'ثمار القابضة هي شركة استثمارية رائدة تأسست في المملكة العربية السعودية. نحن نركز على الاستثمار في قطاعات متنوعة وتقديم حلول استثمارية مبتكرة لعملائنا.',
                'keywords': 'شركة,ثمار,من نحن,عن الشركة,التعريف',
                'category': 'من نحن',
                'order': 1,
                'is_active': True,
            },
            {
                'question': 'ما هي رؤية الشركة؟',
                'answer': 'رؤيتنا هي أن نكون الشركة الاستثمارية الرائدة في المنطقة، ملتزمين بتحقيق أعلى عوائد لمساهمينا وبناء قيمة مستدامة على المدى الطويل.',
                'keywords': 'رؤية,أهداف,استراتيجية,مستقبل',
                'category': 'من نحن',
                'order': 2,
                'is_active': True,
            },
            {
                'question': 'كيف يمكنني الاستثمار مع ثمار؟',
                'answer': 'للاستثمار معنا، يمكنك التواصل مع فريق علاقات المستثمرين عبر صفحة "اتصل بنا" أو زيارة أحد مكاتبنا. سنكون سعداء بتقديم استشارة مجانية لك.',
                'keywords': 'استثمار,كيف,طريقة,بداية,انضمام',
                'category': 'الخدمات',
                'order': 3,
                'is_active': True,
            },
            {
                'question': 'أين يقع مقر الشركة الرئيسي؟',
                'answer': 'يقع مقرنا الرئيسي في مدينة الرياض، المملكة العربية السعودية. يمكنك العثور على تفاصيل العنوان الكامل في صفحة "اتصل بنا".',
                'keywords': 'موقع,عنوان,مقر,مكتب,أين',
                'category': 'معلومات الاتصال',
                'order': 4,
                'is_active': True,
            },
            {
                'question': 'كيف يمكنني التواصل مع خدمة العملاء؟',
                'answer': 'يمكنك التواصل معنا عبر صفحة "اتصل بنا" وملء النموذج، أو الاتصال بنا مباشرة على أرقام الهاتف الموجودة في الموقع، أو عبر البريد الإلكتروني.',
                'keywords': 'تواصل,اتصال,خدمة عملاء,دعم,مساعدة',
                'category': 'معلومات الاتصال',
                'order': 5,
                'is_active': True,
            },
            {
                'question': 'ما هي مجالات استثمار الشركة؟',
                'answer': 'نستثمر في مجموعة متنوعة من القطاعات بما في ذلك العقارات، التقنية، الصناعة، والخدمات. نحرص على تنويع استثماراتنا لتحقيق أفضل العوائد.',
                'keywords': 'مجالات,قطاعات,استثمارات,أنواع,تخصصات',
                'category': 'الخدمات',
                'order': 6,
                'is_active': True,
            },
            {
                'question': 'هل تقدم الشركة وظائف؟',
                'answer': 'نعم، نحن دائماً نبحث عن المواهب المتميزة. يمكنك الاطلاع على الوظائف المتاحة وتقديم طلبك من خلال صفحة "الوظائف" في موقعنا.',
                'keywords': 'وظائف,توظيف,عمل,فرص,مهن,كاريير',
                'category': 'الوظائف',
                'order': 7,
                'is_active': True,
            },
            {
                'question': 'أين يمكنني الاطلاع على التقارير السنوية؟',
                'answer': 'يمكنك الاطلاع على جميع التقارير السنوية ومحاضر الجمعيات العامة في قسم "علاقات المستثمرين" ثم "تقارير مجلس الإدارة".',
                'keywords': 'تقارير,سنوي,محاضر,وثائق,مالية',
                'category': 'علاقات المستثمرين',
                'order': 8,
                'is_active': True,
            },
            {
                'question': 'كيف يمكنني الحصول على القوائم المالية؟',
                'answer': 'القوائم المالية متاحة للجميع في قسم "علاقات المستثمرين" تحت "القوائم المالية". يتم تحديث القوائم بشكل دوري حسب اللوائح.',
                'keywords': 'قوائم مالية,ميزانية,نتائج,أرباح,financial',
                'category': 'علاقات المستثمرين',
                'order': 9,
                'is_active': True,
            },
            {
                'question': 'ما هو البريد الإلكتروني للتواصل؟',
                'answer': 'يمكنك التواصل معنا عبر البريد الإلكتروني الموجود في صفحة "اتصل بنا". نحن نرد على جميع الاستفسارات خلال 24-48 ساعة.',
                'keywords': 'بريد,إيميل,email,contact,تواصل',
                'category': 'معلومات الاتصال',
                'order': 10,
                'is_active': True,
            },
        ]

        created_count = 0
        updated_count = 0

        for qa_data in sample_qas:
            question = qa_data['question']
            
            # Check if Q&A already exists
            existing_qa = ChatbotQA.objects.filter(question=question).first()
            
            if existing_qa:
                # Update existing Q&A
                for key, value in qa_data.items():
                    setattr(existing_qa, key, value)
                existing_qa.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Updated Q&A: {question[:50]}...')
                )
            else:
                # Create new Q&A
                ChatbotQA.objects.create(**qa_data)
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created Q&A: {question[:50]}...')
                )

        # Summary
        self.stdout.write(
            self.style.SUCCESS(
                f'\n--- Summary ---\n'
                f'Created: {created_count}\n'
                f'Updated: {updated_count}\n'
                f'Total Q&As in database: {ChatbotQA.objects.count()}'
            )
        )
