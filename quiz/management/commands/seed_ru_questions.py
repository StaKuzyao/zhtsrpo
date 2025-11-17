from django.core.management.base import BaseCommand
from quiz.models import Question


RUSSIAN_QUESTIONS = [
    {
        "text": "Столица Франции?",
        "correct_answer": "Париж",
        "incorrect_answers": ["Берлин", "Мадрид", "Рим"],
        "category": "Общее",
    },
    {
        "text": "Какой год високосный?",
        "correct_answer": "2024",
        "incorrect_answers": ["2023", "2025", "2026"],
        "category": "Общее",
    },
    {
        "text": "Кто автор романа 'Преступление и наказание'?",
        "correct_answer": "Фёдор Достоевский",
        "incorrect_answers": ["Лев Толстой", "Антон Чехов", "Иван Тургенев"],
        "category": "Литература",
    },
    {
        "text": "Как называется язык программирования, созданный Гвидо ван Россумом?",
        "correct_answer": "Python",
        "incorrect_answers": ["Java", "C++", "Go"],
        "category": "IT",
    },
    {
        "text": "Какой океан самый большой?",
        "correct_answer": "Тихий",
        "incorrect_answers": ["Атлантический", "Индийский", "Северный Ледовитый"],
        "category": "География",
    },
    {
        "text": "Сколько будет 9 × 7?",
        "correct_answer": "63",
        "incorrect_answers": ["56", "72", "54"],
        "category": "Математика",
    },
    {
        "text": "Как называется планета, ближайшая к Солнцу?",
        "correct_answer": "Меркурий",
        "incorrect_answers": ["Венера", "Земля", "Марс"],
        "category": "Астрономия",
    },
    {
        "text": "Кто написал музыку к балету 'Лебединое озеро'?",
        "correct_answer": "Пётр Чайковский",
        "incorrect_answers": ["Сергей Прокофьев", "Модест Мусоргский", "Игорь Стравинский"],
        "category": "Музыка",
    },
    {"text": "Какой элемент обозначается символом 'O'?", "correct_answer": "Кислород", "incorrect_answers": ["Золото", "Олово", "Осмий"], "category": "Химия"},
    {"text": "Сколько континентов на Земле?", "correct_answer": "6", "incorrect_answers": ["5", "7", "4"], "category": "География"},
    {"text": "Как называется самая длинная река в мире?", "correct_answer": "Нил", "incorrect_answers": ["Амазонка", "Янцзы", "Миссисипи"], "category": "География"},
    {"text": "Сколько будет 12 × 12?", "correct_answer": "144", "incorrect_answers": ["124", "154", "132"], "category": "Математика"},
    {"text": "Кто разработал теорию относительности?", "correct_answer": "Альберт Эйнштейн", "incorrect_answers": ["Исаак Ньютон", "Нильс Бор", "Галилео Галилей"], "category": "Наука"},
    {"text": "Какой язык является официальным в Бразилии?", "correct_answer": "Португальский", "incorrect_answers": ["Испанский", "Английский", "Французский"], "category": "География"},
    {"text": "Какой город называют 'северной столицей' России?", "correct_answer": "Санкт‑Петербург", "incorrect_answers": ["Казань", "Новосибирск", "Екатеринбург"], "category": "География"},
    {"text": "Сколько планет в Солнечной системе?", "correct_answer": "8", "incorrect_answers": ["9", "7", "10"], "category": "Астрономия"},
    {"text": "Как называется процесс преобразования воды в пар?", "correct_answer": "Испарение", "incorrect_answers": ["Конденсация", "Замерзание", "Плавление"], "category": "Физика"},
    {"text": "Кто написал 'Евгений Онегин'?", "correct_answer": "Александр Пушкин", "incorrect_answers": ["Михаил Лермонтов", "Николай Гоголь", "Иван Бунин"], "category": "Литература"},
    {"text": "Главный язык разметки в веб‑разработке?", "correct_answer": "HTML", "incorrect_answers": ["CSS", "JavaScript", "XML"], "category": "IT"},
    {"text": "Какой порт по умолчанию использует HTTP?", "correct_answer": "80", "incorrect_answers": ["443", "21", "22"], "category": "IT"},
    {"text": "Какой оператор сравнения в Python проверяет равенство?", "correct_answer": "==", "incorrect_answers": ["=", ":=", "==="], "category": "IT"},
    {"text": "Какая страна самая большая по площади?", "correct_answer": "Россия", "incorrect_answers": ["Канада", "Китай", "США"], "category": "География"},
    {"text": "Какой металл жидкий при комнатной температуре?", "correct_answer": "Ртуть", "incorrect_answers": ["Железо", "Алюминий", "Медь"], "category": "Химия"},
    {"text": "Сколько минут в трёх часах?", "correct_answer": "180", "incorrect_answers": ["120", "160", "200"], "category": "Математика"},
    {"text": "Какой язык программирования используется для стилей веб‑страниц?", "correct_answer": "CSS", "incorrect_answers": ["HTML", "SQL", "Python"], "category": "IT"},
    {"text": "Как называется устройство для вывода изображения на экран?", "correct_answer": "Монитор", "incorrect_answers": ["Клавиатура", "Мышь", "Принтер"], "category": "IT"},
    {"text": "Кто написал роман 'Война и мир'?", "correct_answer": "Лев Толстой", "incorrect_answers": ["Фёдор Достоевский", "Иван Тургенев", "Николай Некрасов"], "category": "Литература"},
    {"text": "Какой город является столицей Японии?", "correct_answer": "Токио", "incorrect_answers": ["Осака", "Киото", "Нагойя"], "category": "География"},
    {"text": "Какая планета известна своими кольцами?", "correct_answer": "Сатурн", "incorrect_answers": ["Юпитер", "Нептун", "Уран"], "category": "Астрономия"},
    {"text": "Кто изобрёл лампу накаливания?", "correct_answer": "Томас Эдисон", "incorrect_answers": ["Никола Тесла", "Александр Белл", "Джеймс Уатт"], "category": "История"},
    {"text": "Какой формат графики поддерживает прозрачность?", "correct_answer": "PNG", "incorrect_answers": ["JPG", "BMP", "TIFF"], "category": "IT"},
    {"text": "Сколько градусов в прямом угле?", "correct_answer": "90", "incorrect_answers": ["45", "60", "120"], "category": "Математика"},
    {"text": "Как называется крупнейший млекопитающий на Земле?", "correct_answer": "Синий кит", "incorrect_answers": ["Африканский слон", "Кашалот", "Белый носорог"], "category": "Биология"},
    {"text": "Что измеряется в герцах (Гц)?", "correct_answer": "Частота", "incorrect_answers": ["Сила тока", "Напряжение", "Сопротивление"], "category": "Физика"},
    {"text": "Какой протокол защищённой версии HTTP?", "correct_answer": "HTTPS", "incorrect_answers": ["FTP", "SSH", "SMTP"], "category": "IT"},
    {"text": "Кто написал пьесу 'Ревизор'?", "correct_answer": "Николай Гоголь", "incorrect_answers": ["Александр Грибоедов", "Александр Пушкин", "Антон Чехов"], "category": "Литература"},
    {"text": "Как называется язык запросов к базам данных?", "correct_answer": "SQL", "incorrect_answers": ["NoSQL", "GraphQL", "LINQ"], "category": "IT"},
    {"text": "Какой орган перекачивает кровь по телу человека?", "correct_answer": "Сердце", "incorrect_answers": ["Лёгкие", "Печень", "Почки"], "category": "Биология"},
    {"text": "Как называется самая высокая гора мира?", "correct_answer": "Эверест", "incorrect_answers": ["Килиманджаро", "Эльбрус", "Монблан"], "category": "География"},
    {"text": "Какая библиотека JavaScript используется для построения интерфейсов?", "correct_answer": "React", "incorrect_answers": ["Django", "Flask", "Laravel"], "category": "IT"},
    {"text": "Кто открыл закон всемирного тяготения?", "correct_answer": "Исаак Ньютон", "incorrect_answers": ["Альберт Эйнштейн", "Галилео Галилей", "Иоганн Кеплер"], "category": "Физика"},
    {"text": "Сколько байт в одном килобайте (в двоичной системе)?", "correct_answer": "1024", "incorrect_answers": ["1000", "512", "2048"], "category": "IT"},
]


class Command(BaseCommand):
    help = "Seed a set of Russian-language quiz questions into the database"

    def handle(self, *args, **options):
        created_count = 0
        for q in RUSSIAN_QUESTIONS:
            obj, created = Question.objects.get_or_create(
                text=q["text"],
                defaults={
                    "correct_answer": q["correct_answer"],
                    "incorrect_answers": q["incorrect_answers"],
                    "category": q.get("category", "Общее"),
                },
            )
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Русские вопросы сохранены: {created_count}"))


