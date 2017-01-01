import time
import yi.yiAPI as yiAPI
from kiLog import *

def execute(_args):
	yi= yiAPI.YiAPI()

	if not yi.res:
		kiLog.err('Camera not found')
		return

	if _args['stopRecording']:
		yi.cmd(yiAPI.stopRecording)
		time.sleep(2)


	result= []
	if _args['getFileList']:
		res= yi.cmd(yiAPI.getFileList)
		result.append(['getFileList',res])
	if _args['getSettings']:
		res= yi.cmd(yiAPI.getSettings)
		result.append(['getSettings',res])
	if _args['getVideoResolution']:
		res= yi.cmd(yiAPI.getVideoResolution)
		result.append(['getVideoResolution',yiAPI.setVideoResolution.values.index(res),res])
	if _args['getPhotoResolution']:
		res= yi.cmd(yiAPI.getPhotoResolution)
		result.append(['getPhotoResolution',yiAPI.setPhotoResolution.values.index(res),res])
	if _args['getPhotoWhiteBalance']:
		res= yi.cmd(yiAPI.getPhotoWhiteBalance)
		result.append(['getPhotoWhiteBalance',yiAPI.setPhotoWhiteBalance.values.index(res),res])
	if _args['getVideoWhiteBalance']:
		res= yi.cmd(yiAPI.getVideoWhiteBalance)
		result.append(['getVideoWhiteBalance',yiAPI.setVideoWhiteBalance.values.index(res),res])
	if _args['getPhotoISO']:
		res= yi.cmd(yiAPI.getPhotoISO)
		result.append(['getPhotoISO',yiAPI.setPhotoISO.values.index(res),res])
	if _args['getVideoISO']:
		res= yi.cmd(yiAPI.getVideoISO)
		result.append(['getVideoISO',yiAPI.setVideoISO.values.index(res),res])
	if _args['getPhotoExposureValue']:
		res= yi.cmd(yiAPI.getPhotoExposureValue)
		result.append(['getPhotoExposureValue',yiAPI.setPhotoExposureValue.values.index(res),res])
	if _args['getVideoExposureValue']:
		res= yi.cmd(yiAPI.getVideoExposureValue)
		result.append(['getVideoExposureValue',yiAPI.setVideoExposureValue.values.index(res),res])
	if _args['getPhotoShutterTime']:
		res= yi.cmd(yiAPI.getPhotoShutterTime)
		result.append(['getPhotoShutterTime',yiAPI.setPhotoShutterTime.values.index(res),res])
	if _args['getVideoSharpness']:
		res= yi.cmd(yiAPI.getVideoSharpness)
		result.append(['getVideoSharpness',yiAPI.setVideoSharpness.values.index(res),res])
	if _args['getPhotoSharpness']:
		res= yi.cmd(yiAPI.getPhotoSharpness)
		result.append(['getPhotoSharpness',yiAPI.setPhotoSharpness.values.index(res),res])
	if _args['getVideoFieldOfView']:
		res= yi.cmd(yiAPI.getVideoFieldOfView)
		result.append(['getVideoFieldOfView',yiAPI.setVideoFieldOfView.values.index(res),res])
	if _args['getRecordMode']:
		res= yi.cmd(yiAPI.getRecordMode)
		result.append(['getRecordMode',yiAPI.setRecordMode.values.index(res),res])
	if _args['getCaptureMode']:
		res= yi.cmd(yiAPI.getCaptureMode)
		result.append(['getCaptureMode',yiAPI.setCaptureMode.values.index(res),res])
	if _args['getMeteringMode']:
		res= yi.cmd(yiAPI.getMeteringMode)
		result.append(['getMeteringMode',yiAPI.setMeteringMode.values.index(res),res])
	if _args['getVideoQuality']:
		res= yi.cmd(yiAPI.getVideoQuality)
		result.append(['getVideoQuality',yiAPI.setVideoQuality.values.index(res),res])
	if _args['getVideoColorMode']:
		res= yi.cmd(yiAPI.getVideoColorMode)
		result.append(['getVideoColorMode',yiAPI.setVideoColorMode.values.index(res),res])
	if _args['getPhotoColorMode']:
		res= yi.cmd(yiAPI.getPhotoColorMode)
		result.append(['getPhotoColorMode',yiAPI.setPhotoColorMode.values.index(res),res])
	if _args['getElectronicImageStabilizationState']:
		res= yi.cmd(yiAPI.getElectronicImageStabilizationState)
		result.append(['getElectronicImageStabilizationState',yiAPI.setElectronicImageStabilizationState.values.index(res),res])
	if _args['getAdjustLensDistortionState']:
		res= yi.cmd(yiAPI.getAdjustLensDistortionState)
		result.append(['getAdjustLensDistortionState',yiAPI.setAdjustLensDistortionState.values.index(res),res])
	if _args['getVideoMuteState']:
		res= yi.cmd(yiAPI.getVideoMuteState)
		result.append(['getVideoMuteState',yiAPI.setVideoMuteState.values.index(res),res])
	if _args['getVideoTimestamp']:
		res= yi.cmd(yiAPI.getVideoTimestamp)
		result.append(['getVideoTimestamp',yiAPI.setVideoTimestamp.values.index(res),res])
	if _args['getPhotoTimestamp']:
		res= yi.cmd(yiAPI.getPhotoTimestamp)
		result.append(['getPhotoTimestamp',yiAPI.setPhotoTimestamp.values.index(res),res])
	if _args['getLEDMode']:
		res= yi.cmd(yiAPI.getLEDMode)
		result.append('getLEDMode',resyiAPI.setLEDMode.values.index(res),[])
	if _args['getVideoStandard']:
		res= yi.cmd(yiAPI.getVideoStandard)
		result.append(['getVideoStandard',yiAPI.setVideoStandard.values.index(res),res])
	if _args['getTimeLapseVideoInterval']:
		res= yi.cmd(yiAPI.getTimeLapseVideoInterval)
		result.append(['getTimeLapseVideoInterval',yiAPI.setTimeLapseVideoInterval.values.index(res),res])
	if _args['getTimeLapsePhotoInterval']:
		res= yi.cmd(yiAPI.getTimeLapsePhotoInterval)
		result.append(['getTimeLapsePhotoInterval',yiAPI.setTimeLapsePhotoInterval.values.index(res),res])
	if _args['getTimeLapseVideoDuration']:
		res= yi.cmd(yiAPI.getTimeLapseVideoDuration)
		result.append(['getTimeLapseVideoDuration',yiAPI.setTimeLapseVideoDuration.values.index(res),res])
	if _args['getScreenAutoLock']:
		res= yi.cmd(yiAPI.getScreenAutoLock)
		result.append(['getScreenAutoLock',yiAPI.setScreenAutoLock.values.index(res),res])
	if _args['getAutoPowerOff']:
		res= yi.cmd(yiAPI.getAutoPowerOff)
		result.append(['getAutoPowerOff',yiAPI.setAutoPowerOff.values.index(res),res])
	if _args['getVideoRotateMode']:
		res= yi.cmd(yiAPI.getVideoRotateMode)
		result.append(['getVideoRotateMode',yiAPI.setVideoRotateMode.values.index(res),res])
	if _args['getBuzzerVolume']:
		res= yi.cmd(yiAPI.getBuzzerVolume)
		result.append(['getBuzzerVolume',yiAPI.setBuzzerVolume.values.index(res),res])
	if _args['getLoopDuration']:
		res= yi.cmd(yiAPI.getLoopDuration)
		result.append(['getLoopDuration',yiAPI.setLoopDuration.values.index(res),res])

	for res in result:
		print(res)

	if _args['setDateTime']!=None:
		yi.cmd(yiAPI.setDateTime, _args['setDateTime'])
	if _args['setSystemMode']!=None:
		yi.cmd(yiAPI.setSystemMode, yiAPI.setSystemMode.values[int(_args['setSystemMode'])])
	if _args['setVideoResolution']!=None:
		yi.cmd(yiAPI.setVideoResolution, yiAPI.setVideoResolution.values[int(_args['setVideoResolution'])])
	if _args['setPhotoResolution']!=None:
		yi.cmd(yiAPI.setPhotoResolution, yiAPI.setPhotoResolution.values[int(_args['setPhotoResolution'])])
	if _args['setPhotoWhiteBalance']!=None:
		yi.cmd(yiAPI.setPhotoWhiteBalance, yiAPI.setPhotoWhiteBalance.values[int(_args['setPhotoWhiteBalance'])])
	if _args['setVideoWhiteBalance']!=None:
		yi.cmd(yiAPI.setVideoWhiteBalance, yiAPI.setVideoWhiteBalance.values[int(_args['setVideoWhiteBalance'])])
	if _args['setPhotoISO']!=None:
		yi.cmd(yiAPI.setPhotoISO, yiAPI.setPhotoISO.values[int(_args['setPhotoISO'])])
	if _args['setVideoISO']!=None:
		yi.cmd(yiAPI.setVideoISO, yiAPI.setVideoISO.values[int(_args['setVideoISO'])])
	if _args['setPhotoExposureValue']!=None:
		yi.cmd(yiAPI.setPhotoExposureValue, yiAPI.setPhotoExposureValue.values[int(_args['setPhotoExposureValue'])])
	if _args['setVideoExposureValue']!=None:
		yi.cmd(yiAPI.setVideoExposureValue, yiAPI.setVideoExposureValue.values[int(_args['setVideoExposureValue'])])
	if _args['setPhotoShutterTime']!=None:
		yi.cmd(yiAPI.setPhotoShutterTime, yiAPI.setPhotoShutterTime.values[int(_args['setPhotoShutterTime'])])
	if _args['setVideoSharpness']!=None:
		yi.cmd(yiAPI.setVideoSharpness, yiAPI.setVideoSharpness.values[int(_args['setVideoSharpness'])])
	if _args['setPhotoSharpness']!=None:
		yi.cmd(yiAPI.setPhotoSharpness, yiAPI.setPhotoSharpness.values[int(_args['setPhotoSharpness'])])
	if _args['setVideoFieldOfView']!=None:
		yi.cmd(yiAPI.setVideoFieldOfView, yiAPI.setVideoFieldOfView.values[int(_args['setVideoFieldOfView'])])
	if _args['setRecordMode']!=None:
		yi.cmd(yiAPI.setRecordMode, yiAPI.setRecordMode.values[int(_args['setRecordMode'])])
	if _args['setCaptureMode']!=None:
		yi.cmd(yiAPI.setCaptureMode, yiAPI.setCaptureMode.values[int(_args['setCaptureMode'])])
	if _args['setMeteringMode']!=None:
		yi.cmd(yiAPI.setMeteringMode, yiAPI.setMeteringMode.values[int(_args['setMeteringMode'])])
	if _args['setVideoQuality']!=None:
		yi.cmd(yiAPI.setVideoQuality, yiAPI.setVideoQuality.values[int(_args['setVideoQuality'])])
	if _args['setVideoColorMode']!=None:
		yi.cmd(yiAPI.setVideoColorMode, yiAPI.setVideoColorMode.values[int(_args['setVideoColorMode'])])
	if _args['setPhotoColorMode']!=None:
		yi.cmd(yiAPI.setPhotoColorMode, yiAPI.setPhotoColorMode.values[int(_args['setPhotoColorMode'])])
	if _args['setElectronicImageStabilizationState']!=None:
		yi.cmd(yiAPI.setElectronicImageStabilizationState, yiAPI.setElectronicImageStabilizationState.values[int(_args['setElectronicImageStabilizationState'])])
	if _args['setAdjustLensDistortionState']!=None:
		yi.cmd(yiAPI.setAdjustLensDistortionState, yiAPI.setAdjustLensDistortionState.values[int(_args['setAdjustLensDistortionState'])])
	if _args['setVideoMuteState']!=None:
		yi.cmd(yiAPI.setVideoMuteState, yiAPI.setVideoMuteState.values[int(_args['setVideoMuteState'])])
	if _args['setVideoTimestamp']!=None:
		yi.cmd(yiAPI.setVideoTimestamp, yiAPI.setVideoTimestamp.values[int(_args['setVideoTimestamp'])])
	if _args['setPhotoTimestamp']!=None:
		yi.cmd(yiAPI.setPhotoTimestamp, yiAPI.setPhotoTimestamp.values[int(_args['setPhotoTimestamp'])])
	if _args['setLEDMode']!=None:
		yi.cmd(yiAPI.setLEDMode, yiAPI.setLEDMode.values[int(_args['setLEDMode'])])
	if _args['setVideoStandard']!=None:
		yi.cmd(yiAPI.setVideoStandard, yiAPI.setVideoStandard.values[int(_args['setVideoStandard'])])
	if _args['setTimeLapseVideoInterval']!=None:
		yi.cmd(yiAPI.setTimeLapseVideoInterval, yiAPI.setTimeLapseVideoInterval.values[int(_args['setTimeLapseVideoInterval'])])
	if _args['setTimeLapsePhotoInterval']!=None:
		yi.cmd(yiAPI.setTimeLapsePhotoInterval, yiAPI.setTimeLapsePhotoInterval.values[int(_args['setTimeLapsePhotoInterval'])])
	if _args['setTimeLapseVideoDuration']!=None:
		yi.cmd(yiAPI.setTimeLapseVideoDuration, yiAPI.setTimeLapseVideoDuration.values[int(_args['setTimeLapseVideoDuration'])])
	if _args['setScreenAutoLock']!=None:
		yi.cmd(yiAPI.setScreenAutoLock, yiAPI.setScreenAutoLock.values[int(_args['setScreenAutoLock'])])
	if _args['setAutoPowerOff']!=None:
		yi.cmd(yiAPI.setAutoPowerOff, yiAPI.setAutoPowerOff.values[int(_args['setAutoPowerOff'])])
	if _args['setVideoRotateMode']!=None:
		yi.cmd(yiAPI.setVideoRotateMode, yiAPI.setVideoRotateMode.values[int(_args['setVideoRotateMode'])])
	if _args['setBuzzerVolume']!=None:
		yi.cmd(yiAPI.setBuzzerVolume, yiAPI.setBuzzerVolume.values[int(_args['setBuzzerVolume'])])
	if _args['setLoopDuration']!=None:
		yi.cmd(yiAPI.setLoopDuration, yiAPI.setLoopDuration.values[int(_args['setLoopDuration'])])


	time.sleep(1)
	if _args['capturePhoto']:
		yi.cmd(yiAPI.capturePhoto)
	if _args['startRecording']:
		yi.cmd(yiAPI.startRecording)

	yi.close()
