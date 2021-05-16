import machine
import socket
from time import sleep


def request(url, sensor):
	addr = socket.getaddrinfo(url, 80)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('POST /metrics/%s HTTP/1.1\r\nContent-Type: multipart/form-data; boundary=---011000010111000001101001\r\nHost: pinogano2.mooo.com\r\n\r\n'% (sensor), 'utf8'))


def current():
	pin = machine.Pin(2, machine.Pin.OUT)
	pin.off()
	adc = machine.ADC(0)
	for _ in range(5):
		print(adc.read())
		request("pinogano2.mooo.com", adc.read())
		sleep(2)
		print("="*4)
	machine.deepsleep()


def sleep_mode(reset_time):
	rtc = machine.RTC() # RTC (Real Time Clock)
	rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)
	# Set reset time -> reset_time
	rtc.alarm(rtc.ALARM0, reset_time)


def run():
	if machine.reset_cause() == machine.DEEPSLEEP_RESET:
		print('\n\rdespertando :c ...')
	else:
		print('\n\rme resetearon we T-T ')
	sleep_mode(2000)
	current()


if __name__ == '__main__':
	run()