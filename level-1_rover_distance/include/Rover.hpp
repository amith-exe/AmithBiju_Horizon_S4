#pragma once
#include<tuple>

class Rover{
public:
    static double calculatingDistance(
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