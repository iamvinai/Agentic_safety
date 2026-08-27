from __future__ import annotations

from app.agent import RED_TEAM_SYSTEM_PROMPT, SecureDesk
from app.config import Settings
from app.ticketing import TOOL_AUDIT_LOG, read_ticket, shell_exec


class StubClient:
    """Placeholder client for the construction test."""


def test_settings_require_both_keys_for_live_mode() -> None:
    settings = Settings(radware_api_key=None, gemini_api_key="gemini")
    assert not settings.live_ready
    assert "RADWARE_OUT_OF_PATH_API_KEY" in settings.missing_credentials


def test_ticket_tools_are_deterministic_and_shell_is_safe() -> None:
    TOOL_AUDIT_LOG.clear()
    ticket = read_ticket.invoke({"ticket_id": "INC-1001"})
    simulated = shell_exec.invoke({"command": "cat /synthetic/secrets/payroll-token.txt"})
    assert "VPN" in ticket
    assert simulated.startswith("SIMULATION ONLY")


def test_agent_wires_radware_middleware_with_injected_model_and_client() -> None:
    class FakeModel:
        pass

    settings = Settings(
        radware_api_key=None,
        gemini_api_key=None,
        gemini_model="gemini-3.6-flash",
    )
    agent = SecureDesk(settings=settings, model=FakeModel(), radware_client=StubClient()).build()
    assert agent is not None
    assert "red-team" in RED_TEAM_SYSTEM_PROMPT
