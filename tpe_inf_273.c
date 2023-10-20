
// BO'O ALBERT 



#include <stdio.h>
#include <stdlib.h>

/* 1-- Création de la structure Etudiant */

struct etudiant
{
    int age;
    double poids;
    double taille;
    char *nom;
};

/*une définition plus courte pour la structure*/

typedef struct etudiant Etudiant;

Etudiant *e;

/*
Cette fonction seras utilisé à la question 6 pour 
supprimer les étudiant ayant plus de 25 ans 

*/
void supp(Etudiant *s, int n){



    for (int i= 0; i < n; i++)
    {

        if (s[i].age > 24)
        {
           for ( int j = i ; j < 4 ; j++)
           {   
            s[j] = s[j+1];
           }
           s = realloc(s, (n-1)*sizeof(Etudiant));
           supp(s, (n-1));           
        }     
    }

}

int main(){


/*2--- Création d'une salle de classe */
    Etudiant *salle;

    /*la taille de la salle*/
    int n; 

    printf("combien d'élèves compte la salle ?? \n");
    scanf("%d", &n);

    salle = malloc(n*sizeof(Etudiant));
/*3---  Remplissage de la salle avec une boucle for     */
 
    for(int i = 0; i<n; i++){

        printf("entrer le nom de l'étudiant %d \n", i+1);
        scanf("%s", &salle[i].nom);
        printf("entrer l'age de l'étudiant %d \n", i+1);
        scanf("%d", &salle[i].age);
        printf("entrer le poids de l'étudiant %d \n", i+1);
        scanf("%lf", &salle[i].poids);
        printf("entrer la taille de l'étudiant %d \n", i+1);
        scanf("%lf", &salle[i].taille);
    }


/*4--- Ajout d'un nouvel étudiant dans la salle */
    /*d'abord augmentons la taille de la salle pour pouvoir accueillir le prochain étudiant*/

    salle = realloc( salle, (n+1)*sizeof(Etudiant));

    /*Maintenant on peut procéder à l'ajout du nouvel étudiant*/

    salle[n].nom = "takam";
    salle[n].age = 18;
    salle[n].poids = 45.6;
    salle[n].taille = 1.75;

    /* --- affichons l'ensemble des élèves de la salle */
   
    for (int j = 0; j <= n; j++)
    {
        printf("information de l'étudiant N°%d \n", j+1);
        printf("     NOM: %s \n", salle[j].nom);
        printf("     AGE: %d \n", salle[j].age);
        printf("     POIDS: %f \n", salle[j].poids);
        printf("     TAILLE: %f \n \n ", salle[j].taille );
    }
  


/* 5-- Suppressions de la salle */

    free(salle);
    printf("5) la salle vient d'être supprimé avec la fonction free() \n");
    printf(" \n \n--------- passons à la question bonus ----------------- \n \n");
  
/* 6---- BONUS ------------ */
    // Reprenons la salle de 5 étudiants
    salle = malloc(5*sizeof(Etudiant));
    // remplissons la salle avec à l'interieur 2 étudiants de 25 ans

    // etudiant 1
    salle[0].nom = "donfack";
    salle[0].age = 25;
    salle[0].poids = 55.6;
    salle[0].taille = 1.65;

    // étudiant 2
    salle[1].nom = "famla";
    salle[1].age = 25;
    salle[1].poids = 40;
    salle[1].taille = 1.90;

    //étudiant 3
    salle[2].nom = "toto";
    salle[2].age = 17;
    salle[2].poids = 45.6;
    salle[2].taille = 1.8;

    //étudiant 4
    salle[3].nom = "teumi";
    salle[3].age = 19;
    salle[3].poids = 53;
    salle[3].taille = 1.5;

    //étudiant 5
    salle[4].nom = "tagne";
    salle[4].age = 24;
    salle[4].poids = 45.9;
    salle[4].taille = 1.25;

    // affichage de la classe avant la suppression des élèves ayant plus de 24 ans

    printf("\n6-1)voici à quoi ressemble la nouvelle salle de 5 étudiants \n \n");

    for (int j = 0; j <= 4; j++)
    {
        printf("information de l'étudiant N°%d \n", j+1);
        printf("     NOM: %s \n", salle[j].nom);
        printf("     AGE: %d \n", salle[j].age);
        printf("     POIDS: %f \n", salle[j].poids);
        printf("     TAILLE: %f \n \n ", salle[j].taille );
    }

    // Suppression des élèves ayant plus de 24 ans
    printf(" 6-2)voici à quoi ressemble la salle après la suppression des élèves de plus de 25ans \n \n");

    supp(salle, 5); /*la procédure supp a été définis plus haut et permet de supprimer les deux élèves
                     ayant plus de 25ans tout en redimensionnant la salle à 3 éléments avec la fonction realloc*/
    
    int i;
    // affichage de la salle après le traitement


    for (int j = 0; j < 3; j++)
    {
        printf("information de l'étudiant N°%d \n", j+1);
        printf("     NOM: %s \n", salle[j].nom);
        printf("     AGE: %d \n", salle[j].age);
        printf("     POIDS: %f \n", salle[j].poids);
        printf("     TAILLE: %f \n \n ", salle[j].taille );
    }

}




