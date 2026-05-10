#---------- © sᴛᴀʟᴋᴇʀ@hehe_stalker
#---------- ᴘʀᴏJᴇᴄᴛ - ᴛᴇʟᴇɢʀᴀᴍ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛ sᴇʟʟɪɴɢ ʙᴏᴛ
#-------------------------------------------------------

import os
from dotenv import load_dotenv

load_dotenv()


def _getenv(name: str, default: str | None = None, required: bool = False) -> str:
    val = os.getenv(name, default)

    if required and (val is None or val == ""):
        raise RuntimeError(f"Missing required env var: {name}")

    return val


# ================= BASIC CONFIG =================

BOT_TOKEN = _getenv("BOT_TOKEN", required=True)

ADMIN_IDS = [
    int(i)
    for i in _getenv("ADMIN_IDS", "", required=True)
    .replace(" ", "")
    .split(",")
    if i
]

MUST_JOIN_CHANNEL = _getenv("MUST_JOIN_CHANNEL", "-1003738973505")

API_ID = int(_getenv("API_ID", "21377358"))
API_HASH = _getenv("API_HASH", "e05bc1f4f03839db7864a99dbf72d1cd")


# ================= DATABASE =================

DATABASE_URL = _getenv(
    "DATABASE_URL",
    required=True
)

# Compatibility
MONGO_URI = DATABASE_URL


# ================= PAYMENTS =================

OXAPAY_API_KEY = _getenv("OXAPAY_API_KEY", "")


# ================= GMAIL =================

GMAIL_USER = _getenv("GMAIL_USER", "")
GMAIL_PASS = _getenv("GMAIL_PASS", "")


# ================= BOT SETTINGS =================

DEFAULT_CURRENCY = _getenv("DEFAULT_CURRENCY", "₹")

MIN_BALANCE_REQUIRED = float(
    _getenv("MIN_BALANCE_REQUIRED", "0")
)
