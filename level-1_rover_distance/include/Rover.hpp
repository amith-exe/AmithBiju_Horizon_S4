#pragma once
#include<tuple>
/*
 Decalaration of the function needed for the calculation
             for better structure and reusability of code
*/

class Rover{
public:
    static double calculateDistance(
      std::tuple<double,double>& origin,
      std::tuple<double,double>& destination
    );
     static double calculateTime(
        double distance,
        double initialVelocity,
        double acceleration,
        double maxSpeed
    );
};
