
/*BO'O ALBERT*/

/*

créons un programme qui permet d'ajouter un nombre dans une pile
dont la structure est implémenté par un simple
l'utilisateur pourra choisir s'il veut ajouter en tête ou en queue
le traitement se fera avec des tableaux

*/



#include <stdio.h>
#include <stdlib.h>



int main(){
    int nbre, var, i, temp=0;

    printf("veuillez entrer la taille initiale de la pile\n");
    scanf("%d", &nbre);

    int tab[nbre];
    int tab2[nbre+1];

    for (i=0; i<nbre; i++){
        printf(" veuillez entrer un entier\n");
        scanf("%d", &tab[i]);
    }
/*affichage de la pile d'entier*/

    printf("voici à quoi ressemble la pile \n \n");
    for ( i = nbre; i > 0; i--)
    {
        printf("%d \n", tab[i-1]);
        printf("---\n");
    }
    
/*ajout d'un élément dans la pile*/
    printf("entrer le nombre à ajouter dans la pile \n");
    scanf("%d", &var);

    printf("pour ajouter en tête de pile taper 1 \n Et pour ajouter en queue taper 2 \n");
    scanf("%d", &temp);
        
    while (temp !=1 && temp != 2)
    {
        printf("vous avez une mauvaise valeur \n");
        printf("pour ajouter en tête de pile taper 1 \n Pour ajouter en queue taper 2 \n");
        scanf("%d", &temp);
        
    }
    
   
    if (temp == 1)
    {
        
        for ( i = 0; i < nbre; i++)
        {
           tab2[i] = tab [i];
        }
        tab2[nbre]= var;
        
        /*affichage de la pile après le traitement */
        printf("voici à quoi ressemble la pile maintenant \n \n");
        for ( i = nbre+1; i > 0; i--)
        {
            printf(" %d \n", tab2[i-1]);
            printf("---\n");
        }

    }

    if (temp == 2)
    {
        tab2[0] = var;
        for ( i = 1; i <= nbre; i++)
        {
            tab2[i] = tab[i-1];
        }
        /*affichage de la pile le traitement*/
        printf("voici à quoi ressemble la pile maintenant \n \n");
        for ( i = nbre+1; i > 0; i--)
        {
            printf("%d \n", tab2[i-1]);
            printf("--- \n");
        }

        
    }

    
    

}
