#include <iostream>
#include <vector>


using namespace std;


int get_size_of_lis(const vector<int>&);

vector<int> get_lis(const vector<int>&);

int find_optimal_position(const vector<int>&, const vector<int>&, const int);


int main() {
    vector<int> nums = {1, -1, 3, 2, 5, 4, 10};
    // vector<int> nums = {1, 3, 4, 2, 5};

    int lis_size = get_size_of_lis(nums);
    cout << "1-algo: Longest increasing subsequence size: " << lis_size << "\n";


    vector<int> lis = get_lis(nums);
    cout << "2-algo: Longest increasing subsequence size: " << lis.size() << "\n";
    for (int item : lis) {
        cout << item << " ";
    }
    cout << "\n";


    return 0;
}


int get_size_of_lis(const vector<int>& nums) {
    /**
    *   lis => longest increasing subsequence
    *   
    *   tails[i] - last element of `lis` with size `i`
    */

    int* tails = new int[nums.size()];

    tails[0] = nums[0];
    int lis_len = 1;

    for (int i = 1; i < nums.size(); ++i) {
        auto it = lower_bound(tails, tails+lis_len, nums[i]);

        if (it == tails + lis_len) {
            tails[lis_len++] = nums[i];
        } else {
            tails[it-tails] = nums[i];
        }
    }

    delete [] tails;
    return lis_len;
}


vector<int> get_lis(const vector<int>& nums) {
    /*
        lis - longest increasing subsequence

        nums - list of source elements;

        To find size of longest increasing subsequence:
            - lis_tails_ind[i] - last element of lis with size `i`
                ... num[lis_tails_ind[i-1]] < num[lis_tails_ind[i]] < num[lis_tails_ind[i+1]] ...

                If there is num[j]:
                    ... num[lis_tails_ind[i-1]] < num[j] < num[lis_tails_ind[i+1]] ...
                        and
                    num[j] < num[lis_tails_ind[i]]

                Then can be applied relax operation:
                    lis_tails_ind[i] = j

            If num[j] > last(lis_tails_ind):
                then size of lis can be extended (+1)

        To construct longest increasing subsequence:
            - prevs_ind[i] - index of the element that will be before the element with index `i`
    */
    vector<int> lis_tails_ind;
    vector<int> prevs_ind(nums.size());

    prevs_ind[0] = -1;
    lis_tails_ind.push_back(0);
    int lis_len = 1;

    for (int i = 1; i < nums.size(); ++i) {
        int pos = -1;

        int first_in_lis = nums[lis_tails_ind[0]];
        int last_in_lis = nums[lis_tails_ind[lis_len-1]];
        if (nums[i] > last_in_lis) {
            lis_tails_ind.push_back(i);
            prevs_ind[i] = lis_tails_ind[lis_len-1];
            lis_len++;
        } else if (nums[i] <= first_in_lis) {
            lis_tails_ind[0] = i;
            prevs_ind[i] = -1;
        } else {
            pos = find_optimal_position(nums, lis_tails_ind, nums[i]); 
            lis_tails_ind[pos] = i;
            prevs_ind[i] = lis_tails_ind[pos - 1];
        }
    }

    vector<int> lis(lis_len);
    for (int ind = lis_tails_ind[lis_len-1], i=lis_len-1; ind >= 0; ind = prevs_ind[ind], i--) {
        lis[i] = nums[ind];
    }

    return lis;
}


int find_optimal_position(const vector<int>& nums, const vector<int>& lis_indexes, const int target) {
    /*
        Use binary search to find `target` inside `lis_indexes`

        lis_indexes - indices of the longest increasing subsequence of nums;
        nums        - list of source elements; 
    */
    int ind = 0;

    for (int step = lis_indexes.size()-1; step >= 1; step /= 2) {
        int jump_to = nums[lis_indexes[ind+step]]; 
        while (jump_to <= target) {
            ind += step; jump_to = nums[lis_indexes[ind+step]];
        }
    }

    return ind;
}