#include <iostream>
#include <string>
using namespace std;

int digits[10][7] = {
	{ 1, 1, 1, 1, 1, 1, 0 },
	{ 0, 1, 1, 0, 0, 0, 0 },
	{ 1, 1, 0, 1, 1, 0, 1 },
	{ 1, 1, 1, 1, 0, 0, 1 },
	{ 0, 1, 1, 0, 0, 1, 1 },
	{ 1, 0, 1, 1, 0, 1, 1 },
	{ 1, 0, 1, 1, 1, 1, 1 },
	{ 1, 1, 1, 0, 0, 0, 0 },
	{ 1, 1, 1, 1, 1, 1, 1 },
	{ 1, 1, 1, 1, 0, 1, 1 }
};

int input[1000][7];

int main() {
	freopen("input.txt","r",stdin);
	int T;
	cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < 7; j++) {
				char t;
				cin >> t;
				input[i][j] = t - '0';
			}
		}
		string result = "";
		for (int i = 9; i >= 0; i--) {
			if (result == "ERROR!") break;
			int broken[7];
			memset(broken, 0, sizeof(broken));
			int pos = i;
			bool flag = true;
			for (int k = 0; flag && k < n; k++) {
				for (int j = 0; j < 7; j++) {
					if (input[k][j] == 1) {
						if (digits[pos][j] == 1) {
							if (broken[j] == 2) {
								flag = false;
							}
							broken[j] = 1;
						}
						else {
							flag = false;
						}
					}
					else {
						if (digits[pos][j] == 1) {
							if (broken[j] == 1) {
								flag = false;
							}
							broken[j] = 2;
						}
					}
				}
				pos--;
				if (pos < 0) pos = 9;
			}
			if (flag) {
				string temp = "";
				for (int j = 0; j < 7; j++) {
					if (digits[pos][j] == 1) {
						if (broken[j] == 1) {
							temp += '1';
						}
						else if (broken[j] == 2) {
							temp += '0';
						}
						else {
							temp = "ERROR!";
							break;
						}
					}
					else {
						temp += '0';
					}
				}
				if (result != "" && result != temp) {
					result = "ERROR!";
				}
				else {
					result = temp;
				}
			}
		}
		if (result=="") result = "ERROR";
		cout << "Case #" << cas << ": " << result << endl;
	}
}
