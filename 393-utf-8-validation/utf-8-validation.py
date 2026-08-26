class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        remaining = 0

        for num in data:
            # Use only the last 8 bits
            num = num & 255

            if remaining == 0:
                # 1-byte character
                if (num >> 7) == 0:
                    continue

                # 2-byte character
                elif (num >> 5) == 0b110:
                    remaining = 1

                # 3-byte character
                elif (num >> 4) == 0b1110:
                    remaining = 2

                # 4-byte character
                elif (num >> 3) == 0b11110:
                    remaining = 3

                else:
                    return False

            else:
                # Continuation byte must start with 10
                if (num >> 6) != 0b10:
                    return False

                remaining -= 1

        return remaining == 0