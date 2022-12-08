#include <iostream>
#include <string>
#include <ctime>

using namespace std;

enum muv{ROCK, PAPER, SCISSORS, null} user_turn, cpu_turn;

// prototypes
string printE(muv x);
void user_move(muv& user_turn);
void cpu_move(muv& cpu_turn);
int point_det(muv user, muv cpu, int r);

int main ()
{
    int i=1, userP=0, cpuP=0, r;

    cout << "Game of Rock-Paper-Scissors (Best of 5)" << endl;

    do {
        cout << "\n\nROUND " << i << endl; // prints round number

        // reads user turn and displays
        user_move(user_turn);
        if (user_turn != 3)
            cout << "Your move = " << printE(user_turn) << endl;
        else
            continue;

        // generates cpu turn and displays
        cpu_move(cpu_turn);
        cout << "My move = " << printE(cpu_turn) << endl;

        // checks who won the round
        switch (point_det(user_turn, cpu_turn, r))
        {
        case 1:
            userP++;
            cout << "\nYOU WIN" << endl;
            break;
        case -1:
            cpuP++;
            cout << "\nI WIN" << endl;
            break;
        case 0:
            cout << "\nTIE" << endl;
        }

        // prints the points at the end of every turn
        cout << "\nPOINTS:  You = " << userP << ", Me = " << cpuP << endl;

        i++;
    }
    while(userP<3 && cpuP<3);   // exits loop if one has >=3 points

    if(userP>cpuP)
        cout << "\nJITSOS MAMA. GGWP" << endl;
    else
        cout << "\nHARSOS BOLOD KHELA PAROS NA NAKI KIRE?" << endl;

    return 0;
}

void user_move(muv& user_turn) // function that reads user move as enum type
{
    char x;
    cout << "\nType in your move (the first letter only):" << endl;
    cin >> x;

    switch(x)
    {
    case 'r':
        user_turn = ROCK;
        break;
    case 'p':
        user_turn = PAPER;
        break;
    case 's':
        user_turn = SCISSORS;
        break;
    default :
        user_turn = null;
        cout << "Invalid Input. Type the first letter only." << endl;
    }
}

string printE(muv x) // function that prints corresponding value of the enum type
{
    string y;

    switch(x)
    {
    case 0:
        y = "ROCK";
        return y;
        break;
    case 1:
        y = "PAPER";
        return y;
        break;
    case 2:
        y = "SCISSORS";
        return y;
        break;
    default :
        y = "Invalid Move";
        return y;
    }
}

void cpu_move(muv& cpu_turn) // function that generates a random move for the cpu
{
    srand(time(0)+rand());

    int x;

    x = rand()%3;

    switch(x)
    {
    case 0:
        cpu_turn = ROCK;
        break;
    case 1:
        cpu_turn = PAPER;
        break;
    case 2:
        cpu_turn = SCISSORS;
        break;
    }
}

int point_det(muv user, muv cpu, int r) // function that determines who gets the point for a round
{
    if(user == cpu)
        r=0;
    else if (user==2 && cpu ==0)
        r=-1;
    else if (user==0 && cpu ==2)
        r=1;
    else if (user>cpu)
        r=1;
    else
        r=-1;

    return r;
}
