from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls._pluralize(cls._camel_case_to_snake_case(cls.__name__))}"

    @staticmethod
    def _camel_case_to_snake_case(input_str: str) -> str:
        chars = []
        for c_idx, char in enumerate(input_str):
            if c_idx and char.isupper():
                nxt_idx = c_idx + 1
                flag = nxt_idx >= len(input_str) or input_str[nxt_idx].isupper()
                prev_char = input_str[c_idx - 1]
                if prev_char.isupper() and flag:
                    pass
                else:
                    chars.append("_")
            chars.append(char.lower())
        return "".join(chars)

    @staticmethod
    def _pluralize(word: str) -> str:
        if word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
            return word[:-1] + "ies"  # Например, 'city' -> 'cities'
        elif (
            word.endswith("s") or word.endswith("x") or word.endswith("z") or word.endswith("ch") or word.endswith("sh")
        ):
            return word + "es"  # Например, 'bus' -> 'buses', 'box' -> 'boxes'
        else:
            return word + "s"  # Например, 'car' -> 'cars'
