#include <iostream>
using namespace std;

#ifndef RINGBUF_HPP
#define RINGBUF_HPP

template<typename T>
class RingBuffer{
// stage 1
public:
    RingBuffer(size_t sz);
    ~RingBuffer();
private:
    T* _buf = nullptr;
    size_t _size;
    T* _pTail = nullptr;
    T* _pHead = nullptr;
    bool _empty;
// stage 2
public:
    size_t getSize() const;
    size_t getCount() const;
    size_t getFree() const;
    bool isEmpty() const;
    bool isFull() const;
// stage 3
public:
    void push(const T& value);

// stage 4
public:
    T &front();
    const T& front() const;
    T& back();
    const T& back() const;
// stage 5
public:
    void pop();
// stage 6
public:
    RingBuffer(const RingBuffer& other);
// stage 7
public:
    RingBuffer& operator = (const RingBuffer& rhv);

};

#endif // RINGBUF_HPP

