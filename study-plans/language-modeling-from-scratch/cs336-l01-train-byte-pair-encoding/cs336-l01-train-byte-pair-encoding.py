
def train_bpe(corpus: list[str], vocab_size: int) -> dict:
    tokens_to_add = vocab_size - 256
    vocab = []
    merges = []

    words_byte_vals = []
    token_bytes = {i: (i,) for i in range(256)}

    for word in corpus:
        words_byte_vals.append(get_byte_vals_of_word(word))

    for i in range(tokens_to_add):
        most_common_pair = get_most_common_pair(
            words_byte_vals, token_bytes
        )

        if most_common_pair is None:
            break

        left, right = most_common_pair
        new_token_id = 256 + i

        token_bytes[new_token_id] = merge_into_pair(
            token_bytes[left], token_bytes[right]
        )

        vocab.append([
            new_token_id,
            list(token_bytes[new_token_id])
        ])

        merges.append([left, right, new_token_id])

        new_word_byte_vals = []

        for byte_vals in words_byte_vals:
            new_byte_vals = []
            j = 0

            while j < len(byte_vals):
                if (
                    j + 1 < len(byte_vals)
                    and (byte_vals[j], byte_vals[j + 1]) == most_common_pair
                ):
                    new_byte_vals.append(new_token_id)
                    j += 2
                else:
                    new_byte_vals.append(byte_vals[j])
                    j += 1

            new_word_byte_vals.append(new_byte_vals)

        words_byte_vals = new_word_byte_vals

    return {"vocab": vocab, "merges": merges}


def get_byte_vals_of_word(word: str) -> list:
    return list(word.encode("utf-8"))


def get_most_common_pair(words_byte_vals, token_bytes):
    byte_pair_count = {}

    for byte_vals in words_byte_vals:
        for i in range(len(byte_vals) - 1):
            pair = (byte_vals[i], byte_vals[i + 1])
            byte_pair_count[pair] = byte_pair_count.get(pair, 0) + 1

    if not byte_pair_count:
        return None

    max_key = max(
        byte_pair_count,
        key=lambda pair: (
            byte_pair_count[pair],
            token_bytes[pair[0]],
            token_bytes[pair[1]]
        )
    )

    return max_key


def merge_into_pair(left, right):
    left_tuple = left if isinstance(left, tuple) else (left,)
    right_tuple = right if isinstance(right, tuple) else (right,)
    return left_tuple + right_tuple
