#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "../../include/board.h"
#include "../../include/player.h"
#include "../../include/card.h"
#include "antimiroir.h"

/*
 * Génère un tableau de n entiers aléatoires entre 1 et max_carte inclus,
 * en utilisant un mélange de Fisher-Yates.
 */
int *melange_carte_1(int n, int max_carte)
{
	if (max_carte <= 0)
	{
		printf("max_carte doit être strictement positif.\n");
		exit(1);
	}

	int *result = malloc(n * sizeof(int));
	if (result == NULL)
	{
		printf("Erreur d'allocation mémoire\n");
		exit(1);
	}

	// Remplissage du tableau avec des entiers aléatoires entre 1 et max_carte
	for (int i = 0; i < n; i++)
	{
		result[i] = rand() % max_carte + 1;
	}

	// Mélange de Fisher-Yates
	for (int i = n - 1; i > 0; i--)
	{
		int j = rand() % (i + 1);
		int temp = result[i];
		result[i] = result[j];
		result[j] = temp;
	}

	return result;
}

/*
 * Fonction simulation
 * Paramètres :
 * - n_round  : nombre de rounds de jeu
 * - num_cartes : nombre de cartes distribuées à chaque joueur (la distribution totale se fait sur tous les joueurs)
 * - max_carte : la valeur maximum d'une carte (les cartes seront comprises entre 1 et max_carte)
 * - strategy : tableau contenant 4 entiers ( 0 ou 1 ) qui déterminent la stratégie de chaque joueuses : 1 pour antimiroir , 0 pour agressif
 */
int *simulation(int n_round, int num_cartes, int max_carte, int *strategy)
{
	// Création et initialisation du plateau de jeu
	board board = create_board();

	// Création des deux équipes
	add_team(board);
	add_team(board);

	// Création et répartition des 4 joueuses
	for (int i = 0; i < 4; i++)
	{
		player p = create_player();
		add_player_to_team(board, i % 2, p);
	}

	// Distribution des cartes générées
	int *cartes = melange_carte_1(num_cartes, max_carte);
	for (int i = 0; i < 4; i++)
	{
		player p = get_player_by_id(i);
		for (int j = 0; j < num_cartes; j++)
		{
			card c = create_card();
			set_value(c, cartes[i * num_cartes + j]);
			add_card_to_hand(p, c);
		}
	}
	free(cartes);

	// Déroulement du jeu
	for (int round = 0; round < n_round; round++)
	{
		for (int i = 0; i < 4; i++)
		{
			player p = get_player_by_id(i);
			int *output;
			if (strategy[i] == 0)
			{
				output = agressif(p);
				set_slate(p, output[0]);
			}
			else
			{
				output = antimiroir(p);
				set_slate(p, output[1]);
			}
			free(output);
		}

		int somme_equipe1 = 0, somme_equipe2 = 0;

		for (int i = 0; i < 4; i++)
		{
			player p = get_player_by_id(i);
			int *output;
			int num_cards;

			if (strategy[i] == 0)
			{
				output = agressif(p);
				num_cards = output[2];
			}
			else
			{
				output = antimiroir(p);
				num_cards = output[3];
			}

			for (int j = 0; j < num_cards; j++)
			{
				card c = get_card_by_id(output[1]);
				play_card(p, c);
				remove_card_from_hand(p, c);

				if (i % 2 == 0)
					somme_equipe1 += get_value(c);
				else
					somme_equipe2 += get_value(c);
			}
			free(output);
		}

		for (int i = 0; i < 4; i++)
		{
			player p = get_player_by_id(i);
			int pari = get_slate(p);
			if (i % 2 == 0)
			{
				if (somme_equipe1 > somme_equipe2 && pari == 1)
					set_score_of_team(board, 0, get_score_of_team(board, 0) + 1);
				else if (somme_equipe1 <= somme_equipe2 && pari == 0)
					set_score_of_team(board, 1, get_score_of_team(board, 1) + 1);
			}
			else
			{
				if (somme_equipe2 > somme_equipe1 && pari == 1)
					set_score_of_team(board, 1, get_score_of_team(board, 1) + 1);
				else if (somme_equipe2 <= somme_equipe1 && pari == 0)
					set_score_of_team(board, 0, get_score_of_team(board, 0) + 1);
			}
		}

		for (int i = 0; i < 4; i++)
		{
			player p = get_player_by_id(i);
			while (get_number_of_played_cards(p) > 0)
			{
				card c = get_played_card(p, 0);
				remove_played_card(p, c);
				add_out_of_game_card(board, c);
			}
		}
	}

	int *result = malloc(2 * sizeof(int));
	if (!result)
	{
		printf("Erreur d'allocation pour le résultat final.\n");
		exit(1);
	}
	result[0] = get_score_of_team(board, 0);
	result[1] = get_score_of_team(board, 1);
	return result;
}

/*
 * Fonction de lancement des expériences : simule plusieurs parties en fonction des stratégies.
 */
void run_experiment(char *filename, int *strategy)
{
	FILE *file = fopen(filename, "w");
	if (!file)
	{
		printf("Erreur d'ouverture du fichier %s\n", filename);
		exit(1);
	}

	for (int max_carte = 2; max_carte <= 5; max_carte++)
	{
		fprintf(file, "# max_carte = %d\n", max_carte);
		fprintf(file, "n_round,victoires_eq1,victoires_eq2,égalité,temps_ms\n");

		for (int n_round = 3; n_round <= 10; n_round++)
		{
			int victories_eq1 = 0;
			int victories_eq2 = 0;
			int egalite = 0;
			double total_time = 0.0;

			for (int i = 0; i < 10; i++)
			{
				clock_t start = clock();
				int *result = simulation(n_round, n_round + (i % 5), max_carte, strategy);
				clock_t end = clock();

				double elapsed = ((double)(end - start)) * 1000.0 / CLOCKS_PER_SEC;
				total_time += elapsed;

				if (result[0] > result[1])
					victories_eq1++;
				else if (result[1] > result[0])
					victories_eq2++;
				else
					egalite++;

				free(result);
			}

			fprintf(file, "%d,%d,%d,%d,%.2f\n", n_round, victories_eq1, victories_eq2, egalite, total_time / 10.0);
		}
		fprintf(file, "\n");
	}

	fclose(file);
}

int main()
{
	// Initialisation unique du générateur de nombres aléatoires
	srand(time(NULL));

	// Stratégie 1 : antimiroir pour le premier joueur uniquement
	int strategy1[4] = {1, 0, 0, 0};
	run_experiment("./experiment_strategy_1.csv", strategy1);

	// Stratégie 2 : deux joueurs antimiroir contre deux agressifs
	int strategy2[4] = {1, 0, 1, 0};
	run_experiment("./experiment_strategy_2.csv", strategy2);

	// Stratégie 3 : 2 joeurs en antimoiroir vs un antimiroir et un agressif
	int strategy3[4] = {1, 1, 1, 0};
	run_experiment("./experiment_strategy_3.csv", strategy3);

	return 0;
}
