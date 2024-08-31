from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню
main_menu_inline = InlineKeyboardMarkup(row_width=2)
main_menu_inline.add(
    InlineKeyboardButton('👤 Профиль', callback_data='profile'),
    InlineKeyboardButton('🔄 Обмен', callback_data='exchange'),
    InlineKeyboardButton('📊 Статистика', callback_data='statistics'),
    InlineKeyboardButton('⚙️ Настройки', callback_data='settings'),
)
main_menu_inline.add(
    InlineKeyboardButton('ℹ️ ЧаВо', callback_data='faq'),
    InlineKeyboardButton('👁‍🗨 Поддержка', url='https://t.me/support_link')
)

# Меню обмена
exchange_menu_inline = InlineKeyboardMarkup(row_width=2)
exchange_menu_inline.add(
    InlineKeyboardButton('💵 Фиат на крипту', callback_data='fiat_to_crypto'),
    InlineKeyboardButton('🔐 Крипту на фиат', callback_data='crypto_to_fiat')
)
exchange_menu_inline.add(
    InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu')
)

# Меню статистики
stat_menu_inline = InlineKeyboardMarkup(row_width=2)
stat_menu_inline.add(
    InlineKeyboardButton('🕐 За день', callback_data='time_day'),
    InlineKeyboardButton('🗓 За неделю', callback_data='time_week'),
    InlineKeyboardButton('📆 За месяц', callback_data='time_month')
)
stat_menu_inline.add(
    InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu')
)

# Админ-панель
admin_panel_inline = InlineKeyboardMarkup(row_width=2)
admin_panel_inline.add(
    InlineKeyboardButton('➕ Добавить фиат', callback_data='add_fiat'),
    InlineKeyboardButton('➕ Добавить крипту', callback_data='add_crypto'),
    InlineKeyboardButton('➖ Удалить фиат', callback_data='delete_fiat'),
    InlineKeyboardButton('➖ Удалить крипту', callback_data='delete_crypto')
)
admin_panel_inline.add(
    InlineKeyboardButton('📊 Статистика', callback_data='statistic'),
    InlineKeyboardButton('📣 Рассылка', callback_data='aspam')
)
admin_panel_inline.add(
    InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu')
)

# Пример функции для генерации меню с каналами
def channel_list(channels):
    channel_menu = InlineKeyboardMarkup(row_width=1)
    for channel in channels:
        channel_menu.add(InlineKeyboardButton('➕ Канал', url=channel))
    channel_menu.add(InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu'))
    return channel_menu

# Меню управления статусом бота
def status_bot(status):
    status_key = InlineKeyboardMarkup(row_width=1)
    if status == 'on':
        status_key.add(InlineKeyboardButton('🔴 Выключить', callback_data='sbot_off'))
    else:
        status_key.add(InlineKeyboardButton('🟢 Включить', callback_data='sbot_on'))
    status_key.add(InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu'))
    return status_key

# Закрытие
close_key = InlineKeyboardMarkup(row_width=1)
close_key.add(InlineKeyboardButton('✖️ Закрыть', callback_data='close'))

# Поддержка
support_key = InlineKeyboardMarkup(row_width=1)
support_key.add(
    InlineKeyboardButton('👁‍🗨 Поддержка', url='https://t.me/support_link'),
    InlineKeyboardButton('✖️ Закрыть', callback_data='close')
)

# Пример меню для удаления валют
def delete_valute_menu(valute_list):
    delete_valute = InlineKeyboardMarkup(row_width=1)
    for valute in valute_list:
        delete_valute.add(InlineKeyboardButton(f'{valute[0]}', callback_data=f'vdelete_{valute[0]}'))
    delete_valute.add(InlineKeyboardButton('🔙 Назад в меню', callback_data='back_to_menu'))
    return delete_valute

# Пример меню подтверждения обмена
def confirm_exchange(id, exchange, amount):
    confirm_key = InlineKeyboardMarkup(row_width=1)
    confirm_key.add(
        InlineKeyboardButton('✅ Закончить обмен', callback_data=f'confirm_good_{id}_{amount}_{exchange}'),
        InlineKeyboardButton('❌ Отменить обмен', callback_data=f'confirm_false_{id}_{amount}_{exchange}')
    )
    return confirm_key
