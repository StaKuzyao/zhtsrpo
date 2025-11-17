import html
import random
from django.core.management.base import BaseCommand, CommandError
import requests
from quiz.models import Question


API_URL = "https://opentdb.com/api.php"
LIBRE_URL = "https://libretranslate.com/translate"


class Command(BaseCommand):
    help = "Fetch quiz questions from Open Trivia DB and store them in the database"

    def add_arguments(self, parser):
        parser.add_argument("--amount", type=int, default=20, help="How many questions to fetch")
        parser.add_argument("--category", type=str, default="IT", help="Local category name to tag questions")
        parser.add_argument("--translate-ru", action="store_true", help="Translate question and answers to Russian if possible")
        parser.add_argument("--require-ru", action="store_true", help="Skip questions that are not successfully translated to Russian")

    def handle(self, *args, **options):
        amount = options["amount"]
        category = options["category"]
        translate_ru = options["translate_ru"]
        require_ru = options["require_ru"]
        translator = None
        use_libre = False
        if translate_ru:
            try:
                from googletrans import Translator  # type: ignore
                translator = Translator()
            except Exception:
                self.stderr.write("googletrans не установлен, попробую LibreTranslate.")
                use_libre = True
        params = {"amount": amount, "type": "multiple"}
        try:
            resp = requests.get(API_URL, params=params, timeout=20)
            resp.raise_for_status()
        except Exception as exc:
            raise CommandError(f"Failed to fetch questions: {exc}")

        data = resp.json()
        if data.get("response_code") != 0:
            raise CommandError(f"API returned non-zero response_code: {data.get('response_code')}")

        created = 0
        for item in data.get("results", []):
            question_text = html.unescape(item.get("question", "")).strip()
            correct = html.unescape(item.get("correct_answer", "")).strip()
            incorrect = [html.unescape(x).strip() for x in item.get("incorrect_answers", [])]
            if translate_ru:
                if translator:
                    try:
                        question_text = translator.translate(question_text, dest="ru").text
                        correct = translator.translate(correct, dest="ru").text
                        incorrect = [translator.translate(x, dest="ru").text for x in incorrect]
                    except Exception:
                        pass
                elif use_libre:
                    try:
                        def t(txt: str) -> str:
                            if not txt:
                                return txt
                            r = requests.post(LIBRE_URL, data={"q": txt, "source": "en", "target": "ru"}, timeout=20)
                            r.raise_for_status()
                            return r.json().get("translatedText", txt)
                        question_text = t(question_text)
                        correct = t(correct)
                        incorrect = [t(x) for x in incorrect]
                    except Exception:
                        pass
            if require_ru:
                # Отбрасываем вопрос, если он остался латиницей и не содержит кириллицы
                def has_cyr(txt: str) -> bool:
                    return any('а' <= ch.lower() <= 'я' or ch == 'ё' for ch in txt)
                if not (has_cyr(question_text) and has_cyr(correct)):
                    continue
            if not question_text or not correct:
                continue
            obj, was_created = Question.objects.get_or_create(
                text=question_text,
                defaults={"correct_answer": correct, "incorrect_answers": incorrect, "category": category},
            )
            if was_created:
                created += 1

        self.stdout.write(self.style.SUCCESS(f"Questions fetched: {len(data.get('results', []))}, new saved: {created}"))


