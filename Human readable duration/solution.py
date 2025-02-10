#Human-readable duration solution 4kyu
#Please check out the kata on: https://www.codewars.com/kata/52742f58faf5485cae000b9a


def format_duration(sec):
    if sec == 0:
        return "now"

    if sec < 60:
        return f"{sec} second{'s' if sec > 1 else ''}"

    if 60 <= sec < 3600:
        minute = sec // 60
        sec %= 60
        if sec == 0:
            return f"{minute} minute{'s' if minute > 1 else ''}"
        return f"{minute} minute{'s' if minute > 1 else ''} and {sec} second{'s' if sec > 1 else ''}"

    if sec < 86400:
        minute = sec // 60
        hour = minute // 60
        sec %= 60
        minute %= 60
        parts = []

        if hour > 0:
            parts.append(f"{hour} hour{'s' if hour > 1 else ''}")
        if minute > 0:
            parts.append(f"{minute} minute{'s' if minute > 1 else ''}")
        if sec > 0:
            parts.append(f"{sec} second{'s' if sec > 1 else ''}")

        return ", ".join(parts[:-1]) + (" and " + parts[-1] if len(parts) > 1 else parts[0]) if parts else "0 seconds"

    elif sec < 31556926:
        minute = sec // 60
        hour = minute // 60
        days = hour // 24
        sec %= 60
        minute %= 60
        hour %= 24

        parts = []

        if days > 0:
            parts.append(f"{days} day{'s' if days > 1 else ''}")
        if hour > 0:
            parts.append(f"{hour} hour{'s' if hour > 1 else ''}")
        if minute > 0:
            parts.append(f"{minute} minute{'s' if minute > 1 else ''}")
        if sec > 0:
            parts.append(f"{sec} second{'s' if sec > 1 else ''}")

        return ", ".join(parts[:-1]) + (" and " + parts[-1] if len(parts) > 1 else parts[0]) if parts else "0 seconds"
    else:
        minute = sec // 60
        hour = minute // 60
        days = hour // 24
        years = days // 365
        sec %= 60
        minute %= 60
        hour %= 24
        days %= 365  # Keeps only the leftover days after full years

        parts = []
        if years > 0:
            parts.append(f"{years} year{'s' if years > 1 else ''}")
        if days > 0:
            parts.append(f"{days} day{'s' if days > 1 else ''}")
        if hour > 0:
            parts.append(f"{hour} hour{'s' if hour > 1 else ''}")
        if minute > 0:
            parts.append(f"{minute} minute{'s' if minute > 1 else ''}")
        if sec > 0:
            parts.append(f"{sec} second{'s' if sec > 1 else ''}")

        return ", ".join(parts[:-1]) + (" and " + parts[-1] if len(parts) > 1 else parts[0]) if parts else "0 seconds"
print(format_duration(31556926))

