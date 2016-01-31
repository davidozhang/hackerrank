class LRUCache: public Cache {
public:
    LRUCache(int);
    void set(int, int);
    int get(int);
private:
    void reenqueue(int);
    void enqueue(Node*);
    Node* detach(int key);
};

LRUCache::LRUCache(int capacity) {
    this->head = NULL;
    this->tail = NULL;
    this->cp = capacity;
}

void LRUCache::set(int key, int value) {
    if (mp.count(key)) {
        mp[key]->value = value;
        reenqueue(key);
    } else {
        Node* node = new Node(key, value);
        enqueue(node);
        if (mp.size() > cp) {
            delete detach(tail->key);
        }
    }
}

int LRUCache::get(int key) {
    if (mp.count(key) == 0) {
        return -1;
    } else {
        reenqueue(key);
        return mp[key]->value;
    }
}

void LRUCache::reenqueue(int key) {
    Node* node = detach(key);
    enqueue(node);
}

void LRUCache::enqueue(Node* node) {
    node->prev = NULL;
    node->next = head;
    head = node;

    if (!tail) {
        tail = node;
    }
    mp[node->key] = node;
}

Node* LRUCache::detach(int key) {
    Node* node = mp[key];
    mp.erase(key);

    if (node->prev) {
        node->prev->next = node->next;
    } else {
        head = node->next;
    }

    if (node->next) {
        node->next->prev = node->prev;
    } else {
        tail = node->prev;
    }
    return node;
}
