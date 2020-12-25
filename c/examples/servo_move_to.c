/******************************************************************************
     * File: servo_move_to.c
     * Description: Пример работы с сервоприводом. Перемещение в требуемую позицию.
******************************************************************************/
#include "Servo.h"
#include "bus_handler.h"

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

  //Стандартный ре-им работы сервопривода
  set_PID_mode(servo_addr,NORMAL);

  //Включение питания обмоток двигателя
  set_torque(servo_addr,true);
  while (1) 
  {  

    //Перемещение на позицию 4000
    set_point(servo_addr,4000);
    sleep(4);

    set_point(servo_addr,0);
    sleep(4);

    set_point(servo_addr,-4000);
    sleep(4);   

  }   
  return 0; 
}