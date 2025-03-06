#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

class Queue {
private:
    Node* head;
    Node* tail;
    int count;  

public:
    Queue() : head(nullptr), tail(nullptr), count(0) {}

    void enqueue(int value) {
        Node* newNode = new Node(value);
        if (tail == nullptr) {
            head = tail = newNode;  
        } else {
            tail->next = newNode;
            tail = newNode;
        }
        count++;
    }

    void dequeue() {
        if (isEmpty()) {
            cout << "Empty!!" << endl;
            return;
        }
        Node* temp = head;
        head = head->next;
        if (head == nullptr) {
            tail = nullptr;
        }
        delete temp;
        count--;
    }

    int top() {
        if (isEmpty()) {
            cout << "Empty!!" << endl;
            return -1; 
        }
        return head->data;
    }

    bool isEmpty() {
        return head == nullptr;
    }

    int size() {
        return count;
    }

    
};

int main() {
    Queue q;
    q.enqueue(10);
    q.enqueue(20);
    q.enqueue(30);

    cout << "Front element: " << q.top() << endl;
    cout << "Queue size: " << q.size() << endl;

    q.dequeue();
    cout << "Queue size after dequeue: " << q.size() << endl;
    return 0;
}
