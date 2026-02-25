#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (s.empty() || words.empty()) return result;

        int wordLen = words[0].length();
        int wordCount = words.size();
        int totalLen = wordLen * wordCount;

        unordered_map<string, int> target;
        for (auto &w : words) target[w]++;

        // Try all possible offsets
        for (int i = 0; i < wordLen; i++) {
            int left = i, right = i;
            unordered_map<string, int> window;
            int count = 0;

            while (right + wordLen <= s.length()) {
                string word = s.substr(right, wordLen);
                right += wordLen;

                // If valid word
                if (target.count(word)) {
                    window[word]++;
                    count++;

                    // If frequency exceeds, shrink window
                    while (window[word] > target[word]) {
                        string leftWord = s.substr(left, wordLen);
                        window[leftWord]--;
                        left += wordLen;
                        count--;
                    }

                    // If valid window found
                    if (count == wordCount) {
                        result.push_back(left);
                    }
                } else {
                    // Reset window
                    window.clear();
                    count = 0;
                    left = right;
                }
            }
        }

        return result;
    }
};