class Solution {
   public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> grupos;

        for (auto palabra : strs) {
            string copia = palabra;

            sort(copia.begin(), copia.end());

            grupos[copia].push_back(palabra);
        }

        vector<vector<string>> resultados;
        for(auto par : grupos){
            resultados.push_back(par.second);
        }
        return resultados;
    }
};
