#include <vector>

#include "vect1.hpp"

std::vector<int> Vect1::firsthalf(const std::vector<int>& vect) {
	return std::vector<int>(vect.begin(), vect.begin() + (vect.size() + 1) / 2);
}
