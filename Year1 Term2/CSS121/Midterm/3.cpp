#include <iostream>
#include <stack>

using namespace std;

class Queue {
    private:
        stack<int> stack1;
        stack<int> stack2;

    public:
        void enqueue(int item) {
            stack1.push(item);
        }

        int dequeue() {
            if (stack1.empty() && stack2.empty()) {
                throw runtime_error("Queue is empty");
            }
            if (stack2.empty()) {
                while (!stack1.empty()) {
                    stack2.push(stack1.top());
                    stack1.pop();
                }
            }
            int item = stack2.top();
            stack2.pop();
            return item;
        }
};

int main() {
    Queue q;
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    cout << q.dequeue() << endl; // Output: 1
    cout << q.dequeue() << endl; // Output: 2
    q.enqueue(4);
    cout << q.dequeue() << endl; // Output: 3
    cout << q.dequeue() << endl; // Output: 4
    return 0;
}