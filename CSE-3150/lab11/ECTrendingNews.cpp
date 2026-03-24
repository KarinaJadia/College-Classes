#include "ECTrendingNews.h"

ECPayPerClickSubscriber::ECPayPerClickSubscriber(ECTrendingNews &news)
{
    news.Subscribe(this);
}

ECContractSubscriber::ECContractSubscriber(ECTrendingNews &news)
{
    news.Subscribe(this);
}

ECTrendingNews::ECTrendingNews() : revenue(0) {}

ECTrendingNews::~ECTrendingNews()
{
    for (auto *p : subs) delete p;
}

void ECTrendingNews::Subscribe(ECSubscriber *pSub)
{
    subs.push_back(pSub);

    int cost = pSub->ContractCost();
    if (cost > 0)
        ReceivePayment(cost);
}

void ECTrendingNews::UnSubscribe(ECSubscriber *pSub)
{
    subs.erase(std::remove(subs.begin(), subs.end(), pSub), subs.end());
}

void ECTrendingNews::Notify()
{
    for (auto *p : subs)
    {
        p->Update();
        if (p->ContractCost() == 0)
            ReceivePayment(1);
    }
}

void ECTrendingNews::ReceivePayment(int amount)
{
    revenue += amount;
}

int ECTrendingNews::GetTotRevenue() const
{
    return revenue;
}
