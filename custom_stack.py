def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Supports (), {}, and [].
    """
    pairs = {")": "(", "}": "{", "]": "["}
    stack = []

    for ch in s:
        # opening bracket -> push
        if ch in pairs.values():
            stack.append(ch)

        # closing bracket -> must match stack top
        elif ch in pairs:
            if not stack:
                return False
            top = stack.pop()
            if top != pairs[ch]:
                return False

        # ignore any other characters (safe)
        else:
            continue

    return len(stack) == 0
