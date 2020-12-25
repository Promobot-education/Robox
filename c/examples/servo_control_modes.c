/******************************************************************************
     * File: servo_control_modes.c
     * Description: Пример работы с сервоприводом . Работа в различных ре-имах управления дигателем.
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

  //Перемещение на позицию 4000
  set_point(servo_addr,4000);

  sleep(4);

  //Выключение питания обмоток двигателя
  set_torque(servo_addr,false);

  //Ре-им ПИД по скорости
  set_PID_mode(servo_addr,SPEED);

  set_torque(servo_addr,true);

   //Скорость вращения вала 10 об/сек
  set_point(servo_addr,10);

  sleep(4);  

  set_torque(servo_addr,false);

  //Прямой ре-им работы. Без ПИД регуляторов
  set_PID_mode(servo_addr,PWM);
  set_torque(servo_addr,true);

  //Высталение ШИМ 750 из 1000. Сква-ность 75%
  set_point(servo_addr,750);
  sleep(4);  
  set_torque(servo_addr,false);

  //Включение стадартного ре-има работы
  set_PID_mode(servo_addr,NORMAL);
 
  return 0; 
}