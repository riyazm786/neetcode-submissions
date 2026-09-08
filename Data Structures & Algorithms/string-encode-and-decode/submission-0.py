class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):

            # Find the '#'
            j = i

            while s[j] != '#':
                j += 1

            # Get the length
            length = int(s[i:j])

            # Move past '#'
            i = j + 1

            # Extract the string
            word = s[i:i + length]
            result.append(word)

            # Move to the next encoded string
            i = i + length

        return result