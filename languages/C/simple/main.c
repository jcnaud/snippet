#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int writing_result(int digit, float ratio ){

    FILE* fichier = NULL;
    fichier = fopen("CellValue.txt", "w");

    if (fichier != NULL)
    {
        // Ex: "d:'5', 83.4641%"
        //fputs("d:", fichier)
        fprintf(fichier,"d:'%d', %0.4f%%", digit, ratio);
        
        fclose(fichier); // On ferme le fichier qui a été ouvert
    }else{
        perror("Erreur de création \n");
		return -1;
    }
    return 0;
}

int main(){
    return writing_result(8, 45.2435554543);
}

