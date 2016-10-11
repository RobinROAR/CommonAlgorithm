#include<vector>
#include<iostream>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i = 0;
        int j = 0;
        for (i=0;i<nums.size();i++){
            if(nums[i] == val){
                continue;
            }
            nums[j] = nums[i];
            j++;
            
        }
        return j;
        
        
    }
};


int main()
{	
	int A[] = {1,2,2,2,3,2,4};
	vector<int> v(A,A+7);
	
	for(int i=0; i<7; i++){
		cout<<v[i];
	}
	cout<<endl;
	Solution S;
	cout<<S.removeElement(v,2);
	for(int i=0; i<7; i++){
		cout<<v[i];
	}
	cout<<endl;
	return 0;
}

