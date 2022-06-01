class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentences = list(map(lambda x: len(x.split()), sentences))
        return max(sentences)