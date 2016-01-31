template <class T>
class AddElements {
    public:
        AddElements(T arg) {element=arg;}
        T add(T element2) {
            return element + element2;
        }
        T concatenate(T element2) {
            return element + element2;
        }
    private:
        T element;
};
