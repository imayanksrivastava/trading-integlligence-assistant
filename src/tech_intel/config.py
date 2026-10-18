"""Application configuration."""

from dataclasses import dataclass
import os

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    """Immutable application settings."""

    openai_api_key: str | None
    log_level: str = "INFO"

    @classmethod
    def from_environment(cls) -> "Settings":
        """Load settings from environment variables."""
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")
        log_level = os.getenv("LOG_LEVEL", "INFO").upper()

        valid_log_levels = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
        if log_level not in valid_log_levels:
            raise ValueError(
                f"Invalid LOG_LEVEL: {log_level}. "
                f"Expected one of {sorted(valid_log_levels)}."
            )

        return cls(
            openai_api_key=api_key,
            log_level=log_level,
        )