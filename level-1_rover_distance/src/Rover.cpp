#include "../include/Rover.hpp"
#include <cmath>

// distance calculation
double Rover::calculateDistance(
     std::tuple<double,double>& origin,
     std::tuple<double,double>& destination
){
    // extracting the values from tuple for calculation
    double x1 = std::get<0>(origin);
    double y1 = std::get<1>(origin);
    double x2 = std::get<0>(destination);
    double y2 = std::get<1>(destination);

    // using distance formula to find the distance between the two points
    double dx = x2 - x1;
    double dy = y2 - y1;

    return std::sqrt(dx * dx + dy * dy);
}

double Rover::calculateTime(
    double distance,
    double initialVelocity,
    double acceleration,
    double maxSpeed
){
    /*
       Using the kinematic equation:
       s = ut + 1/2 at^2

       Solving for time
       t = (-u + sqrt(u^2 + 2as)) / a
    */

    // If acceleration is zero, rover moves with constant velocity
    if(acceleration == 0){
        return distance / initialVelocity;
    }

    double time =
        (-initialVelocity +
        std::sqrt(initialVelocity * initialVelocity +
        2 * acceleration * distance)) / acceleration;

    return time;
}