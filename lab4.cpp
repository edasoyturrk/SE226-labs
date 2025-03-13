#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class Stack {
private:
    Node* head;
    int num;
    int capacity;

public:
    Stack(int initialCapacity) {
        head = nullptr;
        num = -1;
        capacity = initialCapacity;
    }

    void push(int x) {
        if (num == capacity - 1) {
            increaseCapacity();
        }
        Node* newNode = new Node();
        newNode->data = x;
        newNode->next = head;
        head = newNode;
        num++;
    }

    int pop() {
    if (isEmpty()) {
        cout << "Empty Stack!" << endl;
        return -1;  
    }
    Node* temp = head;
    int poppedValue = temp->data;
    head = head->next;
    delete temp;
    num--;  
    return poppedValue;  
}
    int peek() {
        if (isEmpty()) {
            cout << "Empty Stack!" << endl;
            return -1;
        }
        return head->data;
    }

    bool isEmpty() {
        return num < 0;
    }

    void increaseCapacity() {
        capacity *= 2;
    }

    bool deleteElement(int val) {
        Node* temp = head;
        Node* prev = nullptr;
        
        while (temp != nullptr) {
            if (temp->data == val) {
                if (prev == nullptr) {
                    head = temp->next;
                } else {
                    prev->next = temp->next;
                }
                delete temp;
                num--;
                return true;
            }
            prev = temp;
            temp = temp->next;
        }
        return false;
    }
};

int main() {
    Stack s(2);
    
    s.push(10);
    s.push(20);
    s.push(30);
    
    cout << "Peek: " << s.peek() << endl; // 30
    
    cout << "Pop: " << s.pop() << endl; // 30
    cout << "Pop: " << s.pop() << endl; // 20
    
    s.push(40);
    cout << "Peek: " << s.peek() << endl; // 40
    
    cout << "Delete 10: " << (s.deleteElement(10) ? "Deleted" : "Not Found") << endl;
    
    cout << "Is Empty: " << (s.isEmpty() ? "Yes" : "No") << endl;
    
    return 0;
}
