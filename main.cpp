#include <iostream>

using namespace std;

int main() {
    int number, reversed = 0, original, remainder;

    cout << "Enter a number: ";
    cin >> number;

    original = number;  // Store the original number

    // Reverse the number
    while (number > 0) {
        remainder = number % 10;
        reversed = reversed * 10 + remainder;
        number /= 10;
    }

    // Check if the original number is equal to its reverse
    if (original == reversed) {
        cout << original << " is a Palindrome." << endl;
    } else {
        cout << original << " is NOT a Palindrome." << endl;
    }

    return 0;
}
