#include "calculator.h"
double FtemporCtemp(int mode, double temp) {
	if (mode == 1) return temp * 9 / 5 + 32;
	else if (mode == 2) return (temp - 32) * 5 / 9;
	else throw invalid_argument("类型错误！");
}
//注：兑换功能中汇率为2024/12/15 10:56分时查询
double change(int mode, double money) {
	switch (mode) {
		case 1:
			//#CNY USD
			return money * 0.1375;
		case 2:
			//CNY JPY
			return money * 21.1595;
		case 3:
			//USD CNY
			return money * 7.2731;
		case 4:
			//USD JPY
			return money * 153.653;
		case 5:
			//JPY CNY
			return money * 0.0473;
		case 6:
			//JPY USD
			return money * 0.0065;
		case 7:
			//MOP CNY
			return money * 0.9081;
		case 8:
			//CNY MOP
			return money * 1.1012;
		case 9:
			//HKD CNY
			return money * 0.9351;
		case 10:
			//CNY HKD
			return money * 1.0694;
		case 11:
			//TWD CNY
			return money * 0.223;
		case 12:
			//CNY TWD
			return money * 4.4843;
		case 13:
			//GBP CNY
			return money * 9.1823;
		case 14:
			//CNY GBP
			return money * 0.1089;
		case 15:
			//EUR CNY
			return money * 7.6343;
		case 16:
			//CNY EUR
			return money * 0.1310;
		default:
			throw invalid_argument("类型错误！");
	}
}
pair<double,double> slovefc(string fc, int mode) {
	if (mode == 1) {
		regex pattern("(\d+)x\s*([-+])\s*(\d+)\s*=\s*0");
		smatch result;
		if (regex_match(fc, result, pattern)) {
			int a = stoi(result[1].str());
			char sign_b = result[2].str()[0];
			int b = stoi(result[3].str());
			b = (sign_b == '-') ? -b : b;
			return { (-b / (double)a),INFINITY };
		}
		else {
			throw invalid_argument("方程格式错误，应为ax+b=0的形式（a!=0)");
		}
	}
	else if (mode == 2) {
		regex pattern("(\d+)x\^2\s*([-+])\s*(\d*)x\s*([-+])\s*(\d+)\s*=\s*0");
		smatch result;
		if (regex_match(fc, result, pattern)) {
			int a = stoi(result[1].str());
			char sign_b = result[2].str()[0];
			int b = stoi(result[3].str());
			b = (sign_b == '-') ? -b : b;
			char sign_c = result[4].str()[0];
			int c = stoi(result[5].str());
			c = (sign_c == '-') ? -c : c;
			if (b * b - 4 * a * c < 0) {
				throw;
			}
			else {
				return { (-b + sqrtf(b * b - 4 * a * c)) / (2.0 * a), (-b - sqrtf(b * b - 4 * a * c)) / (2.0 * a) };
			}
		}
	}
	else throw invalid_argument("类型错误！");
}