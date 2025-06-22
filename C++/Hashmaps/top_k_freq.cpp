#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        // Step 1: Count frequencies
        for (int num : nums) {
            freq[num]++;
        }

        // Step 2: Use a min-heap (priority queue)
        // Min-heap on frequency: pair<frequency, element>
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> minHeap;

        for (auto& [num, count] : freq) {
            minHeap.push({count, num});
            if (minHeap.size() > k) {
                minHeap.pop(); // Keep only top k frequent
            }
        }

        // Step 3: Extract elements from heap
        vector<int> result;
        while (!minHeap.empty()) {
            result.push_back(minHeap.top().second);
            minHeap.pop();
        }

        return result;
    }

int main() {
    vector<int> nums = {1, 1, 1, 2, 2, 3};
    int k = 2;

    vector<int> topK = topKFrequent(nums, k);

    cout << "Top " << k << " frequent elements: ";
    for (int num : topK) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
