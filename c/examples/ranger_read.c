/******************************************************************************
     * File: ranger_read.c
     * Description: Пример работы с датчиком расстояния. Цикличный опрос.
******************************************************************************/
#include "Ranger.h"
#include "bus_handler.h"

//Структура для записи полученных значений с датчика
struct sensor_data data;

//Адрес датчика. По умолчанию 1
int sensor_addr = 1;

int main()
{

  //Инициализация последовательного порта для работы с датчиком. По умолчанию /dev/RS_485
  if (init_port("/dev/RS_485",false) < 0)
  {
    return -1;
  }


  while(1)
  {

    //Отправка команды на измерение расстояния
    trig_sensor(sensor_addr);

    //О-идание отра-ения сигналов измерения
    usleep(10000);

    //Чтение измеренных значений расстояния
    data = read_sensor(sensor_addr);

    //Вывод измеренных расстояний
    printf("Data from sensor: \n");  
    printf("US_diatance: %i\n",data.US_distance);
    printf("IR_distance: %i\n\n",data.IR_distance);

  }

  return 0; 
}