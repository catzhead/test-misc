#include <iostream>
#include <vector>

#include "vect1.hpp"

int main(void)
{
	Vect1 vect1;
	std::vector<int> input = {0, 1, 2, 3, 4};
	std::vector<int> result = vect1.firsthalf(input);

	for (int i=0; i<result.size(); i++)
	{
		std::cout << result[i] << " - ";
	}
	std::cout << std::endl;

	std::cout << vect1.test(1) << std::endl;

	return 0;
}
