// implement maze game
#include <vector>

// Room
class Room
{
public:
  virtual ~Room() = default;
  virtual int GetPrize() const { return 1; }
};

// Room with a bomb
class RoomWithBomb : public Room
{
public:
  int GetPrize() const override { return -10; }
};

// Enchanted room 
class EnchantedRoom : public Room
{
public:
  int GetPrize() const override { return 20; }  // Prize = 20
};

// maze game
class MazeGame
{
public:
  MazeGame() {}
  virtual ~MazeGame() {
    for (Room* room : rooms)
        delete room;
  }
  
  // create a maze with two rooms and that is it!
  void CreateMaze()
  {
    rooms.push_back(MakeRoom());
    rooms.push_back(MakeRoom());
  }
  // get the total prize amount for the rooms
  int GetTotPrize() const
  {
    int total = 0;
      for (const Room* room : rooms)
        total += room->GetPrize();
      return total;
  }
  
  virtual Room* MakeRoom() {
    return new Room(); 
  }
  
private:
  std::vector<Room*> rooms;
};

// bombed maze
class BombedMazeGame : public MazeGame
{
public:
  Room* MakeRoom() override {
    return new RoomWithBomb();
  }
};

// enchanted maze
class EnchantedMazeGame : public MazeGame
{
public:
  Room* MakeRoom() override {
    return new EnchantedRoom();
  }
};