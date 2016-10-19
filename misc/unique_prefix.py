END = "__END__"

def make_trie(*words):
    root = {}
    for word in words:
        current_dict = root
        for character in word:
            if character not in current_dict:
                current_dict[character] = {}
            current_dict = current_dict[character]
        current_dict[END] = END
    return root

def unique_prefix(root, word):
    current_dict = root
    for i in xrange(len(word)):
        character = word[i]
        if len(current_dict[character].keys()) == 1:
            return word[:i+1]
        else:
            current_dict = current_dict[character]
    return word

def main():
    A = ['zebra', 'dog', 'dove', 'duck']
    trie = make_trie('zebra', 'dog', 'dove', 'duck')
    print trie
    for word in A:
        print unique_prefix(trie, word),

if __name__ == '__main__':
    main()
