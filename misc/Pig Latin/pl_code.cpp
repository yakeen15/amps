// this code inputs a word and translates it into Pig Latin
#include <iostream>
#include <string>

// Irteza Asif - 5 September 2022

using namespace std;

bool vcheck(char x);    // function to check if first letter is vowel or not
void rotate(string& x); // function to shift all letters to the right by 1 cell

int main()
{
    string word, temp, out;
    int i, d;

    cout << "Enter the word:" << endl;
    cin >> word;

    d = word.size();

    if (vcheck(word[0]))
        out = word + "-way";    // if first letter = vowel, add "-way" to word

        else {
            temp = word + "-";
            for(i=0; i<d+1; i++) {  // loop that keeps shifting the word until a vowel comes in the first place
                rotate(temp);
                if (vcheck(temp[0]))
                    break;
            }

            if (i<d)    // if a vowel is found, add "ay", if no vowels in word add "-way"
                out = temp + "ay";
            else
                out = temp + "way";
        }

    cout << "Pig Latin form = " << out << endl;
}

bool vcheck(char x)
{
    switch(x)
    {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
        case 'y':
        case 'A':
        case 'E':
        case 'I':
        case 'O':
        case 'U':
        case 'Y':
            return true;
        default:
            return false;

    }
}

void rotate(string& x)
{
    string ns;
    int d = x.size();

    x = x.substr(1,d) + x[0];
}
