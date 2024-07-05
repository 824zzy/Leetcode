""" https://leetcode.com/problems/encode-and-decode-tinyurl/
"""


class Codec:
    def __init__(self):
        self.hash = {}
        self.cnt = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cnt += 1
        self.hash[str(self.cnt)] = longUrl
        return "http://tinyurl.com/" + str(self.cnt)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash[shortUrl.split("/")[-1]]
