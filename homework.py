class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def put(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Key must be a string")
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.value = value

    def get(self, key):
        node = self.root
        for char in key:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.value if node.is_end else None

    def has_prefix(self, prefix):
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

class Homework(Trie):
    def count_words_with_suffix(self, pattern) -> int:
        if not isinstance(pattern, str):
            raise ValueError("Pattern must be a string")
        
        def dfs(node, path, results):
            if node.is_end:
                results.append(path)
            for char, child in node.children.items():
                dfs(child, path + char, results)
        
        all_words = []
        dfs(self.root, "", all_words)
        return sum(1 for word in all_words if word.endswith(pattern))

    def has_prefix(self, prefix) -> bool:
        if not isinstance(prefix, str):
            raise ValueError("Prefix must be a string")
        return super().has_prefix(prefix)

class LongestCommonWord(Trie):
    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not all(isinstance(s, str) for s in strings):
            raise ValueError("Input must be a list of strings")
        if not strings:
            return ""

        for i, word in enumerate(strings):
            self.put(word, i)

        prefix = ""
        node = self.root

        while True:
            if len(node.children) != 1 or node.is_end:
                break
            char, next_node = next(iter(node.children.items()))
            prefix += char
            node = next_node

        return prefix

if __name__ == "__main__":
    print("🟩 Додавання слів у Trie:")
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    for i, word in enumerate(words):
        trie.put(word, i)
        print(f"  ➕ Додано слово: {word}")
    # 💾 Screenshot 1: words_inserted.png

    print("\n🟦 Перевірка суфіксів:")
    for suffix in ["e", "ion", "a", "at"]:
        count = trie.count_words_with_suffix(suffix)
        print(f"  🔍 Слів із суфіксом '{suffix}': {count}")
    # 💾 Screenshot 2: suffix_counts.png

    print("\n🟨 Перевірка префіксів:")
    for prefix in ["app", "bat", "ban", "ca"]:
        result = trie.has_prefix(prefix)
        print(f"  🔎 Префікс '{prefix}' знайдено: {result}")
    # 💾 Screenshot 3: prefix_checks.png

    print("\n🟪 Пошук найдовшого спільного префікса:")
    examples = [
        (["flower", "flow", "flight"], "fl"),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["dog", "racecar", "car"], "")
    ]

    for strings, expected in examples:
        trie = LongestCommonWord()
        result = trie.find_longest_common_word(strings)
        print(f"  🧩 У словах {strings} => найдовший префікс: '{result}' (очікувано: '{expected}')")
    # 💾 Screenshot 4: longest_common_prefix.png

    print("\n✅ Усі перевірки завершено.")
    # 💾 Screenshot 5: final_success.png
