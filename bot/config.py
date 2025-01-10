from os import environ as env

class Telegram:
    API_ID = int(env.get("API_ID", "26381245"))
    API_HASH = env.get("API_HASH", "aac7ffbd8ad1987df6ef93826c3ef67f")
    BOT_TOKEN = env.get("BOT_TOKEN", "7790050430:AAG8oMKg3DFTNfNcegkCb1gu6bSQDE5SEH0")
    BOT_USERNAME = env.get("BOT_USERNAME", "AskItachiRobot")
    EMOJIS = [
        "👍", "🔥", "🥰",
        "🥶", "👌", "😍",
        "❤‍🔥", "🌚", "💯",
        "👻", "⚡", "👀",
        "🙄", "😇", "🤝",
        "🤗", "😘", "😎"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
