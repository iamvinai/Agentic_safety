"""Load SecureDesk settings from the project .env file."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE, override=False)

DEFAULT_GEMINI_MODEL = "gemini-3.6-flash"


@dataclass(frozen=True)
class Settings:
    """Values used by the app."""

    radware_api_key: str | None
    gemini_api_key: str | None
    gemini_model: str = DEFAULT_GEMINI_MODEL
    radware_user_identifier: str = "securedesk-gemini-demo"
    radware_fail_mode: str = "close"
    radware_timeout_s: float = 90.0

    @property
    def live_ready(self) -> bool:
        return bool(self.radware_api_key and self.gemini_api_key)

    @property
    def missing_credentials(self) -> tuple[str, ...]:
        missing: list[str] = []
        if not self.radware_api_key:
            missing.append("RADWARE_OUT_OF_PATH_API_KEY")
        if not self.gemini_api_key:
            missing.append("GOOGLE_API_KEY or GEMINI_API_KEY")
        return tuple(missing)


def get_settings() -> Settings:
    """Read environment variables into Settings."""

    gemini_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    fail_mode = os.getenv("RADWARE_FAIL_MODE", "close").strip().lower()
    if fail_mode not in {"close", "open"}:
        raise ValueError("RADWARE_FAIL_MODE must be 'close' or 'open'")
    timeout_s = float(os.getenv("RADWARE_TIMEOUT_S", "90"))
    if timeout_s <= 0:
        raise ValueError("RADWARE_TIMEOUT_S must be greater than zero")
    return Settings(
        radware_api_key=os.getenv("RADWARE_OUT_OF_PATH_API_KEY") or None,
        gemini_api_key=gemini_key or None,
        gemini_model=os.getenv("GEMINI_MODEL", DEFAULT_GEMINI_MODEL).strip()
        or DEFAULT_GEMINI_MODEL,
        radware_user_identifier=os.getenv(
            "RADWARE_USER_IDENTIFIER", "securedesk-gemini-demo"
        ).strip()
        or "securedesk-gemini-demo",
        radware_fail_mode=fail_mode,
        radware_timeout_s=timeout_s,
    )
