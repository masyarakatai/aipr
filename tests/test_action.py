"""Keep the composite Action's cache TTL contract aligned with the CLI."""

import re
from pathlib import Path


ACTION_YML = Path(__file__).parent.parent / "action.yml"


def test_action_cache_ttl_uses_cli_seconds_contract():
    """The Action documents and passes AIPR_CACHE_TTL in seconds."""
    action = ACTION_YML.read_text(encoding="utf-8")
    cache_input = re.search(
        r"(?ms)^  cache-ttl:\n(?P<metadata>.*?)(?=^  token:)", action
    )

    assert cache_input, "action.yml must define the cache-ttl input"
    assert "description: 'Cache TTL in seconds (default 86400)'" in cache_input.group(
        "metadata"
    )
    assert "default: '86400'" in cache_input.group("metadata")
    assert "AIPR_CACHE_TTL: ${{ inputs.cache-ttl }}" in action
