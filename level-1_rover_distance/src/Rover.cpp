#include"../include/Rover.hpp"
#include<cmath>

  static double calculatingDistance(
     std::tuple<double,double>& origin,
     std::tuple<double,double>& destination
    ){  //extracting the values from tuple for calculation 
        double x1 = std::get<0>(origin);
        double y1 = std::get<1>(origin);
        double x2 = std::get<0>(destination);
        double y2 = std::get<1>(destination);
     // using distance formula to find the distance  btw the 2 points
        double dx = x2 - x1;
        double dy = y2 - y1;

        return std::sqrt(dx*dx + dy*dy);
    }

      static double calculateTime(
        double distance,
        double initialVelocity,
        double acceleration,
        double maxSpeed
    ){
       // using baisc physics formulas to find the time taken 
        double avgSpeed = (initialVelocity + maxSpeed) / 2;

        return distance / avgSpeed;

    }