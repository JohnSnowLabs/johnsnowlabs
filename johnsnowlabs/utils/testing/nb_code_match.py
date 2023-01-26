from typing import List, Dict


def contains_sub_string(text: str, sub_strings: str) -> bool:
    return any(s in text for s in sub_strings)


def equals_sub_string(text: str, sub_strings: List[str]) -> bool:
    return any(s == text for s in sub_strings)


def replace_on_sub_string_match(
    text: str, sub_string_mapping: Dict[str, str], log=True, log_type="cell"
) -> str:
    # we may have multiple matches, so we keep looping instead of breaking on first match
    for substring_to_check in sub_string_mapping:
        if substring_to_check in text:
            new_text = text.replace(
                substring_to_check, sub_string_mapping[substring_to_check]
            )
            text = new_text
            if log and log_type == "line":
                print(
                    f"[JSL-PREPROCESSOR]: REPLACING <<<{text}>>> with <<<{new_text}>>>"
                )
            if log and log_type == "cell":
                print(
                    f'[JSL-PREPROCESSOR]: REPLACING CELL <<<{text}>>> \nWITH: \n {"=" * 50} \n'
                    f"<<<{new_text}>>>"
                )
    return text


def replace_on_equal_string_match(
    text: str, sub_string_mapping: Dict[str, str], log=True, log_type="cell"
) -> str:
    # we may have multiple matches, so we keep looping instead of breaking on first match
    if text in sub_string_mapping:
        new_text = sub_string_mapping[text]
        if log and log_type == "line":
            print(f"[JSL-PREPROCESSOR]: REPLACING <<<{text}>>> with <<<{new_text}>>>")
        if log and log_type == "cell":
            print(
                f'[JSL-PREPROCESSOR]: REPLACING CELL <<<{text}>>> \nWITH: \n {"=" * 50} \n'
                f"<<<{new_text}>>>"
            )
        text = new_text
    return text
