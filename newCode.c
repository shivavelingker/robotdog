#pragma config(Sensor, S1,     ,               sensorEV3_Ultrasonic)
#pragma config(Sensor, S2,     ,               sensorEV3_Color, modeEV3Color_Color)
#pragma config(Sensor, S3,     ,               sensorEV3_Color, modeEV3Color_Color)
#pragma config(Sensor, S4,     ,               sensorEV3_Color, modeEV3Color_Color)
#pragma config(Motor,  motorA,           ,             tmotorEV3_Large, PIDControl, reversed, encoder)
#pragma config(Motor,  motorB,           ,             tmotorEV3_Large, PIDControl, reversed, encoder)

//These variables will make it easier to call functions
const int black = 1, red = 5, white = 6, yellow = 4, blue = 2, green = 3, parkingSpace = 2005;

int frontSensor();
int leftSensor();
int rightSensor();
void Drive_white();
void Drive_yellow();
void turnLeft();
void turnRight();
void sonarContinuous();
void RightOfWay();
void Parking_right(int space);
void Circle();

int frontSensor(){
	return SensorValue[S2];
}

int leftSensor(){
	return SensorValue[S3];
}

int rightSensor(){
	return  SensorValue[S4];
}

void Circle(){
	while(frontSensor() != red){
		sonarContinuous();
		if(leftSensor() == green){
			motor[motorA] = 25;
			motor[motorB] = 20;
			wait1Msec(1);
		}
		if(leftSensor() == black){
			motor[motorA] = 20;
			motor[motorB] = 25;
			wait1Msec(1);
		}
		if(leftSensor() == yellow){
			motor[motorA] = 25;
			motor[motorB] = 25;
			wait1Msec(1);
		}
	}
}

void Drive_white(){
	motor[motorA] = 20;
	motor[motorB] = 20;
	wait1Msec(300);
	while(frontSensor() != red){
			sonarContinuous();
			if((leftSensor() == black && rightSensor() == white) || (leftSensor() == white && rightSensor() == black) || (leftSensor() == black && rightSensor() == red) || (leftSensor() == red && rightSensor() == black)){
				motor[motorA] = 50;
				motor[motorB] = 50;
				wait1Msec(1);
			}

				if(leftSensor() == black){
						motor[motorA]=40;
						motor[motorB]=50;
						wait1Msec(1);
				}
				else{
				if(rightSensor() == black){
						motor[motorA]=50;
						motor[motorB]=40;
						wait1Msec(1);
				}
				else{//(leftSensor() != black && rightSensor() != black){
						motor[motorA]=50;
						motor[motorB]=50;
						wait1Msec(1);
				}
			}
	}
	motor[motorA]=0;
	motor[motorB]=0;
	wait1Msec(3000);

}

void Drive_yellow(){
	motor[motorA] = 20;
	motor[motorB] = 20;
	wait1Msec(300);
	while(frontSensor() != red){
				sonarContinuous();
				if((leftSensor() == blue || leftSensor() == black) && rightSensor() == blue){
					motor[motorA] = 25;
					motor[motorB] = 25;
					wait1Msec(1);
				}
				if((leftSensor() == black && rightSensor() == white) || (leftSensor() == white && rightSensor() == black) || (leftSensor() == black && rightSensor() == red) || (leftSensor() == red && rightSensor() == black)){
					motor[motorA] = 50;
					motor[motorB] = 50;
					wait1Msec(1);
				}
				if(leftSensor() == black){
						motor[motorA]=20;
						motor[motorB]=25;
						wait1Msec(1);
				}
				else{
				if(rightSensor() == black){
						motor[motorA]=25;
						motor[motorB]=20;
						wait1Msec(1);
				}
				else{//(leftSensor() != black && rightSensor() != black){
						motor[motorA]=25;
						motor[motorB]=25;
						wait1Msec(1);
				}
		}
	}
	//pause for three seconds
	motor[motorA]=0;
	motor[motorB]=0;
	wait1Msec(3000);

}

void turnLeft(){
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorB] = 0;

	motor[motorA] = 70;
	motor[motorB] = 70;
	wait1Msec(650);

	motor[motorA] = -30;
	motor[motorB] = 30;
	wait1Msec(1000);
}

void turnRight(){
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorB] = 0;

	motor[motorA] = 70;
	motor[motorB] = 70;
	wait1Msec(650);

	motor[motorA] = 30;
	motor[motorB] = -30;
	wait1Msec(1000);
}

void Parking_right(int space, bool bump){
	//go until parking spaces
	if (bump == true){
		motor[motorA] = 25;
		motor[motorB] = 25;
		wait1Msec(2000);
	}
	while(rightSensor() != blue){
			//sonarContinuous();

		if(leftSensor() != black && rightSensor() != black){
				motor[motorA]=25;
				motor[motorB]=25;
				wait1Msec(1);
		}
		if(leftSensor() == black && rightSensor() == red){
				motor[motorA]=25;
				motor[motorB]=25;
				wait1Msec(1);
		}
		if(rightSensor() != red){
			motor[motorA] = 20;
			motor[motorB] = 25;
			wait1Msec(1);
		}
	}
	//zero motors
	nMotorEncoder[motorA] = 0;
	nMotorEncoder[motorB] = 0;

	//get to correct parking spot
	int counter = 0;
	while(counter <= parkingSpace*space){
		if(leftSensor()==black){
			motor[motorA] = 25;
			motor[motorB] = 27;
			wait1Msec(1);
		}
		else{
				if(rightSensor() == black){
					motor[motorA] = 27;
					motor[motorB] = 25;
					wait1Msec(1);
				}
				else{
					motor[motorA] = 26;
					motor[motorB] = 25;
				}
		}
		counter++;
	}

	//pause 3 seconds outside of parking spot
	motor[motorA] = 0;
	motor[motorB] = 0;
	wait1Msec(3000);

	//turn right
	motor[motorA] = 30;
	motor[motorB] = -30;
	wait1Msec(1000);

	//bump
	motor[motorA] = 25;
	motor[motorB] = 25;
	wait1Msec(300);

	//move into parking spot
	while(frontSensor()!=white){
		motor[motorA] = 25;
		motor[motorB] = 25;
		wait1Msec(1);
	}

	//pause 3 seconds
	motor[motorA] = 0;
	motor[motorB] = 0;
	wait1Msec(3000);

	//back up bump
	motor[motorA] = -25;
	motor[motorB] = -25;
	wait1Msec(300);

	//back out completely
	while(frontSensor()!= blue){
		motor[motorA] = -25;
		motor[motorB] = -25;
		wait1Msec(1);
	}

	//bump
		motor[motorA] = 25;
		motor[motorB] = 25;
		wait1Msec(200);

		//turn left
	motor[motorA] = -30;
	motor[motorB] = 30;
	wait1Msec(900);

	Drive_yellow();
}

void finishLine(){
	while(leftSensor() != red){
		if(rightSensor()==black){
			motor[motorA] = 30;
			motor[motorB] = 25;
			wait1Msec(1);
		}
		else{
				if(leftSensor() == black){
					motor[motorA] = 25;
					motor[motorB] = 27;
					wait1Msec(1);
				}
				else{
					motor[motorA] = 26;
					motor[motorB] = 25;
				}
		}
	}
	turnLeft();
	while(frontSensor() != white){
		motor[motorA] = 26;
		motor[motorB] = 25;
		wait1Msec(1);
	}
}

void sonarContinuous(){
	if(SensorValue[S1]<20){
			motor[motorA] = 0;
			motor[motorB] = 0;
			wait1Msec(1);
		}
}

void RightOfWay(){
	//turn left and check
	motor[motorA] = -35;
	motor[motorB] = 35;
	wait1Msec(400);
	//if robot is there, wait for it to leave
	while(SensorValue[S1]<25){
		playSound(soundBlip);
		motor[motorA] = 0;
		motor[motorB] = 0;
		wait1Msec(1);
	}

	//turn all the way right now
	motor[motorA] = 35;
	motor[motorB] = -35;
	wait1Msec(950);
	//if robot is here, wait for it to leave
	while (SensorValue[S1]<25){
		playSound(soundBlip);
		motor[motorA] = 0;
		motor[motorB] = 0;
		wait1Msec(1);
	}
	//turn back to original
	motor[motorA] = -35;
	motor[motorB] = 35;
	wait1Msec(450);
	//wait if robot exists
	while (SensorValue[S1]<20){
		playSound(soundBlip);
		motor[motorA] = 0;
		motor[motorB] = 0;
		wait1Msec(1);


	//wait until no robot detected
	while (!SensorValue[S1]<20){
		playSound(soundBlip);
		motor[motorA] = 0;
		motor[motorB] = 0;
		wait1Msec(1);
	}

	//move forward
	motor[motorA] = 25;
	motor[motorB] = 25;
	wait1Msec(3000);

	//exit and go to next function
}
}

task main(){
Drive_white();  //node connection 87
	Drive_white();  //node connection 76
	turnLeft();Drive_yellow();  //node connection 612
	turnLeft();Drive_white();  //node connection 1225
	}
