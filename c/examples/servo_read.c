/******************************************************************************
     * File: servo_control_modes.c
     * Description: Пример работы с сервоприводом. Перемещение в требуемую позицию.
******************************************************************************/
#include "Servo.h"
#include "bus_handler.h"

//Структура для записи данных с сервопривода
struct servo_data data;

//Адрес сервопривода. По умолчанию 10.
int servo_addr = 10;

int main()
{

  //Инициализация последовательного порта для работы с сервоприводом. По умолчанию /dev/RS_485
  if (init_port("/dev/RS_485",false) < 0)
  {
    return -1;
  }

  //Инициализация сервопривода
  init_servo(servo_addr);
  set_torque(10, true);

  while (1) 
  {  
    //Чтение данных с сервопривода
    data = get_servo_data(servo_addr);

    //Вывод некоторых данных с сервопривода
    printf("Data from servo: \n");  
    printf("Position: %i\n",data.position);
    printf("Setpoint: %i\n",data.setpoint);
    printf("Motor current: %i mA \n\n",data.current);
    usleep(10000);
  }

  return 0; 
}