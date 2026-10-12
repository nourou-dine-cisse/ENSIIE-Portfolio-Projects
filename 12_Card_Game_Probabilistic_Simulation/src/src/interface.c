#include <stdio.h>
#include "../include/interface.h"
#include "../include/board.h"
#include "../include/player.h"
#include "../include/card.h"

// Fonction pour afficher le plateau de jeu
void display_board(board b)
{

    printf("\n===== ÉTAT DU JEU =====\n");

    // Affichage des équipes et scores
    int num_teams = get_number_of_teams(b);
    printf("Nombre d'équipes : %d\n", num_teams);

    for (int i = 0; i < num_teams; i++)
    {
        int team_score = get_score_of_team(b, i);
        int num_players = get_number_of_players_in_team(b, i);
        printf("\n--- Équipe %d ---\n", i);
        printf("Score : %d\n", team_score);
        printf("Nombre de joueurs : %d\n", num_players);

        // Affichage des joueurs et de leurs mains
        for (int j = 0; j < num_players; j++)
        {
            player p = get_player(b, i, j);
            int player_id = get_player_id(p);
            int num_cards_in_hand = get_size_of_hand(p);

            printf("\nJoueur %d :\n", player_id);
            printf("Nombre de cartes en main : %d\n", num_cards_in_hand);


            ///////////////// Modifications
            printf("Cartes en main : ");
            for (int k = 0; k < num_cards_in_hand; k++)
            {
                card c = get_card_in_hand(p, k);
                if (is_special_card(c))
                {
                    printf("[SPECIAL: %s] ", get_card_name(c)); // [Ajout - carte spéciale]
                }
                else
                {
                    printf("[%d] ", get_value(c));
                }
            }
            //////////////////


            // Affichage des cartes jouées
            int num_played_cards = get_number_of_played_cards(p);
            printf("Cartes jouées : ");
            for (int k = 0; k < num_played_cards; k++)
            {
                card c = get_played_card(p, k);
                printf("[%d] ", get_value(c));
            }
            printf("\n");

            // Affichage du pari
            int bet = get_slate(p);
            printf("Pari : %d\n", bet);
        }
    }

    printf("\n=========================\n");
}

// Fonction pour demander une mise au joueur
int ask_gamble(player p)
{
    int bet;
    do
    {
        printf("Equipe %d \n", get_player_id(p) % 2);
        printf("Joueur %d, entrez votre mise (1 pour victoire, 0 pour défaite) : ", get_player_id(p));
        scanf("%d", &bet);
        if (bet != 0 && bet != 1)
        {
            printf("Entrée invalide ! Veuillez entrer 1 pour victoire ou 0 pour défaite.\n");
        }
    } while (bet != 0 && bet != 1);

    return bet;
}

// Fonction pour demander le nombre de cartes à jouer
int ask_number_of_played_cards(player p)
{
    int num_cards;
    printf("Equipe %d \n", get_player_id(p) % 2);
    printf("Joueur %d, combien de cartes voulez-vous jouer ? : ", get_player_id(p));
    scanf("%d", &num_cards);
    while (num_cards != 1 && num_cards != 2)
    {
        printf("Veuillez entrer un nombre valide de cartes (1 ou 2) : ");
        scanf("%d", &num_cards);
    }
    return num_cards;
}

// Fonction pour demander au joueur de choisir une carte
card ask_card(player p)
{
    int card_index;
    printf("Equipe %d \n", get_player_id(p) % 2);
    printf("Joueur %d, choisissez une carte à jouer (index) : ", get_player_id(p));
    scanf("%d", &card_index);
    int size = get_size_of_hand(p);
    while (card_index < 0 || card_index >= size)
    {
        printf("Index invalide ! Veuillez choisir une carte entre 0 et %d: ", size - 1);
        scanf("%d", &card_index);
    }
    return get_card_in_hand(p, card_index);
}

// Fonction pour afficher la fin du jeu
void display_end_game(board b)
{
    printf("\n===== FIN DU JEU =====\n");

    if (get_number_of_teams(b) != 2)
    {
        printf("Erreur : Le jeu doit contenir exactement 2 équipes.\n");
        return;
    }

    // Récupérer les scores des deux équipes
    int score_team_0 = get_score_of_team(b, 0);
    int score_team_1 = get_score_of_team(b, 1);

    // Afficher les scores
    printf("Scores finaux :\n");
    printf("  - Équipe 0 : %d points\n", score_team_0);
    printf("  - Équipe 1 : %d points\n", score_team_1);

    // Déterminer l'équipe gagnante
    if (score_team_0 > score_team_1)
    {
        printf("\n🎉 Félicitations à l'équipe 0 qui remporte la partie avec %d points ! 🎉\n", score_team_0);
    }
    else if (score_team_1 > score_team_0)
    {
        printf("\n🎉 Félicitations à l'équipe 1 qui remporte la partie avec %d points ! 🎉\n", score_team_1);
    }
    else
    {
        printf("\n🤝 Match nul ! Les deux équipes ont %d points.\n", score_team_0);
    }
    printf("=========================\n");
}

// Fonction pour afficher un message
void display_message(const char *message)
{
    printf("%s\n", message);
}


// [Ajout - carte spéciale]
int ask_play_special_card(player p)
{
    int choix;
    printf("Joueur %d, souhaitez-vous jouer votre carte spéciale ? (1 = Oui, 0 = Non) : ", get_player_id(p));
    scanf("%d", &choix);
    return choix == 1;
} 


card ask_card_from_out_of_game(board b)
{
    int nb = get_number_of_out_of_game_cards(b);
    printf("Cartes disponibles (hors cartes spéciales) :\n");

    int indices_valides[nb];
    int count = 0;

    for (int i = 0; i < nb; i++)
    {
        card c = get_out_of_game_card(b, i);
        if (!is_special_card(c)) {
            printf("[%d] - Valeur : %d\n", count, get_value(c));
            indices_valides[count++] = i;
        }
    }

    if (count == 0) {
        printf("Aucune carte valide à reprendre.\n");
        return NULL;
    }

    int choix;
    do {
        printf("Entrez l’index de la carte que vous voulez reprendre : ");
        scanf("%d", &choix);
        if (choix < 0 || choix >= count) {
            printf("Index invalide. Réessayez.\n");
        }
    } while (choix < 0 || choix >= count);

    return get_out_of_game_card(b, indices_valides[choix]);
    }


// ===== [Ajout Lot E] : Demande de mise en jetons =====
int ask_token_bet(player p)
{
    int max_tokens = get_tokens(p);
    int bet = 0;

    printf("Equipe %d\n", get_player_id(p) % 2);
    printf("Joueur %d, vous avez %d jetons.\n", get_player_id(p), max_tokens);

    do
    {
        printf("Combien de jetons souhaitez-vous miser ? ");
        scanf("%d", &bet);

        if (bet < 1 || bet > max_tokens)
        {
            printf("⚠️  Mise invalide. Veuillez miser entre 1 et %d jetons.\n", max_tokens);
        }
    } while (bet < 1 || bet > max_tokens);

    return bet;
}
