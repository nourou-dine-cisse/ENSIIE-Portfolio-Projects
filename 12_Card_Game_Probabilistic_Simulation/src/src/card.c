#include "../include/card.h"
#include <stdlib.h>
#include <string.h>

// [Ajout - nombre max de cartes]
#define MAX_CARDS 100

static int next_card_id = 0;
static card card_list[MAX_CARDS] = {0};

// [Ajout - champs supplémentaires pour les cartes spéciales]
struct card_
{
    int id;
    int value;

    // === Champs pour carte spéciale ===
    int is_special;    // [Ajout]
    char *name;        // [Ajout]
    char *description; // [Ajout]
    int effect_id;     // [Ajout]
};

// Fonction de création standard
card create_card()
{
    if (next_card_id >= MAX_CARDS)
        return NULL;

    card c = malloc(sizeof(struct card_));
    if (!c)
        return NULL;

    c->id = next_card_id;
    c->value = 0;

    // [Ajout - initialisation carte spéciale]
    c->is_special = 0;
    c->name = NULL;
    c->description = NULL;
    c->effect_id = -1;

    card_list[next_card_id++] = c;
    return c;
}

// Libération mémoire
void free_card(card c)
{
    if (c)
    {
        card_list[c->id] = NULL;

        // [Ajout - libération des champs spéciaux]
        if (c->name)
            free(c->name);
        if (c->description)
            free(c->description);

        free(c);
    }
}

// Fonctions standards
int get_card_id(card c) { return c ? c->id : -1; }
card get_card_by_id(int id) { return (id >= 0 && id < MAX_CARDS) ? card_list[id] : NULL; }
int get_value(card c) { return c ? c->value : 0; }
void set_value(card c, int value)
{
    if (c)
        c->value = value;
}

// === Fonctions cartes spéciales ===

int is_special_card(card c)
{
    return c ? c->is_special : 0; // [Ajout]
}

const char *get_card_name(card c)
{
    return (c && c->is_special && c->name) ? c->name : ""; // [Ajout]
}

const char *get_card_description(card c)
{
    return (c && c->is_special && c->description) ? c->description : ""; // [Ajout]
}

int get_card_effect_id(card c)
{
    return (c && c->is_special) ? c->effect_id : -1; // [Ajout]
}

card create_special_card(const char *name, const char *description, int effect_id)
{
    card c = create_card();
    if (!c)
        return NULL;

    // [Ajout - initialisation carte spéciale]
    c->is_special = 1;
    c->value = 0;
    c->effect_id = effect_id;

    c->name = strdup(name); // [Ajout - allocation dynamique]
    c->description = strdup(description);

    return c;
}
