// Problem3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <cstdint>
#include <cassert>
#include <chrono>
#include <algorithm>

using namespace std;

#ifdef _WIN32
#include <Windows.h>

class timer {
public:
    timer() {
        QueryPerformanceFrequency(&_freq);
    }

    void start() {
        QueryPerformanceCounter(&_start);
    }

    void end() {
        QueryPerformanceCounter(&_stop);
    }

    double elapsedTime() {
        LARGE_INTEGER elapsed;
        elapsed.QuadPart = _stop.QuadPart - _start.QuadPart;
        return (double)elapsed.QuadPart / (double)_freq.QuadPart;
    }

private:
    LARGE_INTEGER _freq;
    LARGE_INTEGER _start;
    LARGE_INTEGER _stop;
};

#else

class timer {
public:
    void start() {
        _start = chrono::high_resolution_clock::now();
    }

    void end() {
        _stop = chrono::high_resolution_clock::now();
    }

    double elapsedTime() {
        chrono::duration<double> elapsed = _stop - _start;
        return elapsed.count();
    }

private:
    chrono::time_point<chrono::high_resolution_clock> _start;
    chrono::time_point<chrono::high_resolution_clock> _stop;
};

#endif

bool isPrime(uint64_t num) {
    if(num % 2 == 0 || num % 3 == 0 || num % 5 == 0) {
        return false;
    }

    uint64_t numRoot = (uint64_t)sqrtl((long double)num);

    auto end = numRoot;

    for(size_t i = 5; i <= end; i += 6) {
        if(num % i == 0 || num % (i + 2) == 0) {
            return false;
        }
    }

    return true;
}

uint64_t findLargestFactorSad(uint64_t limit) {
    const uint64_t sqrtLimit = (uint64_t)std::ceil(sqrt((long double)limit));

    uint64_t largestPrimeFactor = 1;
    uint64_t factor;

    for(uint64_t i = 2; i < sqrtLimit; ++i) {
        if(limit % i == 0) {
            factor = limit / i;

            if(isPrime(i)) {
                largestPrimeFactor = i;
            }
        }
    }
    
    return largestPrimeFactor;
}

uint64_t findLargestFactorHappier(uint64_t limit) {
    const uint64_t sqrtLimit = (uint64_t)std::ceil(sqrt((long double)limit));

    uint64_t largestPrimeFactor = 1;
    uint64_t reducedLimit = limit;

    for(uint64_t i = 2; i < sqrtLimit; ++i) {
        if(limit % i == 0) {
            while(reducedLimit % i == 0) {
                largestPrimeFactor = i;
                reducedLimit /= i;
            }

            if(reducedLimit <= i) {
                break;
            }
        }
    }

    return largestPrimeFactor;
}

int main(int argc, char* argv[])
{
    timer totalTimer;

    const uint64_t limit = 600851475143;
    const uint32_t runs = 1000;
    uint64_t largestPrimeFactor = 1;
    
    totalTimer.start();

    for(int i = 0; i < runs; ++i) {
        largestPrimeFactor = findLargestFactorSad(limit);
    }

    totalTimer.end();

    assert(limit % largestPrimeFactor == 0);
    assert(isPrime(largestPrimeFactor));

    cout << "Runtime sad: " << totalTimer.elapsedTime() << " (" << (totalTimer.elapsedTime() / runs) << " avg) sec\n";
    cout << "Largest prime factor is " << largestPrimeFactor << "\n\n";

    totalTimer.start();

    for(int i = 0; i < runs; ++i) {
        largestPrimeFactor = findLargestFactorHappier(limit);
    }

    totalTimer.end();

    assert(limit % largestPrimeFactor == 0);
    assert(isPrime(largestPrimeFactor));

    cout << "Runtime happy: " << totalTimer.elapsedTime() << " (" << (totalTimer.elapsedTime() / runs) << " avg) sec\n";

    cout << "Largest prime factor is " << largestPrimeFactor << "\n";

    system("pause");
	return 0;
}

