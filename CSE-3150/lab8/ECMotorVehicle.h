#ifndef _EC_MOTOR_VEHICLE_H
#define _EC_MOTOR_VEHICLE_H

#include <vector>
#include "ECVehicleParts.h"

// Generic vehicle
class ECMotorVehicle
{
public:
  ECMotorVehicle();
  virtual ~ECMotorVehicle();
  double GetPrice() const;

protected:
  // your code here

private:
  // what to put here?
};

// Car
class ECCar : public ECMotorVehicle
{
public:
  ECCar(EC_ENGINE_TYPE t, int szWheel);

protected:
  // what to put here?
};

// Truck 
class ECTruck : public ECMotorVehicle
{
public:
  ECTruck(int numWheels, int szWheel);

protected:
  // what to put here?
};

// Motocycle
class ECMotocycle : public ECMotorVehicle
{
public:
  ECMotocycle();

protected:
  // what to put here?
};

#endif
