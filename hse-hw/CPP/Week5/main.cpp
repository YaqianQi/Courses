#include <iostream>
#include "ringbuf.hpp"

using namespace std;

int main()
{
    cout << "Hello World!" << endl;
    RingBuffer<int> rb(5);
    cout << "size: " << rb.getSize() << endl;
    cout << "cur count: " << rb.getCount() << endl;
    cout << "get free:"<< rb.getFree() << endl;
    cout << "isEmpty: "<< rb.isEmpty() << endl;
    cout << "isFull: "<< rb.isFull() << endl;
    rb.push(1);
    rb.push(2);
    rb.push(3);
    rb.push(4);
    rb.push(5);
    cout << "======= push element ===== "<< endl;
    cout << "front " << rb.front() << endl;
    cout << "back " << rb.back() << endl;
    cout << "size: " << rb.getSize() << endl;
    cout << "cur count: " << rb.getCount() << endl;
    cout << "get free:"<< rb.getFree() << endl;
    cout << "isEmpty: "<< rb.isEmpty() << endl;
    cout << "isFull: "<< rb.isFull() << endl;
    rb.pop();
    cout << "======= after pop ===== " << endl;
    cout << "front " << rb.front() << endl;
    cout << "back " << rb.back() << endl;
    cout << "size: " << rb.getSize() << endl;
    cout << "cur count: " << rb.getCount() << endl;
    cout << "get free:"<< rb.getFree() << endl;
    cout << "isEmpty: "<< rb.isEmpty() << endl;
    cout << "isFull: "<< rb.isFull() << endl;

    RingBuffer<int> rb2(rb);
    cout << "========= copy cb2====== " << endl;
    cout << "front " << rb2.front() << endl;
    cout << "back " << rb2.back() << endl;
    cout << "size: " << rb2.getSize() << endl;
    cout << "cur count: " << rb2.getCount() << endl;
    cout << "get free:"<< rb2.getFree() << endl;
    cout << "isEmpty: "<< rb2.isEmpty() << endl;
    cout << "isFull: "<< rb2.isFull() << endl;
    RingBuffer<int> rb3 = rb;

    return 0;
}
