#include <iostream>
#include <cstdlib>
#include <ctime>


using namespace std;
typedef int Matrice1[7][3];
typedef int Matrice2[3][7];
 /*fontion qui génére un nombre de façon aléatoire*/


/*procédure qui remplie une matrice de 7 lignes et deux colonnes*/

void remplir1(Matrice1 Mat){

    int nombres[21];
    srand(time(0)); // Initialisation du générateur de nombres aléatoires
    for (int i = 0; i < 7; i++)
    {   
        
        for (int j = 0; j < 3; j++)
        {
            Mat[i][j] = rand() % 100;
        } 
    }
}

/*procédure qui affiche les éléments d'une matrice de  7 lignes et 3 colonnes*/

void affiche1(Matrice1 Mat){
        for (int i = 0; i < 7; i++)
    {   
        for (int j = 0; j < 3; j++)
        {
            /*affichage des nombres présent dans la matrice*/
            if (j == 2)
            {     
            cout<<Mat[i][j]<<endl;
            }
            else{
                cout<<Mat[i][j]<<" | " ;
            }
        }
    
    }
}
/*procédure qui affichage les nombres de façon presqu'aléatoire*/
void af(Matrice1 Mat){
    for (int i = 6; i >= 0; i--)
    {   
        for (int j = 0; j < 3; j++)
        {
            /*affichage des nombres présent dans la matrice*/
                cout<<Mat[i][j]<<" | " ;
        }
    
    }
}
/*procédure qui vas placer le  nombre choisi au centre du quatrième tableau*/

void centre(Matrice1 Mat, Matrice2 M1, int nbre, int c){
    if (c == 0)
    {
        /*première colonne différente la colonne du nombre choisi*/
        M1[0][0] = Mat [0][1];
        M1[0][1] = Mat [1][1];
        M1[0][2] = Mat [2][1];
        M1[1][0] = Mat [3][1];
        M1[1][1] = Mat [4][1];
        M1[1][2] = Mat [5][1];
        M1[2][0] = Mat [6][1];
        /* colonne du nombre choisis */
        M1[2][1] = Mat [0][0];
        M1[2][2] = Mat [1][0];
        M1[3][0] = Mat [2][0];
        M1[3][1] = Mat [3][0];
        M1[3][2] = Mat [4][0];
        M1[4][0] = Mat [5][0];
        M1[4][1] = Mat [6][0];
        /*dernière colonne*/
        M1[4][2] = Mat [0][2];
        M1[5][0] = Mat [1][2];
        M1[5][1] = Mat [2][2];
        M1[5][2] = Mat [3][2];
        M1[6][0] = Mat [4][2];
        M1[6][1] = Mat [5][2];
        M1[6][2] = Mat [6][2];

    }

    if (c == 1 )
    {
        /*première colonne différente la colonne du nombre choisi*/
        M1[0][0] = Mat [0][0];
        M1[0][1] = Mat [1][0];
        M1[0][2] = Mat [2][0];
        M1[1][0] = Mat [3][0];
        M1[1][1] = Mat [4][0];
        M1[1][2] = Mat [5][0];
        M1[2][0] = Mat [6][0];
        /* colonne du nombre choisis */
        M1[2][1] = Mat [0][1];
        M1[2][2] = Mat [1][1];
        M1[3][0] = Mat [2][1];
        M1[3][1] = Mat [3][1];
        M1[3][2] = Mat [4][1];
        M1[4][0] = Mat [5][1];
        M1[4][1] = Mat [6][1];
        /*dernière colonne*/
        M1[4][2] = Mat [0][2];
        M1[5][0] = Mat [1][2];
        M1[5][1] = Mat [2][2];
        M1[5][2] = Mat [3][2];
        M1[6][0] = Mat [4][2];
        M1[6][1] = Mat [5][2];
        M1[6][2] = Mat [6][2];
    }
    
    if (c == 2)
    {
        /*première colonne différente la colonne du nombre choisi*/
        M1[0][0] = Mat [0][1];
        M1[0][1] = Mat [1][1];
        M1[0][2] = Mat [2][1];
        M1[1][0] = Mat [3][1];
        M1[1][1] = Mat [4][1];
        M1[1][2] = Mat [5][1];
        M1[2][0] = Mat [6][1];
        /* colonne du nombre choisis */
        M1[2][1] = Mat [0][2];
        M1[2][2] = Mat [1][2];
        M1[3][0] = Mat [2][2];
        M1[3][1] = Mat [3][2];
        M1[3][2] = Mat [4][2];
        M1[4][0] = Mat [5][2];
        M1[4][1] = Mat [6][2];
        /*dernière colonne*/
        M1[4][2] = Mat [0][0];
        M1[5][0] = Mat [1][0];
        M1[5][1] = Mat [2][0];
        M1[5][2] = Mat [3][0];
        M1[6][0] = Mat [4][0];
        M1[6][1] = Mat [5][0];
        M1[6][2] = Mat [6][0];
    }
}
 /*procédure qui inverse un tableau*/
    void inverse (Matrice2 M, Matrice1 M1){
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 7; j++)
            {
                M1[j][i] = M[i][j];
            }
            
        }
        
    }  

    /*fonction qui retourne la colonne d'un nombre donné du tableau*/  
int Colonne(Matrice1 mat, int nbre){
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            if (mat[i][j] == nbre)
            {
                return j;
            }
            
        }
        
    }
    
}
    



int main(){


    int nbre;
    int col, li, c;
    /*création de la première matrice*/
    Matrice1 M;
    /*remplissage de la première matrice*/
    remplir1(M);
    /*affichage de la première matrice*/
    af(M);


    cout<< endl << endl << "veuillez choisir un nombre parmis ces nombres ci dessus" <<endl;
    cin >> nbre;

    cout <<  "Veuillez deviner la colonne où se trouve le nombre que vous venez de choisir"<<endl;
    cin >> col;


    affiche1(M);
    cout<<endl<<endl;
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            if (M[i][j] == nbre)
            {
                c = j;
            }
            
        }
        
    }

    if (c== col){
        cout<<"Bravo vous avez trouvé la colonne où se trouve initialement " << nbre<<endl;
    }
    else{
        cout<<"Désolé, mais vous n'avez pas pu trouver la colonne où se trouve initialement"<< nbre<<endl;
    }

    Matrice2 M1, M2, M3;
    Matrice1 Ma1, Ma2, Ma3;
    /*une fois */
    centre(M, M1, nbre, c);
    inverse(M1, Ma1);

    affiche1(Ma1);
    cout<<endl<<endl;
    /*deux fois*/
     for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            if (Ma1[i][j] == nbre)
            {
                c = j;
            }
            
        }
        
    }
    centre(Ma1, M2, nbre, c);
    inverse(M2, Ma2);
    affiche1(Ma1);
    cout<<endl<<endl;
    /*trois fois*/
     for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 7; j++)
        {
            if (Ma2[i][j] == nbre)
            {
                c = j;
            }
            
        }
        
    }
    
    centre(Ma2, M3, nbre, c);
    inverse(M3, Ma3);

    cout<<"voici le tableau final"<<endl<<endl;
    affiche1(Ma3);


    return 0; 
}
