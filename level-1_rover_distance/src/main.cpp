#include <iostream>
#include <tuple>
#include "../include/Rover.hpp"

using namespace std;

int main() {

    // Tuples to store origin and destination coordinates
    tuple<double,double> origin;
    tuple<double,double> destination;


    cout << "Enter origin coordinates (x y): ";
    cin >> get<0>(origin) >> get<1>(origin);

    cout << "Enter destination coordinates (x y): ";
    cin >> get<0>(destination) >> get<1>(destination);

        //error check for invalide inputs , this will check for both input
         if(!cin) {
        cout << "Invalid coordinate input\n";
        return 1;
       }

    // parameters for calculation 
    double v,a,maxSpeed;

    cout << "Enter initial velocity: ";
    cin >> v;

    cout << "Enter acceleration: ";
    cin >> a;

    cout << "Enter maximum speed: ";
    cin >> maxSpeed;
        //basic error chcek
    if(v < 0 || a < 0 || maxSpeed <= 0) {
        cout << "Velocity, acceleration and max speed must be positive\n";
        return 1;
    }
     //calling function to do the calculation
    double distance = Rover::calculateDistance(origin,destination);
    double time = Rover::calculateTime(distance,v,a,maxSpeed);

    

    cout << "\nDistance to destination: " << distance << " meters\n";
    cout << "Time required: " << time << " seconds\n";

    return 0;
}