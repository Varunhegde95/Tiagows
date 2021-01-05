
"use strict";

let SetDatabase = require('./SetDatabase.js')
let AddTexturedObject = require('./AddTexturedObject.js')
let StartEnrollment = require('./StartEnrollment.js')
let StopEnrollment = require('./StopEnrollment.js')
let ChangeObjectRecognizerModel = require('./ChangeObjectRecognizerModel.js')
let Recognizer = require('./Recognizer.js')
let SelectTexturedObject = require('./SelectTexturedObject.js')

module.exports = {
  SetDatabase: SetDatabase,
  AddTexturedObject: AddTexturedObject,
  StartEnrollment: StartEnrollment,
  StopEnrollment: StopEnrollment,
  ChangeObjectRecognizerModel: ChangeObjectRecognizerModel,
  Recognizer: Recognizer,
  SelectTexturedObject: SelectTexturedObject,
};
