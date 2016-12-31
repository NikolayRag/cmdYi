import socket, json, time, re

from kiLog import *




'''
Lightweighted version of Yi4k API, reverse-engineered from official Java API.
It is limited so:
	- values provided to commands should be correct strings,
	- camera data exchanging operations are blocking,
	- no callbacks are supported.

Commands not implemented:

	formatSDCard
		NSFW

	deleteFile
		Considered vulnerable, maybe later

	downloadFile
	cancelDownload
		Redundant, available by http

	getRtspURL
		Redundant, available at YiAPI() creation

	buildLiveVideoQRCode
		Maybe later

	startRecording datetime
		Lazy to implement

'''



registeredCommands= []


'''
Class usable to pass to YiAPI.cmd()

	params
		dict of non-changing parameters.

	variable
		name or list of names to be assigned later with apply()
'''
class YiAPICommand():
	resultCB= None

	commandName= ''
	params= None
	names= None

	limit= None


	def __init__(self, _id, _commandName='', limit=None, params=None, variable=[], resultCB=None):
		self.resultCB= resultCB

		self.params= {'msg_id':int(_id)}
		if params:
			self.params.update(params)

		if not isinstance(variable, list) and not isinstance(variable, tuple):
			variable= [variable]

		self.names= variable


		if limit:
			self.limit= limit


		if _commandName:
			self.commandName= _commandName
			registeredCommands.append(self)



	'''
	Collect dict to be send to camera.
	Append stored params to provided dict and apply _val to stored .names respectively

	Return complete suitable dict.
	'''
	def apply(self, _dict, _val=None):
		_dict.update(self.params)


		#assign provided _val[] values to stored .names[] parameters
		if not isinstance(_val, list) and not isinstance(_val, tuple):
			_val= [_val]

		for pair in zip(self.names,_val):
			_dict[pair[0]]= pair[1]


		return _dict




class YiAPI():
	jsonTest= re.compile('Extra data: line \d+ column \d+ - line \d+ column \d+ \(char (?P<char>\d+) - \d+\)')

	ip= '192.168.42.1'
	sock= None
	tick= 0
	sessionId= 0

	res= []



	@staticmethod
	def defaults(ip):
		if ip:
			YiAPI.ip= ip



	def __init__(self, _ip=None):
		if _ip:
			self.ip= _ip
		try:
			self.sock= socket.create_connection((self.ip,7878),3)
		except:
			self.res= False
			return

		res= self.cmd(startSession)
		if res<0:
			self.sock= None
			self.res= False
		else:
			self.sessionId= res


	#shoud be called at very end to tell camera it's released
	def close(self):
		self.cmd(stopSession)

		self.sock= None



	'''
	Run predefined _command.
	if _vals provided, it's a value assigned to YiAPICommand.vals respectively. 
	'''
	def cmd(self, _command, _val=None):
		if not self.sock:
			kiLog.err('Camera disconnected')
			return -99999


		self.cmdSend(_command, _val)
		self.res= self.jsonRestore( self.cmdRecv() )
		if not self.res:
			kiLog.err('Invalid response')
			return -99998


		res= {'rval':0}
		if len(self.res):
			for res in self.res:	#find block with rval
				if 'rval' in res:
					break


		if 'rval' in res and res['rval']:
			kiLog.err('Camera error: %d' % res['rval'])
			kiLog.verb('Full result: %s' % str(self.res))
			return res['rval']

		if callable(_command.resultCB):
			return _command.resultCB(res)

		if 'param' in res:
			return res['param']



	'''
	Sent _command co camera.
	'''
	def cmdSend(self, _command, _val=None):
		out= _command.apply({'token':self.sessionId, 'heartbeat':self.tick}, _val)

		kiLog.verb("Send: %s" % out)
		
		self.sock.sendall( bytes(json.dumps(out),'ascii') )

		self.tick+= 1



	'''
	Recieve string from socket till its dry.
	'''
	def cmdRecv(self):
		self.sock.settimeout(2)	#wait for a while for camera to execute command
		res= b''

		while True:
			try:
				recv= self.sock.recv(4096)
				res+= recv

				kiLog.verb("part: %s" % recv)

				self.sock.settimeout(.1) #wait a little for detect end-of-data
			except:
				break

		kiLog.verb("Recieved: %d bytes" % len(res))

		return res.decode()



	'''
	Form array of json-restored values from string containing several json-encoded blocks
	'''
	def jsonRestore(self, _json):
		jsonA= []

		jsonFrom= 0
		while True:
			try:
				jsonTry= json.loads(_json[jsonFrom:])
				jsonA.append(jsonTry)	#rest
				break	#json ended up
			except Exception as exc:
				kiLog.verb('Json result: ' +str(exc))
				
				jsonErr= self.jsonTest.match(str(exc))
				if not jsonErr:
					return False

				jsonFrom2= int(jsonErr.group('char'))
				jsonA.append( json.loads(_json[jsonFrom:jsonFrom+jsonFrom2]) )

				jsonFrom+= jsonFrom2


		return(jsonA)


'''
Define commands
'''
startSession= YiAPICommand(257)
stopSession= YiAPICommand(258)


startRecording=		YiAPICommand(513, 'startRecording')
stopRecording=		YiAPICommand(514, 'stopRecording')
capturePhoto=		YiAPICommand(16777220, 'capturePhoto',
	params={'param':'precise quality;off'}
)
getFileList=		YiAPICommand(1282, 'getFileList',
	params={'param':'/tmp/fuse_d'},
	resultCB= lambda res: res['listing']
)
#	deleteFile=		YiAPICommand(1281, 'deleteFile', {}, {'param': '/tmp/fuse_d/DCIM'}, resultCB= lambda res: res['listing'])
startViewFinder=		YiAPICommand(259, 'startViewFinder')
stopViewFinder=		YiAPICommand(260, 'stopViewFinder')


getSettings=		YiAPICommand(3,	'getSettings',
	resultCB=lambda res:{key:val for d in res['param'] for key,val in d.items()}
)
#"yyyy-MM-dd HH:mm:ss"
setDateTime=		YiAPICommand(2,	'setDateTime',
	params= {'type':'camera_clock'},
	variable= 'param'
)
#
setSystemMode=		YiAPICommand(2,	'setSystemMode',
	limit= ["capture", "record"],
	params= {'type':'system_mode'},
	variable= 'param'
)
#
getVideoResolution=		YiAPICommand(1, 'getVideoResolution',
	params={'type':'video_resolution'}
)
setVideoResolution=		YiAPICommand(2,	'setVideoResolution',
	limit= ["3840x2160 30P 16:9", "3840x2160 30P 16:9 super", "2560x1920 30P 4:3", "1920x1440 60P 4:3", "1920x1440 30P 4:3", "1920x1080 120P 16:9", "1920x1080 120P 16:9 super", "1920x1080 60P 16:9", "1920x1080 60P 16:9 super", "1920x1080 30P 16:9", "1920x1080 30P 16:9 super", "1280x960 120P 4:3", "1280x960 60P 4:3", "1280x720 240P 16:9", "1280x720 120P 16:9 super", "1280x720 60P 16:9 super", "840x480 240P 16:9"],
	params= {'type':'video_resolution'},
	variable= 'param'
)
#
getPhotoResolution=		YiAPICommand(1, 'getPhotoResolution',
	params={'type':'photo_size'}
)
setPhotoResolution=		YiAPICommand(2,	'setPhotoResolution',
	limit= ["12MP (4000x3000 4:3) fov:w", "7MP (3008x2256 4:3) fov:w", "7MP (3008x2256 4:3) fov:m", "5MP (2560x1920 4:3) fov:m", "8MP (3840x2160 16:9) fov:w"],
	params= {'type':'photo_size'},
	variable= 'param'
)
#
getPhotoWhiteBalance=		YiAPICommand(1, 'getPhotoWhiteBalance',
	params={'type':'iq_photo_wb'}
)
setPhotoWhiteBalance=		YiAPICommand(2,	'setPhotoWhiteBalance',
	limit= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_photo_wb'},
	variable= 'param'
)
#
getVideoWhiteBalance=		YiAPICommand(1, 'getVideoWhiteBalance',
	params={'type':'iq_video_wb'}
)
setVideoWhiteBalance=		YiAPICommand(2,	'setVideoWhiteBalance',
	limit= ["auto", "native", "3000k", "5500k", "6500k"],
	params= {'type':'iq_video_wb'},
	variable= 'param'
)
#
getPhotoISO=		YiAPICommand(1, 'getPhotoISO',
	params={'type':'iq_photo_iso'}
)
setPhotoISO=		YiAPICommand(2,	'setPhotoISO',
	limit= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_photo_iso'},
	variable= 'param'
)
#
getVideoISO=		YiAPICommand(1, 'getVideoISO',
	params={'type':'iq_video_iso'}
)
setVideoISO=		YiAPICommand(2,	'setVideoISO',
	limit= ["auto", "100", "200", "400", "800", "1600", "6400"],
	params= {'type':'iq_video_iso'},
	variable= 'param'
)
#
getPhotoExposureValue=		YiAPICommand(1, 'getPhotoExposureValue',
	params={'type':'iq_photo_ev'}
)
setPhotoExposureValue=		YiAPICommand(2,	'setPhotoExposureValue',
	limit= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_photo_ev'},
	variable= 'param'
)
#
getVideoExposureValue=		YiAPICommand(1, 'getVideoExposureValue',
	params={'type':'iq_video_ev'}
)
setVideoExposureValue=		YiAPICommand(2,	'setVideoExposureValue',
	limit= ["-2.0", "-1.5", "-1.0", "-0.5", "0", "+0.5", "+1.0", "+1.5", "+2.0"],
	params= {'type':'iq_video_ev'},
	variable= 'param'
)
#
getPhotoShutterTime=		YiAPICommand(1, 'getPhotoShutterTime',
	params={'type':'iq_photo_shutter'}
)
setPhotoShutterTime=		YiAPICommand(2,	'setPhotoShutterTime',
	limit= ["auto", "2s", "5s", "10s", "20s", "30s"],
	params= {'type':'iq_photo_shutter'},
	variable= 'param'
)
#
getVideoSharpness=		YiAPICommand(1, 'getVideoSharpness',
	params={'type':'video_sharpness'}
)
setVideoSharpness=		YiAPICommand(2,	'setVideoSharpness',
	limit= ["low", "medium", "high"],
	params= {'type':'video_sharpness'},
	variable= 'param'
)
#
getPhotoSharpness=		YiAPICommand(1, 'getPhotoSharpness',
	params={'type':'photo_sharpness'}
)
setPhotoSharpness=		YiAPICommand(2,	'setPhotoSharpness',
	limit= ["low", "medium", "high"],
	params= {'type':'photo_sharpness'},
	variable= 'param'
)
#
getVideoFieldOfView=		YiAPICommand(1, 'getVideoFieldOfView',
	params={'type':'fov'}
)
setVideoFieldOfView=		YiAPICommand(2,	'setVideoFieldOfView',
	limit= ["wide", "medium", "narrow"],
	params= {'type':'fov'},
	variable= 'param'
)
#
getRecordMode=		YiAPICommand(1, 'getRecordMode',
	params={'type':'rec_mode'}
)
setRecordMode=		YiAPICommand(2,	'setRecordMode',
	limit= ["record", "record_timelapse", "record_slow_motion", "record_loop", "record_photo"],
	params= {'type':'rec_mode'},
	variable= 'param'
)
#
getCaptureMode=		YiAPICommand(1, 'getCaptureMode',
	params={'type':'capture_mode'}
)
setCaptureMode=		YiAPICommand(2,	'setCaptureMode',
	["precise quality", "precise self quality", "burst quality", "precise quality cont."],
	{'type':'capture_mode'},
	variable= 'param'
)
#
getMeteringMode=		YiAPICommand(1, 'getMeteringMode',
	params={'type':'meter_mode'}
)
setMeteringMode=		YiAPICommand(2,	'setMeteringMode',
	limit= ["center", "average", "spot"],
	params= {'type':'meter_mode'},
	variable= 'param'
)
#
getVideoQuality=		YiAPICommand(1, 'getVideoQuality',
	params={'type':'video_quality'}
)
setVideoQuality=		YiAPICommand(2,	'setVideoQuality',
	limit= ["S.Fine", "Fine", "Normal"],
	params= {'type':'video_quality'},
	variable= 'param'
)
#
getVideoColorMode=		YiAPICommand(1, 'getVideoColorMode',
	params={'type':'video_flat_color'}
)
setVideoColorMode=		YiAPICommand(2,	'setVideoColorMode',
	limit= ["yi", "flat"],
	params= {'type':'video_flat_color'},
	variable= 'param'
)
#
getPhotoColorMode=		YiAPICommand(1, 'getPhotoColorMode',
	params={'type':'photo_flat_color'}
)
setPhotoColorMode=		YiAPICommand(2,	'setPhotoColorMode',
	limit= ["yi", "flat"],
	params= {'type':'photo_flat_color'},
	variable= 'param'
)
#
getElectronicImageStabilizationState=		YiAPICommand(1, 'getElectronicImageStabilizationState',
	params={'type':'iq_eis_enable'}
)
setElectronicImageStabilizationState=		YiAPICommand(2,	'setElectronicImageStabilizationState',
	limit= ["on", "off"],
	params= {'type':'iq_eis_enable'},
	variable= 'param'
)
#
getAdjustLensDistortionState=		YiAPICommand(1, 'getAdjustLensDistortionState',
	params={'type':'warp_enable'}
)
setAdjustLensDistortionState=		YiAPICommand(2,	'setAdjustLensDistortionState',
	limit= ["on", "off"],
	params= {'type':'warp_enable'},
	variable= 'param'
)
#
getVideoMuteState=		YiAPICommand(1, 'getVideoMuteState',
	params={'type':'video_mute_set'}
)
setVideoMuteState=		YiAPICommand(2,	'setVideoMuteState',
	limit= ["on", "off"],
	params= {'type':'video_mute_set'},
	variable= 'param'
)
#
getVideoTimestamp=		YiAPICommand(1, 'getVideoTimestamp',
	params={'type':'video_stamp'}
)
setVideoTimestamp=		YiAPICommand(2,	'setVideoTimestamp',
	limit= ["off", "time", "date", "date/time"],
	params= {'type':'video_stamp'},
	variable= 'param'
)
#
getPhotoTimestamp=		YiAPICommand(1, 'getPhotoTimestamp',
	params={'type':'photo_stamp'}
)
setPhotoTimestamp=		YiAPICommand(2,	'setPhotoTimestamp',
	limit= ["off", "time", "date", "date/time"],
	params= {'type':'photo_stamp'},
	variable= 'param'
)
#
getLEDMode=		YiAPICommand(1, 'getLEDMode',
	params={'type':'led_mode'}
)
setLEDMode=		YiAPICommand(2,	'setLEDMode',
	limit= ["all enable", "all disable", "status enable"],
	params= {'type':'led_mode'},
	variable= 'param'
)
#
getVideoStandard=		YiAPICommand(1, 'getVideoStandard',
	params={'type':'video_standard'}
)
setVideoStandard=		YiAPICommand(2,	'setVideoStandard',
	limit= ["PAL", "NTSC"],
	params= {'type':'video_standard'},
	variable= 'param'
)
#
getTimeLapseVideoInterval=		YiAPICommand(1, 'getTimeLapseVideoInterval',
	params={'type':'timelapse_video'}
)
setTimeLapseVideoInterval=		YiAPICommand(2,	'setTimeLapseVideoInterval',
	limit= ["0.5", "1", "2", "5", "10", "30", "60"],
	params= {'type':'timelapse_video'},
	variable= 'param'
)
#
getTimeLapsePhotoInterval=		YiAPICommand(1, 'getTimeLapsePhotoInterval',
	params={'type':'precise_cont_time'}
)
setTimeLapsePhotoInterval=		YiAPICommand(2,	'setTimeLapsePhotoInterval',
	limit= ["continue", "0.5 sec", "1.0 sec", "2.0 sec", "5.0 sec", "10.0 sec", "30.0 sec", "60.0 sec", "2.0 min", "5.0 min", "10.0 min", "30.0 min", "60.0 min"],
	params= {'type':'precise_cont_time'},
	variable= 'param'
)
#
getTimeLapseVideoDuration=		YiAPICommand(1, 'getTimeLapseVideoDuration',
	params={'type':'timelapse_video_duration'}
)
setTimeLapseVideoDuration=		YiAPICommand(2,	'setTimeLapseVideoDuration',
	limit= ["off", "6s", "8s", "10s", "20s", "30s", "60s", "120s"],
	params= {'type':'timelapse_video_duration'},
	variable= 'param'
)
#
getScreenAutoLock=		YiAPICommand(1, 'getScreenAutoLock',
	params={'type':'screen_auto_lock'}
)
setScreenAutoLock=		YiAPICommand(2,	'setScreenAutoLock',
	limit= ["never", "30s", "60s", "120s"],
	params= {'type':'screen_auto_lock'},
	variable= 'param'
)
#
getAutoPowerOff=		YiAPICommand(1, 'getAutoPowerOff',
	params={'type':'auto_power_off'}
)
setAutoPowerOff=		YiAPICommand(2,	'setAutoPowerOff',
	limit= ["off", "3 minutes", "5 minutes", "10 minutes"],
	params= {'type':'auto_power_off'},
	variable= 'param'
)
#
getVideoRotateMode=		YiAPICommand(1, 'getVideoRotateMode',
	params={'type':'video_rotate'}
)
setVideoRotateMode=		YiAPICommand(2,	'setVideoRotateMode',
	limit= ["off", "on", "auto"],
	params= {'type':'video_rotate'},
	variable= 'param'
)
#
getBuzzerVolume=		YiAPICommand(1, 'getBuzzerVolume',
	params={'type':'buzzer_volume'}
)
setBuzzerVolume=		YiAPICommand(2,	'setBuzzerVolume',
	limit= ["high", "low", "mute"],
	params= {'type':'buzzer_volume'},
	variable= 'param'
)
#
getLoopDuration=		YiAPICommand(1, 'getLoopDuration',
	params={'type':'loop_rec_duration'}
)
setLoopDuration=		YiAPICommand(2,	'setLoopDuration',
	limit= ["5 minutes", "20 minutes", "60 minutes", "120 minutes", "max"],
	params= {'type':'loop_rec_duration'},
	variable= 'param'
)
