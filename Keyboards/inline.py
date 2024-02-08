from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Валюта", callback_data="cur"),
            InlineKeyboardButton(text="Криптовалюта", callback_data="crypto")
        ]
    ]
)

help_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад к списку", callback_data="back")
        ]
    ]
)




currency_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="$ USD (🇺🇸Американский доллар)", callback_data="usd"),
        ],
        [
            InlineKeyboardButton(text="€ EUR (🇪🇺Евро)", callback_data="euro")
        ],
        [
            InlineKeyboardButton(text="฿ THB(🇹🇭Тайский бат)", callback_data="thai")
        ],
        [
            InlineKeyboardButton(text="¥ CNY (🇨🇳Китайский юань)", callback_data="china")
        ],
        [
            InlineKeyboardButton(text="₩ KRW (🇰🇷Южнокорейская вона)", callback_data="korea")
        ],
        [
            InlineKeyboardButton(text="₸ KZT (🇰🇿Казахстанский тенге)", callback_data="kz")
        ],
        [
            InlineKeyboardButton(text="¥ JPY (🇯🇵Японская иена)", callback_data="japan")
        ],
        [
            InlineKeyboardButton(text="🔙В основное меню🔙", callback_data="go_main_menu")
        ]
    ]
)

cryptocurrency_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🟡 Bitcoin", callback_data="btc")
        ],
        [
            InlineKeyboardButton(text="🟡 Ethereum", callback_data="eth")
        ],
        [
            InlineKeyboardButton(text="🟡 Litecoin", callback_data="lite")
        ],
        [
            InlineKeyboardButton(text="🟡 Dogecoin", callback_data="dog")
        ],
        [
            InlineKeyboardButton(text="🟡 Tether", callback_data="tet")
        ],
        [
            InlineKeyboardButton(text="🟡 XRP", callback_data="xrp")
        ],
        [
            InlineKeyboardButton(text="🟡 Binance coin", callback_data="bin")
        ],
        [
            InlineKeyboardButton(text="🔙В основное меню🔙", callback_data="go_main_menu")
        ]
    ]
)