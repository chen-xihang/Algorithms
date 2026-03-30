using namespace std;

int boyerMoore (vector<int>& arr){
    int counter = 0;
    int candidate;

    for (int i = 0; i < arr.size(); i++){
        if (counter == 0){
            candidate = arr[i];
        }
        if (arr[i] == candidate){
            counter++;
        } else {
            counter--;
        }
    }
    return candidate;

}

