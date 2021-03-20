# TODO: add 62 chars hash solution
class Codec:
    def __init__(self):
        self.hash = {}
        self.cnt = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.cnt += 1
        self.hash[str(self.cnt)] = longUrl
        return "http://tinyurl.com/"+str(self.cnt)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.hash[shortUrl.split('/')[-1]]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))