MENU_COMMANDS: dict[str, dict[str, str]] = {
    "RU": {"/start": "Запуск бота",
           "/help": "Справка по работе бота",
           "/beginning": "Перейти в начало книги",
           "/continue": "Продолжить чтение",
           "/bookmarks": "Посмотреть список закладок"},
    "EN": {"/start": "Start bot",
           "/help": "Bot Help",
           "/beginning": "Go to the beginning of the book",
           "/continue": "Continue Reading",
           "/bookmarks": "See list of bookmarks"}
}

BUTTONS_PG: dict[str, dict[str, str]] = {
    "RU": {"forward": ">>",
           "backward": "<<",
           }
}

BUTTONS_BM: dict[str, dict[str, str]] = {
    "RU": {"edit_bookmarks_button": "❌ РЕДАКТИРОВАТЬ",
           "del": "❌",
           "cancel": "ОТМЕНИТЬ"}
}

START: dict[str, str] = {
    "RU": "<b>Привет!</b>\n"
          "\nТут можно почитать книгу!\n"
          "Чтобы посмотреть список команд - нажми /help"
}

HELP: dict[str, str] = {
    "RU": f"<b>Это бот читалка</b>\n"
          f"\nДоступные команды\n"
          f"\nЧтобы сохранить закладку - нажмите на кнопку с номером страницы\n"
          f"\n<b>Приятного чтения!</b>"
}

NOTIFICATIONS: dict[str, dict[str, str]] = {
    "RU": {"no_bookmarks": "У вас пока нет ни одной закладки.\n"
                           "\n"
                           "Чтобы добавить страницу в закладки - во время "
                           "чтения книги нажмите на кнопку с номером этой "
                           "страницы\n"
                           "\n"
                           "/continue - продолжить чтение",
           "cancel_text": "/continue - продолжить чтение",
           "bookmarks": "<b>Это список ваших закладок:</b>",
           "added_bookmarks": "Страница добавлена в закладки!",
           "edit_bookmarks": "<b>Редактировать закладки</b>"}
}
