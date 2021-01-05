
"use strict";

let ASREvent = require('./ASREvent.js');
let VoiceActivity = require('./VoiceActivity.js');
let I18nArgument = require('./I18nArgument.js');
let TtsText = require('./TtsText.js');
let audiosignal = require('./audiosignal.js');
let AudioPlayerState = require('./AudioPlayerState.js');
let asrresult = require('./asrresult.js');
let asrupdate = require('./asrupdate.js');
let TTSstate = require('./TTSstate.js');
let I18nText = require('./I18nText.js');
let ASRStatus = require('./ASRStatus.js');
let Input = require('./Input.js');
let ASRSrvResponse = require('./ASRSrvResponse.js');
let AudioDeviceDescription = require('./AudioDeviceDescription.js');
let ASRLangModelMngmt = require('./ASRLangModelMngmt.js');
let actiontag = require('./actiontag.js');
let WebGuiEvent = require('./WebGuiEvent.js');
let ASRSrvRequest = require('./ASRSrvRequest.js');
let TtsMark = require('./TtsMark.js');
let ASRActivation = require('./ASRActivation.js');
let DirectionOfArrival = require('./DirectionOfArrival.js');
let EnablingSoundLocalisation = require('./EnablingSoundLocalisation.js');
let ASRLanguage = require('./ASRLanguage.js');
let InputArgument = require('./InputArgument.js');
let SoundGoal = require('./SoundGoal.js');
let SoundAction = require('./SoundAction.js');
let ASRFileAction = require('./ASRFileAction.js');
let ASRFileActionResult = require('./ASRFileActionResult.js');
let TtsGoal = require('./TtsGoal.js');
let AudioPlayActionGoal = require('./AudioPlayActionGoal.js');
let SoundFeedback = require('./SoundFeedback.js');
let SoundActionResult = require('./SoundActionResult.js');
let AudioPlayActionResult = require('./AudioPlayActionResult.js');
let TtsResult = require('./TtsResult.js');
let ASRFileFeedback = require('./ASRFileFeedback.js');
let AudioPlayAction = require('./AudioPlayAction.js');
let ASRFileActionFeedback = require('./ASRFileActionFeedback.js');
let AudioPlayResult = require('./AudioPlayResult.js');
let ASRFileActionGoal = require('./ASRFileActionGoal.js');
let SoundActionGoal = require('./SoundActionGoal.js');
let ASRFileGoal = require('./ASRFileGoal.js');
let SoundResult = require('./SoundResult.js');
let TtsActionGoal = require('./TtsActionGoal.js');
let TtsFeedback = require('./TtsFeedback.js');
let SoundActionFeedback = require('./SoundActionFeedback.js');
let AudioPlayGoal = require('./AudioPlayGoal.js');
let TtsActionResult = require('./TtsActionResult.js');
let TtsActionFeedback = require('./TtsActionFeedback.js');
let AudioPlayActionFeedback = require('./AudioPlayActionFeedback.js');
let TtsAction = require('./TtsAction.js');
let AudioPlayFeedback = require('./AudioPlayFeedback.js');
let ASRFileResult = require('./ASRFileResult.js');

module.exports = {
  ASREvent: ASREvent,
  VoiceActivity: VoiceActivity,
  I18nArgument: I18nArgument,
  TtsText: TtsText,
  audiosignal: audiosignal,
  AudioPlayerState: AudioPlayerState,
  asrresult: asrresult,
  asrupdate: asrupdate,
  TTSstate: TTSstate,
  I18nText: I18nText,
  ASRStatus: ASRStatus,
  Input: Input,
  ASRSrvResponse: ASRSrvResponse,
  AudioDeviceDescription: AudioDeviceDescription,
  ASRLangModelMngmt: ASRLangModelMngmt,
  actiontag: actiontag,
  WebGuiEvent: WebGuiEvent,
  ASRSrvRequest: ASRSrvRequest,
  TtsMark: TtsMark,
  ASRActivation: ASRActivation,
  DirectionOfArrival: DirectionOfArrival,
  EnablingSoundLocalisation: EnablingSoundLocalisation,
  ASRLanguage: ASRLanguage,
  InputArgument: InputArgument,
  SoundGoal: SoundGoal,
  SoundAction: SoundAction,
  ASRFileAction: ASRFileAction,
  ASRFileActionResult: ASRFileActionResult,
  TtsGoal: TtsGoal,
  AudioPlayActionGoal: AudioPlayActionGoal,
  SoundFeedback: SoundFeedback,
  SoundActionResult: SoundActionResult,
  AudioPlayActionResult: AudioPlayActionResult,
  TtsResult: TtsResult,
  ASRFileFeedback: ASRFileFeedback,
  AudioPlayAction: AudioPlayAction,
  ASRFileActionFeedback: ASRFileActionFeedback,
  AudioPlayResult: AudioPlayResult,
  ASRFileActionGoal: ASRFileActionGoal,
  SoundActionGoal: SoundActionGoal,
  ASRFileGoal: ASRFileGoal,
  SoundResult: SoundResult,
  TtsActionGoal: TtsActionGoal,
  TtsFeedback: TtsFeedback,
  SoundActionFeedback: SoundActionFeedback,
  AudioPlayGoal: AudioPlayGoal,
  TtsActionResult: TtsActionResult,
  TtsActionFeedback: TtsActionFeedback,
  AudioPlayActionFeedback: AudioPlayActionFeedback,
  TtsAction: TtsAction,
  AudioPlayFeedback: AudioPlayFeedback,
  ASRFileResult: ASRFileResult,
};
