#ifndef EC_TRANDING_NEWS_H
#define EC_TRANDING_NEWS_H

#include <vector>
#include <algorithm>

class ECTrendingNews;

// Subscriber interface. DON'T CHANGE THIS
class ECSubscriber
{
public:
    virtual ~ECSubscriber() {}
    virtual void Update() = 0;
    virtual int ContractCost() const = 0;
};

// pay-per click subscriber
class ECPayPerClickSubscriber : public ECSubscriber
{
public:
    ECPayPerClickSubscriber(ECTrendingNews &news);
    virtual void Update() override {}
    virtual int ContractCost() const override { return 0; }
};

// contract subscriber
class ECContractSubscriber : public ECSubscriber
{
public:
    ECContractSubscriber(ECTrendingNews &news);
    virtual void Update() override {}
    virtual int ContractCost() const override { return 100; }
};

class ECTrendingNews
{
public:
    ECTrendingNews();
    ~ECTrendingNews();

    void Subscribe(ECSubscriber *pSub);
    void UnSubscribe(ECSubscriber *pSub);

    void Notify();
    void ReceivePayment(int amount);
    int GetTotRevenue() const;

private:
    std::vector<ECSubscriber*> subs;
    int revenue;
};

#endif
