#ifndef _EC_VEHICLE_PARTS_H
#define _EC_VEHICLE_PARTS_H

// Engine type
enum EC_ENGINE_TYPE
{
  EC_ENGINE_4CYL = 0,
  EC_ENGINE_6CYL = 1,
  EC_ENGINE_ELECTRIC = 2
};

// Engine
class ECEngine 
{
public:
  ECEngine(EC_ENGINE_TYPE type );
  // what to put here?
};

// Wheel
class ECWheel 
{
public:
  ECWheel(int size);

};

// light
class ECLight 
{
public:

};

#endif
