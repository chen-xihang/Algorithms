#include <vector>
#include <iostream>

std::vector<int> merge(std::vector<int> left, std::vector<int> right){
    std::vector<int> result;

    int i = 0;
    int j = 0;

    while (i < left.size() && j < right.size()){
        if (left[i] <= right[j]){
            result.push_back(left[i]);
            i++;
        } else {
            result.push_back(right[j]);
            j++;
        }
    }

    while (i < left.size()){
        result.push_back(left[i]);
        i++;
    }

    while (j < right.size()){
        result.push_back(right[j]);
        j++;
    }

    return result;
}


std::vector<int> mergeSort(std::vector<int> arr) 
{
    if (arr.size() <= 1){
        return arr;
    }

    int mid = arr.size()/2;

    std::vector<int> left(arr.begin(), arr.begin() + mid);
    std::vector<int> right(arr.begin() + mid, arr.end());

    std::vector<int> left_sorted = mergeSort(left);
    std::vector<int> right_sorted = mergeSort(right);

    return merge(left_sorted, right_sorted);
}

int main(){
    std::vector<int> arr = {1, -4, 1, 42, 1, -6, 0};

    std::vector<int> sorted = mergeSort(arr);

    for (int x : sorted) {
        std::cout << x << " ";
    }
}