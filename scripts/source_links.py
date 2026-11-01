"""Read stored supplementary evidence aliases without fetching or refreshing facts."""
from urllib.parse import urlsplit


def _safe_https_url(value):
    if not isinstance(value, str) or not value:
        return False
    if any(ord(char) <= 32 or ord(char) == 127 for char in value) or '\\' in value:
        return False
    try:
        parsed = urlsplit(value)
        # Accessing port also validates malformed/out-of-range port values.
        parsed.port
        return (parsed.scheme == 'https' and bool(parsed.hostname)
                and parsed.username is None and parsed.password is None)
    except ValueError:
        return False


def supplementary_sources(fact):
    """Keep canonical order; append valid non-image aliases once per section.

    menuImageUrl is deliberately not included. These are stored evidence links,
    not a claim that the external pages are available or were checked again.
    """
    candidates = []
    for key in ('supportingUrls', 'sources'):
        values = fact.get(key)
        if isinstance(values, list):
            candidates.extend(values)
    candidates.append(fact.get('supportingUrl'))
    result = []
    seen = set()
    for value in candidates:
        if _safe_https_url(value) and value not in seen:
            result.append(value)
            seen.add(value)
    return result
