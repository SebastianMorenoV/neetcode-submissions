class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()){
            return false;
        }

        unordered_map<char,int> frecuencias1;
        unordered_map<char,int> frecuencias2;
        for(auto letra : s){
            frecuencias1[letra]++; 
        }
        for(auto letra2: t){
            frecuencias2[letra2]++;
        }

        if(frecuencias1 == frecuencias2){
            return true;
        }

        return false;
       

        
    }
};
