import machine
from time import sleep

def sleep_mode(reset_time):
	rtc = machine.RTC() # RTC (Real Time Clock)
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
	# Set reset time -> reset_time
	rtc.alarm(rtc.ALARM0, reset_time)


def current():
	pin = machine.Pin(2, machine.Pin.OUT)
	pin.off()
	adc = machine.ADC(0)
	while True:
		print(adc.read())
		sleep(0.25)
		if (adc.read() > 1020):
			break
	machine.deepsleep()


def run():
	if machine.reset_cause() == machine.DEEPSLEEP_RESET:
		print('\n\rDespertando...')
	else:
		print('\n\rMe resetearon we :3')
	sleep_mode(5000)
	current()


if __name__ == '__main__':
	run()
