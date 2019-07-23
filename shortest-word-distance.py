class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        distance = len(words)
        index1, index2 = distance, distance

        for i, word in enumerate(words):
            if hash(word) == hash(word1):
                index1 = i
                distance = min(distance, abs(index1 - index2))
            elif hash(word) == hash(word2):
                index2 = i
                distance = min(distance, abs(index1 - index2))
        return distance
