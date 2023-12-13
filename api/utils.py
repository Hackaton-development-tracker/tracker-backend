from django.utils import timezone


def format_time_until_available(time_until_available):
    """
    Форматирует время до доступности теста.
    """
    days = time_until_available.days
    hours, remainder = divmod(time_until_available.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if days == 1:
        return f'1 день, {hours} часов, {minutes} минут, {seconds} секунд'
    elif days > 1:
        return f'{days} дней'
    else:
        return f'{hours} часов, {minutes} минут, {seconds} секунд'


def is_test_available_for_user(request, user):
    """
    Проверяет доступность теста для указанного пользователя и возвращает время
    через которое тест снова будет доступен.
    """
    user = request.user

    if (user.next_test_date is not None and
            user.next_test_date > timezone.now()):
        time_until_available = user.next_test_date - timezone.now()
        formatted_time = format_time_until_available(time_until_available)

        return (f'Время прохождения теста еще не наступило. Тест будет '
                f'доступен через {formatted_time}.')
