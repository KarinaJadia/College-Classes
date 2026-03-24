// implement a task scheduler based on the Singleton pattern
#include <set>

class ECScheduler {
  public:
    static ECScheduler& Instance() {
      static ECScheduler instance;
      return instance;
    }

    void StartTask(int id) {
      runningTasks.insert(id);
    }
    void StopTask(int id) {
      runningTasks.erase(id);
    }
    int GetNumRunTasks() const {
      return static_cast<int>(runningTasks.size());
    }
    
  private:
    ECScheduler() = default;
    ~ECScheduler() = default;
    ECScheduler(const ECScheduler&) = delete;
    ECScheduler& operator=(const ECScheduler&) = delete;
    std::set<int> runningTasks;
};
