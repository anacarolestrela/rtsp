#referencia: Jenish Mangukiya https://www.youtube.com/watch?v=bSs7H1NluIQ&ab_channel=JenishMangukiya
import sys
from time import time
HEADER_SIZE = 12

class RtpPacket:	
	header = bytearray(HEADER_SIZE)
	
	def __init__(self):
		pass
		
	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""
		timestamp = int(time())
		header = bytearray(HEADER_SIZE)

		self.header[0] = version << 6
		self.header[0] = self.header[0] | padding << 5
		self.header[0] = self.header[0] | extension << 4
		self.header[0] = self.header[0] | cc
		self.header[1] = marker << 7
		self.header[1] = self.header[1] | pt

		self.header[2] = seqnum >> 8
		self.header[3] = seqnum

		self.header[4] = (timestamp >> 24) & 0xFF
		self.header[5] = (timestamp >> 16) & 0xFF
		self.header[6] = (timestamp >> 8) & 0xFF
		self.header[7] = timestamp & 0xFF

		self.header[8] = ssrc >> 24
		self.header[9] = ssrc >> 16
		self.header[10] = ssrc >> 8
		self.header[11] = ssrc
		
		self.payload = payload
		
	def decode(self, byteStream):
		"""Decode do pacote RTP ."""
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]
	
	def version(self):
		"""Retorna RTP version."""
		return int(self.header[0] >> 6)
	
	def seqNum(self):
		"""Retorna numero de sequcia (frame) ."""
		seqNum = self.header[2] << 8 | self.header[3]
		return int(seqNum)
	
	def timestamp(self):
		"""Retorna timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)
	
	def payloadType(self):
		"""Retorna payload type."""
		pt = self.header[1] & 127
		return int(pt)
	
	def getPayload(self):
		"""Retorna payload."""
		return self.payload
		
	def getPacket(self):
		"""Retorna o pacote RTP"""
		return self.header + self.payload