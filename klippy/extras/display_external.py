import serial
import logging
import klippy

class DisplayExternal:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.baudrate = config.getint('baudrate', 115200)
        self.serial_port = config.get('serial_port', '/dev/ttyUSB0')
        self.ready_text = config.get('ready_text', 'DisplayExternal V1')
        self.serial_conn = None
        
        try:
            self.serial_conn = serial.Serial(
                self.serial_port, self.baudrate, timeout=1
            )
            logging.info(f"[DisplayExternal] Connected to a {self.serial_port} a {self.baudrate} bps")
        except Exception as e:
            logging.error(f"[DisplayExternal] Fail Connecting: {e}")
            self.serial_conn = None
        
        self.printer.register_event_handler('klippy:ready', self._on_ready)
        self.printer.add_object('display_external', self)
        self.gcode = self.printer.lookup_object('gcode')
        self.gcode.register_command('DISPLAY_EXTERNAL_TEXT', self.cmd_display_text, desc="Send text to External Display")

    def _on_ready(self):
        if self.serial_conn and self.serial_conn.is_open:
            self.send_text(self.ready_text)
    
    def send_text(self, text):
        if self.serial_conn and self.serial_conn.is_open:
            try:
                self.serial_conn.write((text + '\n').encode('utf-8'))
            except Exception as e:
                logging.error(f"[DisplayExternal] Fail while sending data: {e}")
        else:
            logging.error("[DisplayExternal] Serial Connection failed")
    
    def cmd_display_text(self, gcmd):
        text = gcmd.get('TEXT', None)
        if text:
            self.send_text(text)
        else:
            logging.error("[DisplayExternal] Please specify text to send")

def load_config(config):
    return DisplayExternal(config)
