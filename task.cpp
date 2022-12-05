#include <iostream>
#include <cstdlib>

uint64_t f(uint64_t size, uint64_t b, uint64_t c)
{
    uint64_t sum = 0;
    for (uint64_t i = 0; i < size; i++)
    {
        sum += (b * 2 + c - i);
    }
    return sum;
}

// main.exe | size | b | c
int main(int argc, char* argv[])
{
    if (argc != 5) return -1;
    
    volatile uint64_t size = strtoull(argv[1], nullptr, 0);
    uint64_t b             = strtoull(argv[2], nullptr, 0);
    uint64_t c             = strtoull(argv[3], nullptr, 0);
    uint64_t repeat_times  = strtoull(argv[4], nullptr, 0);

    uint64_t s = 0;
    for (int i = 0; i < repeat_times; i++)
        s += f(size, b, c);
    return s;
}