#include<stdio.h>

int main(void){

    int year, weekday, counter;

    counter = 0;
    weekday = 1;

    for (year = 1900; year < 2001; year += 1){
        //Jan || 1 Jan 1900 was Mon. Let Mon be weekday = 1 and Sun be weekday = 7
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Feb || to add leap year logic
        if (year % 4 == 0 && (year % 100) % 4 == 0){
            for (int feb = 1; feb <= 29; feb++){
                if (feb == 1 && weekday == 7){
                    counter += 1;
                }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
            }
        }
        else if (year % 4 == 0 && (year % 100) % 4 != 0){
            for (int feb = 1; feb <= 29; feb++){
                if (feb == 1 && weekday == 7){
                    counter += 1;
                }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
            }
        }
        else{
            for (int feb = 1; feb <= 28; feb++){
                if (feb == 1 && weekday == 7){
                    counter += 1;
                }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
            }
        }
        //Mar
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Apr
        for (int jan = 1; jan <= 30; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //May
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Jun
        for (int jan = 1; jan <= 30; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Jul
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Aug
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Sep
        for (int jan = 1; jan <= 30; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Oct
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Nov
        for (int jan = 1; jan <= 30; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }
        //Dec
        for (int jan = 1; jan <= 31; jan++){         
            if (jan == 1 && weekday == 7){
                counter += 1;
            }
            weekday += 1;
            if (weekday % 8 == 0){
                weekday = 1;
            }
        }

    }

    printf("Number of 1st of Month which fell on Sundays from 1 Jan 1901 to 31 Dec 2020 is %d\n", counter - 2); // 2 deducted for 2 Sundays with 1 date in 1900

    return 0;

}
