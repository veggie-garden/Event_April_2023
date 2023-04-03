#include <stdio.h>
#include <ctype.h>

int	blackjack(char *str, int *A)
{
	int	res = 0;
	int	num = 0;

	while (*str)
	{
		num = *str - 48;
		if (*str == 'A')
			(*A)++;
		else if (*str == 'J' || *str == 'Q' || *str == 'K' || *str == 'D')
			res += 10;
		else if (isdigit(*str) && num >= 2 && num <= 9)
			res += num;
		else
			return (-1);
		str++;
	}
	return (res);
}

int	count(int res, int A)
{
	while (A)
	{
		if (res + A * 11 <= 21)
			return (res + A * 11);
		if (res + 11 < 21)
			res += 11;
		else
			res += 1;
		A--;
	}
	return (res);
}

int	main(int argc, char **argv)
{
	int	A = 0;
	int	res;
	int	ret;

	if (argc != 2)
		return (1);
	res = blackjack(argv[1], &A);
	if (res == -1)
		return (1);
	ret = count(res, A);
	if (ret == 21)
		printf("Blackjack!\n");
	else
		printf("%d\n", ret);
	return (0);
}
