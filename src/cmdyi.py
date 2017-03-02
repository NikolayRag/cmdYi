import time, logging
import Yi4kAPI

#set order
cmdA= (
	Yi4kAPI.stopRecording,
	Yi4kAPI.getFileList,
	Yi4kAPI.getSettings,

	Yi4kAPI.getVideoResolution,
	Yi4kAPI.getPhotoResolution,
	Yi4kAPI.getPhotoWhiteBalance,
	Yi4kAPI.getVideoWhiteBalance,
	Yi4kAPI.getPhotoISO,
	Yi4kAPI.getVideoISO,
	Yi4kAPI.getPhotoExposureValue,
	Yi4kAPI.getVideoExposureValue,
	Yi4kAPI.getPhotoShutterTime,
	Yi4kAPI.getVideoSharpness,
	Yi4kAPI.getPhotoSharpness,
	Yi4kAPI.getVideoFieldOfView,
	Yi4kAPI.getRecordMode,
	Yi4kAPI.getCaptureMode,
	Yi4kAPI.getMeteringMode,
	Yi4kAPI.getVideoQuality,
	Yi4kAPI.getVideoColorMode,
	Yi4kAPI.getPhotoColorMode,
	Yi4kAPI.getElectronicImageStabilizationState,
	Yi4kAPI.getAdjustLensDistortionState,
	Yi4kAPI.getVideoMuteState,
	Yi4kAPI.getVideoTimestamp,
	Yi4kAPI.getPhotoTimestamp,
	Yi4kAPI.getLEDMode,
	Yi4kAPI.getVideoStandard,
	Yi4kAPI.getTimeLapseVideoInterval,
	Yi4kAPI.getTimeLapsePhotoInterval,
	Yi4kAPI.getTimeLapseVideoDuration,
	Yi4kAPI.getScreenAutoLock,
	Yi4kAPI.getAutoPowerOff,
	Yi4kAPI.getVideoRotateMode,
	Yi4kAPI.getBuzzerVolume,
	Yi4kAPI.getLoopDuration,


	Yi4kAPI.setDateTime,
	Yi4kAPI.setSystemMode,
	Yi4kAPI.setVideoResolution,
	Yi4kAPI.setPhotoResolution,
	Yi4kAPI.setPhotoWhiteBalance,
	Yi4kAPI.setVideoWhiteBalance,
	Yi4kAPI.setPhotoISO,
	Yi4kAPI.setVideoISO,
	Yi4kAPI.setPhotoExposureValue,
	Yi4kAPI.setVideoExposureValue,
	Yi4kAPI.setPhotoShutterTime,
	Yi4kAPI.setVideoSharpness,
	Yi4kAPI.setPhotoSharpness,
	Yi4kAPI.setVideoFieldOfView,
	Yi4kAPI.setRecordMode,
	Yi4kAPI.setCaptureMode,
	Yi4kAPI.setMeteringMode,
	Yi4kAPI.setVideoQuality,
	Yi4kAPI.setVideoColorMode,
	Yi4kAPI.setPhotoColorMode,
	Yi4kAPI.setElectronicImageStabilizationState,
	Yi4kAPI.setAdjustLensDistortionState,
	Yi4kAPI.setVideoMuteState,
	Yi4kAPI.setVideoTimestamp,
	Yi4kAPI.setPhotoTimestamp,
	Yi4kAPI.setLEDMode,
	Yi4kAPI.setVideoStandard,
	Yi4kAPI.setTimeLapseVideoInterval,
	Yi4kAPI.setTimeLapsePhotoInterval,
	Yi4kAPI.setTimeLapseVideoDuration,
	Yi4kAPI.setScreenAutoLock,
	Yi4kAPI.setAutoPowerOff,
	Yi4kAPI.setVideoRotateMode,
	Yi4kAPI.setBuzzerVolume,
	Yi4kAPI.setLoopDuration,

	Yi4kAPI.capturePhoto,
	Yi4kAPI.startRecording
)


def execute(_args):
	yi= Yi4kAPI.YiAPI()

	if not yi.sock:
		logging.error('Camera not found')
		return


	for cCmd in cmdA:
		cName= '_'.join( cCmd.commandName.split('-') )
		if _args[cName] not in (None,False):
			print(cCmd.values)
			if cCmd.values:
				res= yi.cmd(cCmd, cCmd.values[int(_args[cName])])
				print("%s: %s, %s" % (cName, cCmd.values.index(res),res))
			else:
				res= yi.cmd(cCmd, _args[cName])
				print("%s: %s" % (cName, res))


	yi.close()
