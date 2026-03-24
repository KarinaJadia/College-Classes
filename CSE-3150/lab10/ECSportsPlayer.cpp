#include "ECSportsPlayer.h"

// ********************************************
// Generic player
bool ECSportsPlayer :: CanPlay(ECTournament &tr) const
{
  return false;
}

// ********************************************
// Ranked player
ECSportsPlayerRanked :: ECSportsPlayerRanked(int r) : rank(r) 
{
}

bool ECSportsPlayerRanked::CanPlay(ECTournament &tr) const
{
  return rank <= tr.GetMinRank();
}

// ********************************************
// Wildcard player: qualify for any tournament 
ECSportsPlayerWildcard :: ECSportsPlayerWildcard(ECSportsPlayer &playerOrig) : ECSportsPlayerDecorator(playerOrig)
{
} 

bool ECSportsPlayerWildcard::CanPlay(ECTournament &tr) const
{
  return true;
}

// ********************************************
// Displined player: cannot attend any tournament during the period of probation
ECSportsPlayerDisciplined::ECSportsPlayerDisciplined(ECSportsPlayer &po, int mStart, int mEnd) : ECSportsPlayerDecorator(po), ms(mStart), me(mEnd)
{
}

bool ECSportsPlayerDisciplined::CanPlay(ECTournament &tr) const
{
  int tm = tr.GetMonth();

  if (tm >= ms && tm <= me)
    return false;

  return player.CanPlay(tr);
}

// ********************************************
// Injured player: cannot attend any tournament during the period of injury(injury occurs at a single month) 
ECSportsPlayerInjured::ECSportsPlayerInjured(ECSportsPlayer &po, int m) : ECSportsPlayerDecorator(po), mInj(m)
{
}

bool ECSportsPlayerInjured::CanPlay(ECTournament &tr) const
{
  if (tr.GetMonth() == mInj)
    return false;

  return player.CanPlay(tr);
}