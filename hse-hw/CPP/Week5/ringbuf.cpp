#include "ringbuf.hpp"
#include <iostream>
using namespace std;

// stage1
template<typename T>
RingBuffer<T>::RingBuffer(size_t sz){
    if(sz <= 0){
        throw std::invalid_argument("Input size is not compatible.");
    }
    _buf = new T[_size];
    _pHead = _buf;
    _pTail = _buf;
    _empty = true;
    _size = sz;
}

template<typename T>
RingBuffer<T>::~RingBuffer()
{
delete [] _buf;
}

// stage2
template<typename T>
size_t RingBuffer<T>::getSize() const{
    return _size;
}

template<typename T>
size_t RingBuffer<T>::getCount() const{
    if(_empty){
        return 0;
    }else if (_pHead == _pTail){
        return _size;
    }else if(_pHead < _pTail){
        return _pTail - _pHead;
    }else{
        return _size - (_pHead - _pTail);
    }
}
template<typename T>
size_t RingBuffer<T>::getFree() const{
    const size_t count = getCount();
    const size_t free = _size - count;
    return free;
}
template<typename T>
bool RingBuffer<T>::isEmpty() const{
    return _empty;

}
template<typename T>
bool RingBuffer<T>::isFull() const{
    const size_t count = getCount();
    return count == _size;
}

// stage 3
template<typename T>
void RingBuffer<T>::push(const T& value){
    if(isFull()){
        throw out_of_range("The queue is full");
    }

    *_pTail = value;
    _pTail++;
    if(_pTail == _buf + _size){
        _pTail = _buf;
    }
    _empty = false;
}

//stage 4
template<typename T>
T& RingBuffer<T>::front(){
    if(isEmpty()){
        throw out_of_range("Ring buffer is empty");
    }
    return *_pHead;
}

template<typename T>
const T& RingBuffer<T>::front() const{
    if(isEmpty()){
        throw out_of_range("Ring buffer is empty");
    }
    return *_pHead;
}

template<typename T>
T& RingBuffer<T>::back(){
    if(isEmpty()){
        throw out_of_range("Ring buffer is empty");
    }
    if(_pTail == _buf){
        return *(_buf + _size - 1);
    }else{
        return *(_pTail - 1);
    }
}

template<typename T>
const T& RingBuffer<T>::back() const{
    if(isEmpty()){
        throw out_of_range("Ring buffer is empty");
    }
    if(_pTail == _buf){
        return *(_buf + _size - 1);
    }else{
        return *(_pTail - 1);
    }
}

// stage 5
template<typename T>
void RingBuffer<T>::pop(){
    if(_empty){
        throw out_of_range("Ring buffer is empty.");
    }
    T& frontVal = *_pHead;
    _pHead++;
    if(_pHead == _buf + _size){
        _pHead = _buf;
    }
    if(_pHead == _pTail){
        _empty = true;
    }
}
// stage 6
template<typename T>
RingBuffer<T>::RingBuffer(const RingBuffer& other){
    _size = other._size;
    _empty = other._empty;
    _buf = new T[_size];
    for (size_t i = 0; i < _size; i++) {
        _buf[i] = other._buf[i];
    }
    _pTail = _buf + (other._pTail - other._buf);
    _pHead = _buf + (other._pHead - other._buf);

}
// stage 7
template<typename T>
RingBuffer<T>& RingBuffer<T>::operator = (const RingBuffer<T>& rhv){
    if(this != &rhv){
        RingBuffer<T> temp(rhv);
        swap(temp);
    }
    return *this;
}
