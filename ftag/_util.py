from __future__ import annotations


def line_col_to_index(text: str, line: int, col: int):
    """TODO: This is slow"""
    lines = text.splitlines(True)  # Keep line breaks
    index = sum(len(lines[i]) for i in range(line - 1)) + col
    return index
