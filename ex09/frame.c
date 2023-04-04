#include <stdio.h>

int	max_len(char *str, int *height)
{
	int	cnt = 0;
	int	max = 0;

	while (*str)
	{
		if (*str == ' ')
		{
			if (cnt > max)
				max = cnt;
			cnt = 0;
			(*height)++;
		}
		str++;
		cnt++;
	}
	return (max);
}

int	main(int argc, char **argv)
{
	int	width = 0;
	int	height = 1;
	int	tmp = 0;

	if (argc != 2)
		return (1);
	width = max_len(argv[1], &height) + 4;
	for (int i = 0; i < height + 2; i++)
	{
		if (i == 0 || i == height + 1)
		{
			for (int j = 0; j < width; j++)
				printf("*");
		}
		else
		{
			printf("* ");
			for (int j = 0; j < width - 4; j++)
			{
				printf("%c", argv[1][tmp]?argv[1][tmp]:' ');
				if (argv[1][tmp] && argv[1][tmp] != ' ')
				{
					tmp++;
				}
			}
			tmp++;
			printf(" *");
		}
		printf("\n");
	}
}
