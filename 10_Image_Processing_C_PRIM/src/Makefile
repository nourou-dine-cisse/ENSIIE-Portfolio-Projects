CC = gcc
CFLAGS = -Wall -Wextra

# programme final
CIBLE = programme

# sources et objets
SRC = main.c filename.c picture.c pixels.c lut.c apply_filtre.c
OBJ = $(SRC:.c=.o)

# regle principale
$(CIBLE): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $^

# regle pour chaque fichier
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# nettoyage
clean:
	rm -f $(OBJ) $(CIBLE) 
