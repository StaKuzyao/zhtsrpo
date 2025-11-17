import os
import shutil

# Маппинг старых имен на новые
folder_mapping = {
    "Диаграммы компонентов": "component_diagrams",
    "Диаграммы классов": "class_diagrams",
    "Диаграмму активностей": "activity_diagrams",
    "Диаграмма развертывания": "deployment_diagram",
    "Диаграммы состояния": "state_diagrams",
    "Диаграммы прецедентов": "use_case_diagrams",
    "Диаграммы последовательностей": "sequence_diagrams",
}

# Маппинг файлов
file_mapping = {
    # component_diagrams
    "маршруты аккаунтов.png": "account_routes.png",
    "маршруты викторины.png": "quiz_routes.png",
    "маршруты магазина.png": "store_routes.png",
    "основные маршруты.png": "main_routes.png",
    
    # class_diagrams
    "модели Game, Category, Purchase, RouletteGame, RouletteSpin, RouletteAttempt.png": "models_game_category_purchase_roulette.png",
    "модели Question, Streak.png": "models_question_streak.png",
    "модели User, SavedCard.png": "models_user_savedcard.png",
    
    # activity_diagrams
    "процесс викторины.png": "quiz_process.png",
    "процессы покупки, рулетки, просмотра каталога.png": "purchase_roulette_catalog_processes.png",
    "регистрация, пополнение баланса.png": "registration_balance_topup.png",
    
    # deployment_diagram
    "WSGI конфигурация.png": "wsgi_configuration.png",
    "точка входа Django.png": "django_entry_point.png",
    
    # state_diagrams
    "состояния игр, рулетки, попыток.png": "game_roulette_attempt_states.png",
    "состояния пользователей и карт.png": "user_card_states.png",
    "состояния серий в викторине.png": "quiz_streak_states.png",
    
    # use_case_diagrams
    "викторина.png": "quiz_use_case.png",
    "главная страница.png": "main_page_use_case.png",
    "детали игры.png": "game_details_use_case.png",
    "каталог игр.png": "game_catalog_use_case.png",
    "рулетка.png": "roulette_use_case.png",
    
    # sequence_diagrams
    "процессы покупки, рулетки.png": "purchase_roulette_sequence.png",
}

docs_dir = os.path.join(os.getcwd(), "docs")

# Переименовываем папки
for old_name, new_name in folder_mapping.items():
    old_path = os.path.join(docs_dir, old_name)
    new_path = os.path.join(docs_dir, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed folder: {old_name} -> {new_name}")

# Переименовываем файлы в каждой папке
for folder_name in os.listdir(docs_dir):
    folder_path = os.path.join(docs_dir, folder_name)
    if os.path.isdir(folder_path):
        for old_file_name, new_file_name in file_mapping.items():
            old_file_path = os.path.join(folder_path, old_file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
                print(f"Renamed file: {old_file_name} -> {new_file_name}")

print("Renaming completed!")

