
"use strict";

let GetPOI = require('./GetPOI.js')
let Acknowledgment = require('./Acknowledgment.js')
let GetMapConfiguration = require('./GetMapConfiguration.js')
let ListMaps = require('./ListMaps.js')
let SetMapConfiguration = require('./SetMapConfiguration.js')
let FinalApproachPose = require('./FinalApproachPose.js')
let DisableEmergency = require('./DisableEmergency.js')
let GetNodes = require('./GetNodes.js')
let RenameMap = require('./RenameMap.js')
let VisualLocRecognize = require('./VisualLocRecognize.js')
let SafetyZone = require('./SafetyZone.js')
let SetSubMapFloor = require('./SetSubMapFloor.js')
let ChangeBuilding = require('./ChangeBuilding.js')
let GetSubMap = require('./GetSubMap.js')
let SetPOI = require('./SetPOI.js')
let SaveMap = require('./SaveMap.js')

module.exports = {
  GetPOI: GetPOI,
  Acknowledgment: Acknowledgment,
  GetMapConfiguration: GetMapConfiguration,
  ListMaps: ListMaps,
  SetMapConfiguration: SetMapConfiguration,
  FinalApproachPose: FinalApproachPose,
  DisableEmergency: DisableEmergency,
  GetNodes: GetNodes,
  RenameMap: RenameMap,
  VisualLocRecognize: VisualLocRecognize,
  SafetyZone: SafetyZone,
  SetSubMapFloor: SetSubMapFloor,
  ChangeBuilding: ChangeBuilding,
  GetSubMap: GetSubMap,
  SetPOI: SetPOI,
  SaveMap: SaveMap,
};
