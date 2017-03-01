import time, logging
import Yi4kAPI


def execute(_args):
	yi= Yi4kAPI.YiAPI()

	if not yi.sock:
		logging.error('Camera not found')
		return

	if _args['stopRecording']:
		yi.cmd(Yi4kAPI.stopRecording)
		time.sleep(2)


	result= []
	if _args['getFileList']:
		res= yi.cmd(Yi4kAPI.getFileList)
		result.append(['getFileList',res])
	if _args['getSettings']:
		res= yi.cmd(Yi4kAPI.getSettings)
		result.append(['getSettings',res])
	if _args['getVideoResolution']:
		res= yi.cmd(Yi4kAPI.getVideoResolution)
		result.append(['getVideoResolution',Yi4kAPI.setVideoResolution.values.index(res),res])
	if _args['getPhotoResolution']:
		res= yi.cmd(Yi4kAPI.getPhotoResolution)
		result.append(['getPhotoResolution',Yi4kAPI.setPhotoResolution.values.index(res),res])
	if _args['getPhotoWhiteBalance']:
		res= yi.cmd(Yi4kAPI.getPhotoWhiteBalance)
		result.append(['getPhotoWhiteBalance',Yi4kAPI.setPhotoWhiteBalance.values.index(res),res])
	if _args['getVideoWhiteBalance']:
		res= yi.cmd(Yi4kAPI.getVideoWhiteBalance)
		result.append(['getVideoWhiteBalance',Yi4kAPI.setVideoWhiteBalance.values.index(res),res])
	if _args['getPhotoISO']:
		res= yi.cmd(Yi4kAPI.getPhotoISO)
		result.append(['getPhotoISO',Yi4kAPI.setPhotoISO.values.index(res),res])
	if _args['getVideoISO']:
		res= yi.cmd(Yi4kAPI.getVideoISO)
		result.append(['getVideoISO',Yi4kAPI.setVideoISO.values.index(res),res])
	if _args['getPhotoExposureValue']:
		res= yi.cmd(Yi4kAPI.getPhotoExposureValue)
		result.append(['getPhotoExposureValue',Yi4kAPI.setPhotoExposureValue.values.index(res),res])
	if _args['getVideoExposureValue']:
		res= yi.cmd(Yi4kAPI.getVideoExposureValue)
		result.append(['getVideoExposureValue',Yi4kAPI.setVideoExposureValue.values.index(res),res])
	if _args['getPhotoShutterTime']:
		res= yi.cmd(Yi4kAPI.getPhotoShutterTime)
		result.append(['getPhotoShutterTime',Yi4kAPI.setPhotoShutterTime.values.index(res),res])
	if _args['getVideoSharpness']:
		res= yi.cmd(Yi4kAPI.getVideoSharpness)
		result.append(['getVideoSharpness',Yi4kAPI.setVideoSharpness.values.index(res),res])
	if _args['getPhotoSharpness']:
		res= yi.cmd(Yi4kAPI.getPhotoSharpness)
		result.append(['getPhotoSharpness',Yi4kAPI.setPhotoSharpness.values.index(res),res])
	if _args['getVideoFieldOfView']:
		res= yi.cmd(Yi4kAPI.getVideoFieldOfView)
		result.append(['getVideoFieldOfView',Yi4kAPI.setVideoFieldOfView.values.index(res),res])
	if _args['getRecordMode']:
		res= yi.cmd(Yi4kAPI.getRecordMode)
		result.append(['getRecordMode',Yi4kAPI.setRecordMode.values.index(res),res])
	if _args['getCaptureMode']:
		res= yi.cmd(Yi4kAPI.getCaptureMode)
		result.append(['getCaptureMode',Yi4kAPI.setCaptureMode.values.index(res),res])
	if _args['getMeteringMode']:
		res= yi.cmd(Yi4kAPI.getMeteringMode)
		result.append(['getMeteringMode',Yi4kAPI.setMeteringMode.values.index(res),res])
	if _args['getVideoQuality']:
		res= yi.cmd(Yi4kAPI.getVideoQuality)
		result.append(['getVideoQuality',Yi4kAPI.setVideoQuality.values.index(res),res])
	if _args['getVideoColorMode']:
		res= yi.cmd(Yi4kAPI.getVideoColorMode)
		result.append(['getVideoColorMode',Yi4kAPI.setVideoColorMode.values.index(res),res])
	if _args['getPhotoColorMode']:
		res= yi.cmd(Yi4kAPI.getPhotoColorMode)
		result.append(['getPhotoColorMode',Yi4kAPI.setPhotoColorMode.values.index(res),res])
	if _args['getElectronicImageStabilizationState']:
		res= yi.cmd(Yi4kAPI.getElectronicImageStabilizationState)
		result.append(['getElectronicImageStabilizationState',Yi4kAPI.setElectronicImageStabilizationState.values.index(res),res])
	if _args['getAdjustLensDistortionState']:
		res= yi.cmd(Yi4kAPI.getAdjustLensDistortionState)
		result.append(['getAdjustLensDistortionState',Yi4kAPI.setAdjustLensDistortionState.values.index(res),res])
	if _args['getVideoMuteState']:
		res= yi.cmd(Yi4kAPI.getVideoMuteState)
		result.append(['getVideoMuteState',Yi4kAPI.setVideoMuteState.values.index(res),res])
	if _args['getVideoTimestamp']:
		res= yi.cmd(Yi4kAPI.getVideoTimestamp)
		result.append(['getVideoTimestamp',Yi4kAPI.setVideoTimestamp.values.index(res),res])
	if _args['getPhotoTimestamp']:
		res= yi.cmd(Yi4kAPI.getPhotoTimestamp)
		result.append(['getPhotoTimestamp',Yi4kAPI.setPhotoTimestamp.values.index(res),res])
	if _args['getLEDMode']:
		res= yi.cmd(Yi4kAPI.getLEDMode)
		result.append('getLEDMode',resYi4kAPI.setLEDMode.values.index(res),[])
	if _args['getVideoStandard']:
		res= yi.cmd(Yi4kAPI.getVideoStandard)
		result.append(['getVideoStandard',Yi4kAPI.setVideoStandard.values.index(res),res])
	if _args['getTimeLapseVideoInterval']:
		res= yi.cmd(Yi4kAPI.getTimeLapseVideoInterval)
		result.append(['getTimeLapseVideoInterval',Yi4kAPI.setTimeLapseVideoInterval.values.index(res),res])
	if _args['getTimeLapsePhotoInterval']:
		res= yi.cmd(Yi4kAPI.getTimeLapsePhotoInterval)
		result.append(['getTimeLapsePhotoInterval',Yi4kAPI.setTimeLapsePhotoInterval.values.index(res),res])
	if _args['getTimeLapseVideoDuration']:
		res= yi.cmd(Yi4kAPI.getTimeLapseVideoDuration)
		result.append(['getTimeLapseVideoDuration',Yi4kAPI.setTimeLapseVideoDuration.values.index(res),res])
	if _args['getScreenAutoLock']:
		res= yi.cmd(Yi4kAPI.getScreenAutoLock)
		result.append(['getScreenAutoLock',Yi4kAPI.setScreenAutoLock.values.index(res),res])
	if _args['getAutoPowerOff']:
		res= yi.cmd(Yi4kAPI.getAutoPowerOff)
		result.append(['getAutoPowerOff',Yi4kAPI.setAutoPowerOff.values.index(res),res])
	if _args['getVideoRotateMode']:
		res= yi.cmd(Yi4kAPI.getVideoRotateMode)
		result.append(['getVideoRotateMode',Yi4kAPI.setVideoRotateMode.values.index(res),res])
	if _args['getBuzzerVolume']:
		res= yi.cmd(Yi4kAPI.getBuzzerVolume)
		result.append(['getBuzzerVolume',Yi4kAPI.setBuzzerVolume.values.index(res),res])
	if _args['getLoopDuration']:
		res= yi.cmd(Yi4kAPI.getLoopDuration)
		result.append(['getLoopDuration',Yi4kAPI.setLoopDuration.values.index(res),res])

	for res in result:
		print(res)

	if _args['setDateTime']!=None:
		yi.cmd(Yi4kAPI.setDateTime, _args['setDateTime'])
	if _args['setSystemMode']!=None:
		yi.cmd(Yi4kAPI.setSystemMode, Yi4kAPI.setSystemMode.values[int(_args['setSystemMode'])])
	if _args['setVideoResolution']!=None:
		yi.cmd(Yi4kAPI.setVideoResolution, Yi4kAPI.setVideoResolution.values[int(_args['setVideoResolution'])])
	if _args['setPhotoResolution']!=None:
		yi.cmd(Yi4kAPI.setPhotoResolution, Yi4kAPI.setPhotoResolution.values[int(_args['setPhotoResolution'])])
	if _args['setPhotoWhiteBalance']!=None:
		yi.cmd(Yi4kAPI.setPhotoWhiteBalance, Yi4kAPI.setPhotoWhiteBalance.values[int(_args['setPhotoWhiteBalance'])])
	if _args['setVideoWhiteBalance']!=None:
		yi.cmd(Yi4kAPI.setVideoWhiteBalance, Yi4kAPI.setVideoWhiteBalance.values[int(_args['setVideoWhiteBalance'])])
	if _args['setPhotoISO']!=None:
		yi.cmd(Yi4kAPI.setPhotoISO, Yi4kAPI.setPhotoISO.values[int(_args['setPhotoISO'])])
	if _args['setVideoISO']!=None:
		yi.cmd(Yi4kAPI.setVideoISO, Yi4kAPI.setVideoISO.values[int(_args['setVideoISO'])])
	if _args['setPhotoExposureValue']!=None:
		yi.cmd(Yi4kAPI.setPhotoExposureValue, Yi4kAPI.setPhotoExposureValue.values[int(_args['setPhotoExposureValue'])])
	if _args['setVideoExposureValue']!=None:
		yi.cmd(Yi4kAPI.setVideoExposureValue, Yi4kAPI.setVideoExposureValue.values[int(_args['setVideoExposureValue'])])
	if _args['setPhotoShutterTime']!=None:
		yi.cmd(Yi4kAPI.setPhotoShutterTime, Yi4kAPI.setPhotoShutterTime.values[int(_args['setPhotoShutterTime'])])
	if _args['setVideoSharpness']!=None:
		yi.cmd(Yi4kAPI.setVideoSharpness, Yi4kAPI.setVideoSharpness.values[int(_args['setVideoSharpness'])])
	if _args['setPhotoSharpness']!=None:
		yi.cmd(Yi4kAPI.setPhotoSharpness, Yi4kAPI.setPhotoSharpness.values[int(_args['setPhotoSharpness'])])
	if _args['setVideoFieldOfView']!=None:
		yi.cmd(Yi4kAPI.setVideoFieldOfView, Yi4kAPI.setVideoFieldOfView.values[int(_args['setVideoFieldOfView'])])
	if _args['setRecordMode']!=None:
		yi.cmd(Yi4kAPI.setRecordMode, Yi4kAPI.setRecordMode.values[int(_args['setRecordMode'])])
	if _args['setCaptureMode']!=None:
		yi.cmd(Yi4kAPI.setCaptureMode, Yi4kAPI.setCaptureMode.values[int(_args['setCaptureMode'])])
	if _args['setMeteringMode']!=None:
		yi.cmd(Yi4kAPI.setMeteringMode, Yi4kAPI.setMeteringMode.values[int(_args['setMeteringMode'])])
	if _args['setVideoQuality']!=None:
		yi.cmd(Yi4kAPI.setVideoQuality, Yi4kAPI.setVideoQuality.values[int(_args['setVideoQuality'])])
	if _args['setVideoColorMode']!=None:
		yi.cmd(Yi4kAPI.setVideoColorMode, Yi4kAPI.setVideoColorMode.values[int(_args['setVideoColorMode'])])
	if _args['setPhotoColorMode']!=None:
		yi.cmd(Yi4kAPI.setPhotoColorMode, Yi4kAPI.setPhotoColorMode.values[int(_args['setPhotoColorMode'])])
	if _args['setElectronicImageStabilizationState']!=None:
		yi.cmd(Yi4kAPI.setElectronicImageStabilizationState, Yi4kAPI.setElectronicImageStabilizationState.values[int(_args['setElectronicImageStabilizationState'])])
	if _args['setAdjustLensDistortionState']!=None:
		yi.cmd(Yi4kAPI.setAdjustLensDistortionState, Yi4kAPI.setAdjustLensDistortionState.values[int(_args['setAdjustLensDistortionState'])])
	if _args['setVideoMuteState']!=None:
		yi.cmd(Yi4kAPI.setVideoMuteState, Yi4kAPI.setVideoMuteState.values[int(_args['setVideoMuteState'])])
	if _args['setVideoTimestamp']!=None:
		yi.cmd(Yi4kAPI.setVideoTimestamp, Yi4kAPI.setVideoTimestamp.values[int(_args['setVideoTimestamp'])])
	if _args['setPhotoTimestamp']!=None:
		yi.cmd(Yi4kAPI.setPhotoTimestamp, Yi4kAPI.setPhotoTimestamp.values[int(_args['setPhotoTimestamp'])])
	if _args['setLEDMode']!=None:
		yi.cmd(Yi4kAPI.setLEDMode, Yi4kAPI.setLEDMode.values[int(_args['setLEDMode'])])
	if _args['setVideoStandard']!=None:
		yi.cmd(Yi4kAPI.setVideoStandard, Yi4kAPI.setVideoStandard.values[int(_args['setVideoStandard'])])
	if _args['setTimeLapseVideoInterval']!=None:
		yi.cmd(Yi4kAPI.setTimeLapseVideoInterval, Yi4kAPI.setTimeLapseVideoInterval.values[int(_args['setTimeLapseVideoInterval'])])
	if _args['setTimeLapsePhotoInterval']!=None:
		yi.cmd(Yi4kAPI.setTimeLapsePhotoInterval, Yi4kAPI.setTimeLapsePhotoInterval.values[int(_args['setTimeLapsePhotoInterval'])])
	if _args['setTimeLapseVideoDuration']!=None:
		yi.cmd(Yi4kAPI.setTimeLapseVideoDuration, Yi4kAPI.setTimeLapseVideoDuration.values[int(_args['setTimeLapseVideoDuration'])])
	if _args['setScreenAutoLock']!=None:
		yi.cmd(Yi4kAPI.setScreenAutoLock, Yi4kAPI.setScreenAutoLock.values[int(_args['setScreenAutoLock'])])
	if _args['setAutoPowerOff']!=None:
		yi.cmd(Yi4kAPI.setAutoPowerOff, Yi4kAPI.setAutoPowerOff.values[int(_args['setAutoPowerOff'])])
	if _args['setVideoRotateMode']!=None:
		yi.cmd(Yi4kAPI.setVideoRotateMode, Yi4kAPI.setVideoRotateMode.values[int(_args['setVideoRotateMode'])])
	if _args['setBuzzerVolume']!=None:
		yi.cmd(Yi4kAPI.setBuzzerVolume, Yi4kAPI.setBuzzerVolume.values[int(_args['setBuzzerVolume'])])
	if _args['setLoopDuration']!=None:
		yi.cmd(Yi4kAPI.setLoopDuration, Yi4kAPI.setLoopDuration.values[int(_args['setLoopDuration'])])


	time.sleep(1)
	if _args['capturePhoto']:
		yi.cmd(Yi4kAPI.capturePhoto)
	if _args['startRecording']:
		yi.cmd(Yi4kAPI.startRecording)

	yi.close()
