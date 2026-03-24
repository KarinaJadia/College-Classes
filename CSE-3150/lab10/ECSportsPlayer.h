#ifndef _EC_SPORTS_PLAYER_H
#define _EC_SPORTS_PLAYER_H

// ********************************************
// Sports Tournament
class ECTournament
{
public:
  ECTournament(int mon, int mr) : month(mon), minRank(mr) {}
  int GetMonth() const { return month; }
  int GetMinRank() const { return minRank; }

private:
  int month;
  int minRank;
};

// ********************************************
// Generic player
class ECSportsPlayer
{
public:
  virtual ~ECSportsPlayer() {}
  virtual bool CanPlay(ECTournament &tr) const = 0;
};

// ********************************************
// Ranked player
class ECSportsPlayerRanked : public ECSportsPlayer
{
public:
  ECSportsPlayerRanked(int r);
  bool CanPlay(ECTournament &tr) const override;

private:
  int rank;
};

// ********************************************
// Decorator base class
class ECSportsPlayerDecorator : public ECSportsPlayer
{
public:
  ECSportsPlayerDecorator(ECSportsPlayer &p) : player(p) {}
protected:
  ECSportsPlayer &player;
};

// ********************************************
// Wildcard player: qualify for any tournament
class ECSportsPlayerWildcard : public ECSportsPlayerDecorator
{
public:
  ECSportsPlayerWildcard(ECSportsPlayer &playerOrig);
  bool CanPlay(ECTournament &tr) const override;
};

// ********************************************
// Displined player: cannot attend any tournament during the period of probation
class ECSportsPlayerDisciplined : public ECSportsPlayerDecorator
{
public:
  ECSportsPlayerDisciplined(ECSportsPlayer &playerOrig, int mStart, int mEnd);
  bool CanPlay(ECTournament &tr) const override;

private:
  int ms, me;
};

// ********************************************
// Injured player: cannot attend any tournament during the period of injury(injury occurs at a single month) 
class ECSportsPlayerInjured : public ECSportsPlayerDecorator
{
public:
  ECSportsPlayerInjured(ECSportsPlayer &playerOrig, int m);
  bool CanPlay(ECTournament &tr) const override;

private:
  int mInj;
};

#endif
